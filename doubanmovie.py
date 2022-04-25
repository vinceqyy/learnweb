import requests
import json

# link = https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=

# Get url
# header url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20'
url = 'https://movie.douban.com/j/chart/top_list'

# Set up Parameters
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20',
}

# Set up headers
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}

# Send requests
response = requests.get(url = url, params = param, headers=header)

json_data = response.json()

# save response to html

filepath = 'download/' +'movies.json'

f = open(filepath, 'w', encoding='utf-8')
json.dump(json_data, fp=f, ensure_ascii=False)

print('completed')