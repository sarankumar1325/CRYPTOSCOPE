# CryptoScope: Real-Time Cryptocurrency Dashboard 💡

CryptoScope is a real-time cryptocurrency tracking and visualization tool powered by the Gemini 2.0 API and Streamlit. Designed for simplicity and efficiency, CryptoScope offers live updates on market metrics like bid/ask prices, last traded values, and trading volumes, with interactive visualizations to make crypto market analysis accessible and actionable.

![image](https://github.com/user-attachments/assets/dab12221-6498-4d07-a17d-1dfc04452bfa)


## Features

- **Live Updates**: Fetches and displays real-time market data every 5 seconds
- **Key Metrics**: Displays bid price, ask price, last traded value, and volume in both BTC and USD
- **Dynamic Visualizations**: Trend graphs and widgets for deeper insights into the crypto market
- **Scalability**: Framework built to integrate predictive analytics, portfolio tracking, or alert systems

## Technology Stack

- **API**: Gemini 2.0 API
- **Frontend**: Streamlit
- **Graphs**: Plotly and Matplotlib

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cryptoscope.git
cd cryptoscope
```

### 2. Install Dependencies

Ensure you have Python 3.8+ installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory with your Gemini API credentials:

```env
API_KEY=your_gemini_api_key
API_SECRET=your_gemini_api_secret
```

### 4. Run the Application

Launch the Streamlit app:

```bash
streamlit run app.py
```

## How It Works

- Connects to Gemini 2.0 API to fetch market data
- Updates information dynamically, showing bid/ask prices, last price, and volume
- Displays interactive charts for monitoring price and volume trends in real time

## Future Enhancements

- Introduce portfolio tracking for user investments
- Add predictive analytics using machine learning
- Expand to multiple exchanges for comparative analysis
- Implement notification systems for price alerts

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request to help us make CryptoScope even better.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Gemini API
- Streamlit
- Open-source developers for their invaluable resources
