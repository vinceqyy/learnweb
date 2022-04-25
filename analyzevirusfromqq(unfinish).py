'''
Objective: 
    find number of covid cases and analyze the result based on QQ website

Library:
    requests >>> pip install requests
    parsel >>> pip install parsel
    pandas
    pyecharts

Analysis:
    1. Open link: https://news.qq.com/zt2020/page/feiyan.htm#/
    2. Get request link 
    https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign&callback=jQuery35109299742628569403_1650512817452&_=1650512817453
    3. Filter the response for information needed
    4. 
'''
# send request
import requests
import json
import pprint
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&_=1650512817453'

response = requests.get(url)
#print(response.json())

# analyze data 
# xpath, css, re, json
# Json  {key1:value1, key2:value2, key3:value3}
json_data = response.json()['data']
pprint.pprint(json_data)
#json_data = json.loads(json_data)



