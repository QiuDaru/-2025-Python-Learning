import requests
url = "https://s.yimg.com/ny/api/res/1.2/F048.fCR2GjuEXC1zIbw.w--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTM1OQ--/https://media.zenfs.com/zh-tw/setn.com.tw/94e569eb3e1e8062b98ec83c22bb5288"
response = requests.get(url)
if response.status_code == 200:
    with open("python_logo.png", "wb") as f:
        f.write(response.content)
    print("圖片下載完成！")
else:
    print("圖片下載失敗，狀態碼：", response.status_code)
