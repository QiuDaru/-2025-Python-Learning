import pandas as pd

file = pd.read_csv('pandss/全國3大速食業資料集.csv')  
count = (file["公司名稱"] == "和德昌股份有限公司").sum()
print(count)

