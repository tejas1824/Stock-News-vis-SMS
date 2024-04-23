# Stock News Alert

This Python script tracks the stock price of a specified company and sends news alerts via SMS using Twilio when there's a significant price change.

## Overview

This script fetches the latest stock data for a given company from the Alpha Vantage API and checks for a significant percentage change in the stock price. If the percentage change exceeds a certain threshold, it retrieves news articles related to the company from the News API and sends them as SMS alerts using Twilio.

## Prerequisites

Before running the script, ensure you have the following:

1. Python installed on your system.
2. Pip installed for Python package management.
3. Access to the Alpha Vantage and News API, and a Twilio account for SMS messaging.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/stock-news-alert.git

   
Install the required Python packages:

pip install -r requirements.txt

Configuration:
Obtain API keys for Alpha Vantage and News API, and your Twilio SID and authentication token.
Update the constants in the script (STOCK_NAME, COMPANY_NAME, NEWS_API_KEY, TWILIO_SID, AUTH_TOKEN, API_KEY) with your API keys and Twilio credentials.
Replace "YOUR_TWILIO_NUMBER" with your Twilio phone number and "YOUR_PHONE_NUMBER" with the recipient phone number.
Usage
Run the script using Python:
python main.py

The script will fetch stock data, check for significant price changes, retrieve news articles if necessary, and send them as SMS alerts using Twilio.

Disclaimer
This script is for educational purposes only. Use it responsibly and at your own risk. Always do your own research and consult with a financial advisor before making any investment decisions.
Replace placeholders like `your_username` in the repository URL and update the configuration instructions and usage information accordingly. Save this README file in your repository's root directory as `README.md`.

