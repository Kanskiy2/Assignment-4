# Пример: сопоставление пользовательского ввода с CoinGecko ID
def normalize_coin_name(user_input):
    mapping = {
        "bitcoin": ("BTC", "bitcoin"),
        "ethereum": ("ETH", "ethereum"),
        "solana": ("SOL", "solana"),
        "cardano": ("ADA", "cardano"),
        "dogecoin": ("DOGE", "dogecoin"),
        # добавь больше по мере надобности
    }
    return mapping.get(user_input.lower(), (None, None))
