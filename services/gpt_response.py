import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(coin, price, market_data, news):
    prompt = f"""
Информация о {coin}:
Цена: ${price}
Капитализация: ${market_data['market_cap']}
Ранг: {market_data['rank']}
Новости:
- {news[0]}
- {news[1] if len(news) > 1 else ''}
- {news[2] if len(news) > 2 else ''}

Сформулируй краткий вывод на русском языке.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "user", "content": prompt }
        ]
    )
    return response.choices[0].message.content
