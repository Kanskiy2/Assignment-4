import requests
import os

def get_news(coin_symbol: str):
    key = os.getenv("CRYPTO_PANIC_KEY")
    url = "https://cryptopanic.com/api/v1/posts/"
    params = {
        "auth_token": key,
        "currencies": coin_symbol.upper()
    }
    try:
        res = requests.get(url, params=params)
        articles = res.json().get('results', [])[:3]
        return [a['title'] for a in articles]
    except:
        return ["Ошибка загрузки новостей."]
