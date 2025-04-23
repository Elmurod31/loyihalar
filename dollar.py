import requests

API_KEY = "2b7c2a5169c1b7251600340b"

currency = 'USD'

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
json_data = response.json()

kurs = json_data['conversion_rate']

print(kurs)