import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from textblob import TextBlob
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from get_stock_data import get_stock_data
from sentiment import get_news_sentiment

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')


stock_data = get_stock_data(stock_symbol = "AAPL",start_date = "2015-01-01",end_date = "2026-01-01")
# Example news headlines related to the stock
news_headlines = [
    "Apple shares hit all-time high",
    "Apple reports better-than-expected earnings",
    "Apple announces new product launch",
    "Apple stocks fall due to market conditions",
    "Apple faces supply chain issues"
]
news_sentiments = get_news_sentiment(news_headlines)
# Add a 'Sentiment' column to the stock data (use the sentiment value from the news data)
# For demonstration, just assigning random sentiment scores for each date (real-world implementation would map sentiment to dates)
stock_data['Sentiment'] = np.random.choice(news_sentiments, size=len(stock_data))

