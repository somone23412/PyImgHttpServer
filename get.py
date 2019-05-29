import requests
import json

url = 'http://192.168.2.201:9123'
urlGetCamera = url+'/vcn/cameras'

response = requests.get(urlGetCamera)
response
print(response.text)
camerainfo = []
for cminfo in json.loads(response.text)['cameras']:
    camerainfo.append(cminfo)
with open ('CameraList.json','w') as ci:
    json.dump(camerainfo,ci)
