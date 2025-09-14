import requests

x = requests.get("https://www.bbc.com/")
print(x.content)