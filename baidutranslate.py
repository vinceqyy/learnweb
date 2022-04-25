import requests
import json

# post url
url = 'https://fanyi.baidu.com/sug'

# set up headers
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}

# set up post parameters
keyword = 'cat'
data = {
    'kw':keyword
}

# send requests
response = requests.post(url = url, data=data, headers = header)

# save response from json format
json_data = response.json()

# save response to html

filepath = 'download/' + keyword +'.json'

f = open(filepath, 'w', encoding='utf-8')
json.dump(json_data, fp=f, ensure_ascii=False)

print('completed')