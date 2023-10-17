from bs4 import BeautifulSoup
from selenium import webdriver
from dataclasses import dataclass
from tabulate import tabulate


# Stock class for stock info
@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = 'USD'
    usd_price: float = 0

    def __post_init__(self):
        stock_info = get_price_info(self.ticker, self.exchange)

        if stock_info['ticker'] == self.ticker:
            self.price = stock_info['price']
            self.currency = stock_info['currency']
            self.usd_price = stock_info['USD-price']


# Position class to hold the stocks and quantity 
@dataclass
class Position:
    stock: Stock
    quantity: int


# Portfolio class to have a list of positions and calculate the total value
@dataclass
class Portfolio:
    positions: list[Position]

    def get_total_value(self):
        total_value = 0

        for position in self.positions:
            total_value += position.stock.usd_price * position.quantity

        return total_value 


def fx_currency_to_usd(currency):
    driver = webdriver.Chrome()
    url = f'https://www.google.com/finance/quote/{currency}-USD'
    driver.get(url)
    page_html = driver.page_source
    driver.quit()

    # get usd
    soup = BeautifulSoup(page_html, 'html.parser')
    price_div = soup.find('div', attrs={'data-last-price':True})
    usd_price = float(price_div['data-last-price'])

    return usd_price


# using selenuim to get the html
def get_price_info(ticker, exchange):

    # get html
    driver = webdriver.Chrome()
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    driver.get(url)
    page_html = driver.page_source
    driver.quit()

    # get price info
    soup = BeautifulSoup(page_html, 'html.parser')
    price_div = soup.find('div', attrs={'data-last-price': True})
    price = float(price_div['data-last-price'])
    currency = price_div['data-currency-code']
    usd_price = price

    if currency != 'USD':
        usd_price = round(fx_currency_to_usd(currency=currency)*price, 2)

    return {
        'ticker': ticker,
        'exchange': exchange,
        'price': price,
        'currency': currency,
        'USD-price': usd_price,
    }


#Display portfolio summary using Tabulate
def display_portfolio_summary(portfolio):
    if not isinstance(portfolio, Portfolio):
        raise TypeError('Please provide an instance of portfolio type.')
    
    portfolio_value = portfolio.get_total_value()

    position_data = []

    for position in portfolio.positions:
        position_data.append([
            position.stock.ticker,
            position.stock.exchange,
            position.stock.usd_price,
            position.quantity,
            position.stock.usd_price * position.quantity,
            position.stock.usd_price * position.quantity / portfolio_value * 100
        ])

    print(tabulate(position_data,
                    headers=['Ticker', 'Exchange', 'Price', 'Quantity', 'Market Value', '% Allocation'],
                    tablefmt='psql',
                    floatfmt='.2f'))
    
    print(f'Total Portfolio Value: ${portfolio_value:,.2f}')
        
    


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
