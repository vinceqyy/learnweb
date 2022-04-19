'''
Objective: 
    Browse thru the web page and all sub pages and save all photos to local drive


Library:
    requests >>> pip install requests
    parsel >>> pip install parsel

Analysis:
    1. Send request for the link: http://www.cosplay8.com/pic/xiezhen/
    2. Get response from the website
    3. Analyze the response and parse the subpages links
    4. Send request for the subpages
    5. Get response from subpages
    6. Analyze the response and get the download link
    7. Save the pic
'''

# import library
import requests
import parsel

# 1. Send request for the main page
url = 'http://www.cosplay8.com/pic/xiezhen/'
# Go to Browser, Network, then refresh the page, find a page and view the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}
response = requests.get(url, headers = headers)
# Response [200] : Successful
# print(response)

# 2. Get response from the website

# change encoding to utf-8 to display chinese
response.encoding = 'utf-8'
# print(response.text)
html_data = response.text

# 3. Analyze the response and parse the subpages links
# on Browser, Go to Elements, crl+F to search '.txtover'
# In this case, all subpage link has 'class = txtover'
selector = parsel.Selector(html_data)
# url_list = selector.css('.txtover').getall()
# use .to select class
# Use ::attr(herf) to filter contents with herf attributes
url_list = selector.css('.txtover::attr(href)').getall()
title_list = selector.css('.txtover::attr(title)').getall()
#print(url_list)
#print(title_list)
# concat url and title
zip_data = zip(title_list, url_list)
# 4. send requests for subpages
for title, sub_url in zip_data:
    link = 'http://www.cosplay8.com' + sub_url
    #print(title, link)
    response_sub = requests.get(link, headers = headers)
    response_sub.encoding = 'utf-8'
    # 5 Get response from subpage
    html_sub = response_sub.text
    selector_sub = parsel.Selector(html_sub)
    # 6. Analyze the response and get the download link
    # use # for search id
    sub_img = selector_sub.css('#bigimg::attr(src)').get()
    img_url = 'http://www.cosplay8.com' + sub_img
    # print(img_url)
    # 7 Save pic
    img_data = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    with open (f'download/img/{img_name}', mode = 'wb') as f:
        f.write(img_data)


