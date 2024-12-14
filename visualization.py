import matplotlib.pyplot as plt

def plot_stock_price(data, ticker):
    plt.figure(figsize=(10, 4))
    plt.plot(data['Close'], label=f'{ticker} Closing Price')
    plt.title(f'Stock Price of {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

