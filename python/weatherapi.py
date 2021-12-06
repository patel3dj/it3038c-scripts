import requests
import json

print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=bd4cc3b5e68d937c70fa11ad02357ec4')
data =r.json()

#print(type(data['weather'][0]['description']))
print("The weather in %s is %s" % (zip, data['weather'] [0] ['description']))

