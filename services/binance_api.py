import requests

def get_price(coin_symbol: str):
    symbol = coin_symbol.upper() + "USDT"
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        res = requests.get(url)
        return float(res.json()['price'])
    except:
        return None
