import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com"
response = requests.get(url)

if response.status_code == 200:
   
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all( 'span')

    for headline in headlines:
        print(headline.get_text())
else:
    print(f"請求失敗，狀態碼：{response.status_code}")
print("結束")