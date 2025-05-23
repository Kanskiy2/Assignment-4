import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from utils import normalize_coin_name
from services.binance_api import get_price
from services.coingecko_api import get_market_data
from services.cryptopanic_api import get_news
from services.gpt_response import generate_response

st.set_page_config(page_title="AI Crypto Assistant", layout="centered")
st.title("🪙 AI Crypto Assistant")

user_input = st.text_input("Введите монету (напр. bitcoin, ethereum):").strip().lower()

if user_input:
    coin_symbol, coin_id = normalize_coin_name(user_input)

    if not coin_symbol or not coin_id:
        st.error("❌ Монета не поддерживается или введена с ошибкой.")
    else:
        st.info("🔄 Получаем данные...")

        price = get_price(coin_symbol)
        market_data = get_market_data(coin_id)
        news = get_news(coin_symbol)

        if price and market_data:
            st.subheader(f"📊 Данные по {market_data['name']}")
            st.markdown(f"**Цена:** ${price}")
            st.markdown(f"**Капитализация:** ${market_data['market_cap']}")
            st.markdown(f"**Ранг:** {market_data['rank']}")

            st.subheader("📰 Новости:")
            for n in news:
                st.markdown(f"- {n}")

            st.subheader("🤖 Ответ от AI:")
            gpt_text = generate_response(user_input, price, market_data, news)
            st.success(gpt_text)
        else:
            st.error("❌ Не удалось получить данные с Binance или CoinGecko.")
