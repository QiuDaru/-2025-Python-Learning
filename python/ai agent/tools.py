import webbrowser
def open_web(web_URL:str): #網站開啟"https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"
    webbrowser.open(web_URL)




























def guess_number(answer:int,user:int): #第一個數是答案 第二個是玩家輸入
    try:
        
        if user>answer:
            return "太大"
        if user<answer:
            return "太小"
        if user==answer:
            return "正確"
    except:
        pass




def play_rps(ai_choice: str, player_choice: str) -> str: #剪刀石頭布遊戲
    """
    剪刀石頭布對戰判定
    
    參數：
        ai_choice (str): AI出的拳（剪刀、石頭、布）
        player_choice (str): 玩家出的拳（剪刀、石頭、布）
    
    回傳：
        str: 比賽結果，例如 "你贏了"、"你輸了"、"平手"
    """
    try:
        valid_choices = ["剪刀", "石頭", "布"]
        if ai_choice not in valid_choices or player_choice not in valid_choices:
            return "請輸入有效的拳：剪刀、石頭、布"

        if ai_choice == player_choice:
            return "平手"
        elif (
            (player_choice == "剪刀" and ai_choice == "布") or
            (player_choice == "石頭" and ai_choice == "剪刀") or
            (player_choice == "布" and ai_choice == "石頭")
        ):
            return "你贏了"
        else:
            return "你輸了"
    except Exception as e:
        return f"出錯了：{str(e)}"












from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def find_stock(x:str): #輸入股票編號0050,00940之類的
    driver = webdriver.Chrome()
    driver.get("https://tw.stock.yahoo.com/")

    """search = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID,"ssb-search-input"))
    )"""
    search = driver.find_element(By.ID,"ssb-search-input")


    search.send_keys(x)
    time.sleep(10)
    search.send_keys(Keys.ENTER)
    time.sleep(20)


    driver.quit()
#找到股票程式


