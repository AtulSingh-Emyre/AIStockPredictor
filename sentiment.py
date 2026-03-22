from textblob import TextBlob


def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def get_news_sentiment(news_headlines):
    # Calculate sentiment for each headline (assuming each headline corresponds to a stock entry)
    news_sentiments = [get_sentiment(headline) for headline in news_headlines]
    return news_sentiments
