# 安裝必要的套件（Transformers、Datasets、Evaluate 和 PyTorch）


# 匯入所需的函式庫和類別
import numpy as np
import torch
from datasets import load_dataset
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
import evaluate

# 1. 載入 IMDb 電影評論資料集 (如果尚未下載會自動下載)
dataset = load_dataset("imdb")
train_ds = dataset["train"]    # 25,000 筆訓練資料
test_ds  = dataset["test"]     # 25,000 筆測試資料

# 為了加快示範，隨機抽取較小的子集，例如 1000 筆訓練資料與 200 筆測試資料
train_ds_small = train_ds.shuffle(seed=42).select(range(1000))
test_ds_small  = test_ds.shuffle(seed=42).select(range(200))

# 2. 載入 DistilBERT 分詞器，用於將文字轉換為模型輸入的編碼
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

# 定義分詞函式：對輸入的評論文本進行編碼，截斷長度超過128的部分，並補齊至固定長度
def tokenize_function(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

# 對訓練和測試資料集進行分詞編碼
train_encodings = train_ds_small.map(tokenize_function, batched=True)
test_encodings  = test_ds_small.map(tokenize_function, batched=True)

# 設定資料格式為 PyTorch tensor，並僅保留模型所需的欄位
train_encodings.set_format("torch", columns=["input_ids", "attention_mask", "label"])
test_encodings.set_format("torch", columns=["input_ids", "attention_mask", "label"])

# 3. 載入預訓練的 DistilBERT 序列分類模型（num_labels=2 表示二分類）
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# 4. 使用 evaluate 套件載入 accuracy 評估指標
accuracy = evaluate.load("accuracy")

# 定義計算評估指標的函式：這將在每個 evaluation 時被 Trainer 調用
def compute_metrics(eval_pred):
    logits, labels = eval_pred       # 模型預測的原始分數和真實標籤
    predictions = np.argmax(logits, axis=-1)  # 選取分數最高的類別作為預測結果
    return accuracy.compute(predictions=predictions, references=labels)

# 5. 設定訓練參數，如訓練週期數、批次大小、評估策略等
training_args = TrainingArguments(
    output_dir="./results",          # 模型輸出保存目錄
    num_train_epochs=1,              # 訓練 epoch 數（此處設為 1 以示範）
    per_device_train_batch_size=16,  # 每個裝置(GPU/CPU)的訓練批次大小
    per_device_eval_batch_size=16,   # 每個裝置的評估批次大小
    learning_rate=2e-5,              # 學習率
    weight_decay=0.01,               # 權重衰減率 (避免過擬合)
    evaluation_strategy="epoch",     # 每個 epoch 結束後進行評估
    save_strategy="no",              # 不額外保存檢查點 (checkpoint) 以簡化流程
    logging_strategy="epoch",        # 每個 epoch 結束後輸出訓練日誌
    report_to="none"                 # 不使用內建的日誌報告 (如 TensorBoard)
)

# 6. 初始化 Trainer，並傳入模型、訓練參數、資料集以及評估函式
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_encodings,
    eval_dataset=test_encodings,
    compute_metrics=compute_metrics    # 指定評估指標計算函式
)

# 開始模型訓練 (微調過程)
trainer.train()

# 7. 在測試資料集上評估模型，並列印準確率
eval_results = trainer.evaluate()
print(f"Accuracy: {eval_results['eval_accuracy']:.4f}")

# 8. 使用訓練好的模型進行單一句子情感預測示範
sample_text = "This movie was absolutely fantastic! I loved it."  # 範例評論
inputs = tokenizer(sample_text, return_tensors="pt", truncation=True, padding="max_length", max_length=128)
outputs = model(**inputs)
predicted_class = torch.argmax(outputs.logits, dim=1).item()
label_map = {0: "負面", 1: "正面"}  # 定義預測結果對應的中文標籤
print(f"範例評論: \"{sample_text}\"")
print(f"預測情感: {label_map[predicted_class]}")
