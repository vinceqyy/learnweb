import requests

# website : http://www.kfc.com.cn/kfccda/storelist/index.aspx

# Get url from headers
# link = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'


# Set up headers
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}


# Set up Parameters
keyword = '深圳'

data ={
    'cname':'',
    'pid':'',
    'keyword': keyword,
    'pageIndex':'1',
    'pageSize': '10',
}

response = requests.post(url = url, data=data, headers = header)

response_text = response.text

print(response_text)

# save reponse to html
filepath = 'download/' + keyword +'.html'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(response_text)

print('Completed')
