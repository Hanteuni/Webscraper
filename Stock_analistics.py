class Stock_analistics():

    def __init__(self, ticker):
        self.ticker_mame = ticker
        print(self.ticker_mame)
        self.get_basic_info(self.ticker_mame)


    def stock_checker(self):
        print("i had to  make some changes")

    def webscrape_yahoo_page(self):
        # import webzooi
        pass


    def get_basic_info(self,ticker):
        print("This is the ticker: " + ticker)
        print("yea tis is a price")


# TODO: get basic info
# ticker_name, stock_price, company_name
# TODO: get advanced info
# Market_cap, PE_ratio, EPS, 1y_Target, Beta, outstanding_shares, forward_PE
# TODO: get more info
# price_to_sales, price_to_book, ROI, ROA, revenue
# TODO: WIP balance sheets and historical data

test = Stock_analistics("NIO")
