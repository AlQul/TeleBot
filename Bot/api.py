import requests
import json

base_key = "USD"
quote_key = "RUB"
amount = 100

r = requests.get(f"https://api.exchangeratesapi.io/latest?base={base_key}&symbols={quote_key}")
resp = json.loads(r.content)
new_price = resp['rates'][quote_key] * amount

print(new_price)