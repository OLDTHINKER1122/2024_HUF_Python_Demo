#https://opendata.cwa.gov.tw/dist/opendata-swagger.html
from urllib.request import urlopen
import ssl
import json

json_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-FAAB3B91-B4D2-4C1F-9F3C-E2D01B4F718A&format=JSON"

ssl._create_default_https_context = ssl._create_unverified_context
response = urlopen(json_url)

data = response.read()
output = json.loads(data)

location=output['records']['location'][0]['weatherElement']


for i in location:
    print(f'{i}')


for i in location:
  with open('mydata.json', 'wb') as f:
    f.write(json.dumps(i).encode())
  







