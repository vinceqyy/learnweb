import requests

# link = 'https://www.sogou.com/web?query=vincent'

url = 'https://www.sogou.com/web'

# input keyword
keyword = 'Music'

# set up parameters
param = {
    'query':keyword
}

# set up headers
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}

''' 
get response
Three important parameters:
1.url
2.params
3.headers
'''
response = requests.get(url = url, params = param, headers=header)

response_text = response.text

# save reponse to html
filepath = 'download/' + keyword +'.html'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(response_text)

print('Completed')