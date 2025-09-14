import webbrowser

# 你可以自己改成常用的網站
favorites = {
    1: ("Google", "https://www.google.com"),
    2: ("YouTube", "https://www.youtube.com"),
    3: ("OpenAI", "https://www.openai.com"),
    4: ("GitHub", "https://github.com"),
    5: ("Gmail", "https://mail.google.com")
}

print("🚀 常用網站快速開啟器 🚀")
print("------------------------")

# 印出選單
for key, (name, url) in favorites.items():
    print(f"{key}. {name}")

print("0. 一次打開全部")

# 使用者選擇
choice = input("請輸入編號（或輸入 0 打開全部）：")

# 判斷輸入
if choice == "0":
    for name, url in favorites.values():
        webbrowser.open(url)
        print(f"✅ 已打開：{name}")
        
elif choice.isdigit() and int(choice) in favorites:
    name, url = favorites[int(choice)]
    webbrowser.open(url)
    print(f"✅ 已打開：{name}")
else:
    print("⚠️ 無效輸入，請重新執行程式")
