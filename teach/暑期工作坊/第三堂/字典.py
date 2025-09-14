# 定義一個學生成績字典
scores = {
    "小明": {"數學": 85, "英文": 90, "科學": 88},
    "小華": {"數學": 78, "英文": 82, "科學": 91},
    "小美": {"數學": 92, "英文": 85, "科學": 89},
}

# 輸入學生姓名
student_name = input("請輸入學生姓名：")

# 查詢並顯示成績
if student_name in scores:
    print(f"{student_name} 的成績如下：")
    for subject, score in scores[student_name].items():
        print(f"{subject}: {score}")
else:
    print("查無此學生！")
