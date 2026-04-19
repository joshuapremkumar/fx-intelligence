import requests

def get_rate(base, target):
    url = f"https://api.frankfurter.app/latest?from={base}&to={target}"
    res = requests.get(url).json()
    return res["rates"][target]