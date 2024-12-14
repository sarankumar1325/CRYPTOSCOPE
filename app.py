import streamlit as st
import requests
import plotly.graph_objects as go
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file (if needed)
load_dotenv()

# Gemini API base URL
GEMINI_API_URL = "https://api.gemini.com/v1/pubticker/"

# Function to get cryptocurrency data from Gemini API
def get_gemini_data(symbol="btcusd"):
    response = requests.get(GEMINI_API_URL + symbol)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to retrieve data from Gemini API")
        return None

# Streamlit App Layout
st.set_page_config(page_title="Crypto Price Viewer", page_icon="💹", layout="wide")
st.title("Real-Time Cryptocurrency Data")

# Sidebar for selecting cryptocurrency pair
st.sidebar.header("Select Cryptocurrency Pair")
symbol = st.sidebar.selectbox(
    "Choose a currency pair:",
    ["btcusd", "ethusd", "ltcusd", "xrpusd", "bnbusd"]
)

# Display a header for the selected symbol
st.subheader(f"Market Information for {symbol.upper()}")

# Placeholder for the graph
graph_placeholder = st.empty()

# Variables to store historical data for graphing
historical_times = []
historical_bid_prices = []
historical_ask_prices = []
historical_last_prices = []

# Create columns for a clean layout
col1, col2 = st.columns([2, 1])

# Fetch data and update the graph
while True:
    data = get_gemini_data(symbol)

    if data:
        # Manually add the symbol based on selection
        bid = float(data['bid'])
        ask = float(data['ask'])
        last = float(data['last'])
        volume_btc = float(data['volume']['BTC'])
        volume_usd = float(data['volume']['USD'])

        # Add data to the historical lists
        historical_times.append(time.time())
        historical_bid_prices.append(bid)
        historical_ask_prices.append(ask)
        historical_last_prices.append(last)

        # Limit the history to the last 50 entries to avoid excessive memory use
        if len(historical_times) > 50:
            historical_times.pop(0)
            historical_bid_prices.pop(0)
            historical_ask_prices.pop(0)
            historical_last_prices.pop(0)

        # Display price information in the first column
        with col1:
            st.markdown(f"**Last Price:** ${last}")
            st.markdown(f"**Bid Price:** ${bid}")
            st.markdown(f"**Ask Price:** ${ask}")
            st.markdown(f"**Volume (BTC):** {volume_btc:.2f} BTC")
            st.markdown(f"**Volume (USD):** ${volume_usd:,.2f} USD")

        # Graph in the second column
        with col2:
            st.markdown("### Price Graph (Bid, Ask, Last)")
            
            # Create a plotly graph
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=historical_times, y=historical_bid_prices, mode='lines', name='Bid Price', line=dict(color='blue')))
            fig.add_trace(go.Scatter(x=historical_times, y=historical_ask_prices, mode='lines', name='Ask Price', line=dict(color='red')))
            fig.add_trace(go.Scatter(x=historical_times, y=historical_last_prices, mode='lines', name='Last Price', line=dict(color='green')))
            
            # Update layout for better presentation
            fig.update_layout(
                title="Live Prices for " + symbol.upper(),
                xaxis_title="Time",
                yaxis_title="Price (USD)",
                showlegend=True,
                template="plotly_dark",
                margin=dict(l=40, r=40, t=40, b=40)
            )

            graph_placeholder.plotly_chart(fig, use_container_width=True)

        # Adding a refresh interval
        time.sleep(5)  # Update every 5 seconds
    else:
        st.warning("No data available for the selected cryptocurrency pair.")
