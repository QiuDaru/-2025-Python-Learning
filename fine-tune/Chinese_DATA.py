from datasets import load_dataset
def data_chinese():
    ds = load_dataset("Mxode/Chinese-Instruct", "dpsk-r1-distil")
    print("資料加載完成")
    return ds
print("函式加載完成")