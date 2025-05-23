import requests

def get_market_data(coin_id: str):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "ids": coin_id.lower()}
    try:
        res = requests.get(url, params=params)
        data = res.json()[0]
        return {
            "name": data["name"],
            "market_cap": data["market_cap"],
            "rank": data["market_cap_rank"]
        }
    except:
        return None
