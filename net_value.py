import requests
import time

url = 'http://api.fund.eastmoney.com/f10/lsjz'
# url = 'http://api.fund.eastmoney.com/f10/lsjz?fundCode=161725&pageIndex=1&pageSize=20'
ts = time.time()
payload = {
    'fundCode':'070002', 
    'pageIndex':1, 
    'pageSize':20, 
    'startDate':'2020-03-01', 
    'endDate':'2020-03-29',
    '_':ts
    }
header = {
    'Host': 'api.fund.eastmoney.com',    
    'Referer': 'http://fundf10.eastmoney.com/jjjz_161725.html', 
    'User-Agent': 'PostmanRuntime/7.23.0'
}

r0 = requests.get(url, headers=header, params=payload)

print(r0.url)
print(r0.json())
