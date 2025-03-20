import requests

# pip install requests
url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = requests.get(url)
print(response)  # <Response [200]>

print(response.text)
data = response.json()
print(type(data))
print(data)
# {'table': 'A',
# 'currency': 'euro',
# 'code': 'EUR',
# 'rates': [{'no': '021/A/NBP/2025', 'effectiveDate': '2025-01-31', 'mid': 4.213}]}

print(data['currency'])  # euro
print(data['rates'])
# [
# {'no': '021/A/NBP/2025', 'effectiveDate': '2025-01-31', 'mid': 4.213}
# ]
print(data['rates'][0])  # {'no': '021/A/NBP/2025', 'effectiveDate': '2025-01-31', 'mid': 4.213}
print(data['rates'][0]['mid'])
