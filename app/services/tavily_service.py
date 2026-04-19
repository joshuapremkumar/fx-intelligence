import os
import requests

API_KEY = os.getenv("TAVILY_API_KEY")

def get_news(query):
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": API_KEY,
        "query": query,
        "max_results": 3
    }
    res = requests.post(url, json=payload).json()
    return res.get("results", [])