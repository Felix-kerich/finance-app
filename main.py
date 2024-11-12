import yfinance as yf

print("Hello user")
STK = input("Enter the share name: ")

# Fetch historical data with a valid period
data = yf.Ticker(STK).history(period="1d")

# Access the 'Close' column and get the last value
last_market_price = data['Close'].iloc[-1]

print("Last market price:", last_market_price)



