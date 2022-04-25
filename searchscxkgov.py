import requests

# website: http://scxk.nmpa.gov.cn:81/xk/

# get url from header
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5nryweihe6QA7HDaJqRTJvLpj9JWy7C1301nSSBQKezEVEjThbf3h04yw0.asTR02FfgqQL3utmzequ8.3scYQKeb9bmKa6SsxPlLKIsILUBfJwjwP7LbQwKDfRllfJB0Pl0k.zbXG3wMG37lRAlykdqRB_041maXjSCs_oIHTp4b78rcnS4ZBW_8RbGSNpsXzbB7Wr9xNC3ekVXcGjk9l6hmWPLDQs86uuJJEkG_Y0a98xSm5ekWVhYGLXrLh9IRk4Q.xgsidMO.vxDwmEZBOmXT2._dMHBlanoqKyWaNh9&8X7Yi61c=4dTz1yAoWC9akDOU4oyb_iGRPQkRTTTpCNQ704suVAwykYMGXmu8hr7vO2fb6aLT4Za1im4OK9TjAlX7D2J0xjzwjy9dPAyAtl.dqNcyVF1n5V5ziLxbDQTFpm7dyCPmK'

# Set up headers
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}

# Set up data
data ={
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName':'' ,
    'conditionType': '1',
    'applyname': '',
    'applysn': '',
}

# send request
response = requests.post(url = url, headers = header, data = data)
print(response)

#json_data = response.json()

#print(json_data)