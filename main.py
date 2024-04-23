import requests
from twilio.rest import Client

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

# Fetching stock data
response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()

# Extracting yesterday's and day before yesterday's closing prices
data_list = [value for (key, value) in data["Time Series (Daily)"].items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# Calculating price difference and percentage difference
price_difference = (yesterday_closing_price - day_before_yesterday_closing_price)
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = round((price_difference / day_before_yesterday_closing_price) * 100)

# Checking if percentage difference is significant
if abs(percentage_difference) > 1:
    print("Get News")
    # Fetching news data
    response1 = requests.get(NEWS_ENDPOINT, params={"qInTitle": COMPANY_NAME, "apiKey": NEWS_API_KEY})
    articles = response1.json()["articles"]

    # Getting the first 3 articles
    three_articles = articles[:3]

    # Formatting articles for Twilio
    formatted_articles = [
        f"{STOCK_NAME} : {up_down} {percentage_difference}%\nHeadline: {article['title']}\nBrief: {article['description']}\n"
        for article in three_articles]

    # Twilio client setup
    client = Client(TWILIO_SID, AUTH_TOKEN)

    # Sending articles via Twilio
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="YOUR_TWILIO_NUMBER",
            to="YOUR_PHONE_NUMBER"
        )
