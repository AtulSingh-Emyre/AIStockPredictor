import yfinance as yf

def get_stock_data(stock_symbol, start_date, end_date):
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    stock_data['Date'] = stock_data.index
    stock_data = stock_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    return stock_data