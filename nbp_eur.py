import requests

url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = requests.get(url)
print(response)

print(response.text)
data = response.json()
print(type(data))
print(data)

print(data['currency'])
print(data['rates'])
print(data['rates'][0])
print(data['rates'][0]['mid'])