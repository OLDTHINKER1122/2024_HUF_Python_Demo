from urllib.request import urlopen
import ssl
import json

#json_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=KEY&format=JSON"
json_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-FAAB3B91-B4D2-4C1F-9F3C-E2D01B4F718A&format=JSON"

ssl._create_default_https_context = ssl._create_unverified_context
response = urlopen(json_url)
data = response.read()
output = json.loads(data)
location=output['records']['location']

for i in location:
    print(f'{i}')

for i in location:
    city = i['locationName']    # 縣市名稱
    wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
    pop8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
    mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
    ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
    maxt8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
    print(f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')


