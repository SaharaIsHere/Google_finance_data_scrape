# Google_finance_data_scrape
# README: Stock Portfolio Analysis with Web Scraping

This Python script is designed to create and analyze a stock portfolio using web scraping techniques. It uses the BeautifulSoup library for parsing HTML and the Selenium library to automate web interactions. The code fetches real-time stock data from Google Finance, calculates the total portfolio value, and displays a summary using the Tabulate library.

**Disclaimer:** This code is inspired by Project 1 from the Udemy course 'The Ultimate Web Scraping With Python Bootcamp 2023' by Andy Bek, with the modification of using Selenium for web scraping.

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Code Structure](#code-structure)
- [Credits](#credits)

## Requirements
Before using this script, you need to have the following dependencies installed:
- Python 3.x
- Selenium
- BeautifulSoup
- Tabulate
- Chrome web browser
- Chrome WebDriver

You can install the required Python packages using pip:

```bash
pip install selenium beautifulsoup4 tabulate
```

Make sure you have the Chrome WebDriver downloaded and placed in your system's PATH.

## Usage
1. Import the necessary libraries: `BeautifulSoup`, `Selenium`, `tabulate`.
2. Define your stock positions by creating `Stock` instances with the ticker symbol and exchange.
3. Create a list of `Position` objects that specify the stock and the quantity you own.
4. Instantiate a `Portfolio` by passing the list of positions.
5. Use the `display_portfolio_summary()` function to view a summary of your portfolio.

Here's an example of how to use the code:

```python
if __name__ == '__main__':
    shop = Stock('SHOP', 'TSE')
    msft = Stock('MSFT', 'NASDAQ')
    googl = Stock('GOOGL', 'NASDAQ')
    bns = Stock('BNS', 'TSE')

    positions = [Position(shop, 18),
                 Position(msft, 20),
                 Position(googl, 200),
                 Position(bns, 35)]
    
    portfolio = Portfolio(positions)

    display_portfolio_summary(portfolio)
```

## How It Works
1. The code defines a `Stock` class to store information about a stock, such as its ticker symbol, exchange, price, currency, and USD price.

2. It also defines a `Position` class, which associates a `Stock` with the quantity of that stock held in the portfolio.

3. The `Portfolio` class is used to group a list of positions, and it has a method `get_total_value()` to calculate the total portfolio value in USD.

4. The `fx_currency_to_usd()` function uses Selenium to fetch the conversion rate of a foreign currency to USD from Google Finance.

5. The `get_price_info()` function scrapes real-time stock price data for a given stock and exchange.

6. The `display_portfolio_summary()` function uses Tabulate to create a tabular summary of the portfolio, including ticker, exchange, price, quantity, market value, and percentage allocation.

7. In the main part of the script, you define your stock positions, create a portfolio, and then display the portfolio summary.

## Code Structure
- The code follows a modular structure with well-defined data classes for `Stock`, `Position`, and `Portfolio`.
- Web scraping is performed in separate functions, such as `fx_currency_to_usd()` and `get_price_info()`, making the code easy to maintain and extend.

## Credits
This code was inspired by Project 1 in the Udemy course 'The Ultimate Web Scraping With Python Bootcamp 2023' by Andy Bek. The original project served as a foundation for creating a stock portfolio analysis tool using web scraping, with the addition of Selenium for improved data extraction.

Please note that this code is provided for educational and informational purposes and should not be used for financial decisions without proper validation and consideration of risks.
