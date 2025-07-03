from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, TrainingArguments
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, TaskType
from trl import SFTTrainer

# === 模型與 tokenizer ===
model_id = "meta-llama/Meta-Llama-3-8B"  # 需先申請權限 &登入 huggingface-cli

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16"
)

tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
tokenizer.pad_token = tokenizer.eos_token  # LLaMA 沒有 pad token，設為 eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    quantization_config=bnb_config,
    torch_dtype="auto"
)

# === LoRA 配置 ===
peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    bias="none",
    target_modules=["q_proj", "v_proj"]
)

model = get_peft_model(model, peft_config)

# === 載入資料集 ===
dataset = load_dataset("Mxode/Chinese-Instruct")
train_data = dataset["train"].shuffle(seed=42).select(range(3000))  # 建議小樣本先測試
print("資料庫加載完成")

 #=== 訓練參數 ===
training_args = TrainingArguments(
    output_dir="./llama3-chinese-instruct",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    num_train_epochs=3,
    learning_rate=2e-4,
    logging_steps=10,
    save_strategy="epoch",
    save_total_limit=2,
    gradient_checkpointing=True,
    bf16=False,
    fp16=True,
    report_to="none"
)
print("訓練參數加載完成")
 #=== 微調器 ===
def formatting_func(example):
    return f"### 問題：{example['prompt']}\n\n### 回答：{example['response']}"
trainer = SFTTrainer(
    model=model,
    #tokenizer=tokenizer,
    train_dataset=train_data,
    args=training_args,
    peft_config=peft_config,
    #dataset_text_field="output",
    #max_seq_length=1024,
    formatting_func=formatting_func
)

trainer.train()
print("微調器加載完成")
# #=== 儲存模型 ===
# trainer.model.save_pretrained("./llama3-chinese-instruct")
# tokenizer.save_pretrained("./llama3-chinese-instruct")
# print("訓練完成")

