import requests

def get_rate(base, target):
    url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"
    res = requests.get(url).json()
    return res["rates"][target]