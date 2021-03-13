class stock_statistics:

    def __init__(self, ticker_name, full_name, share_price, outstanding_shares):
        self.full_name = full_name
        self.ticker_name = ticker_name
        self.share_price = share_price
        self.outstanding_shares = outstanding_shares
        self.total_debt
        self.cash
        self.cash_equivilents
        self.predicted_earings_per_share
        self.earnings_per_share_12m
        self.annual_eps_growth
        self.book_value_share
        self.net_income
        self.total_assets
        self.shareholder_equity

        self.market_cap = market_cap(self.share_price, self.outstanding_shares)
        self.enterprice_value = enterprice_value(self.market_cap, self.total_debt, self.cash, self.cash_equivilents)
        self.forward_price_to_earnings = forward_price_to_earnings(self.share_price, self.predicted_earings_per_share)
        self.trailing_price_to_earnings = trailing_price_to_earnings(self.share_price, self.earnings_per_share_12m)
        self.price_earnings_to_growth = price_earnings_to_growth(self.share_price, self.earnings_per_share,
                                                                 self.annual_eps_growth)
        self.price_to_sales = price_to_sales(self.share_price, self.income_per_share)
        self.price_to_book = price_to_book(self.share_price, self.book_value_share)
        self.return_on_assets = return_on_assets(self.net_income, self.total_assets)
        self.return_on_equity = return_on_equity(self.net_income, self.shareholder_equity)


def market_cap(share_price, outstanding_shares):
    try:
        mc = share_price * outstanding_shares
    except:
        pass
    return mc


def enterprice_value(market_cap, total_debt, cash, cash_equivalents):
    try:
        ev = (market_cap + total_debt) - (cash + cash_equivalents)
    except:
        pass
    return ev


def price_to_earnings(share_price, earnings_per_share):
    pe = share_price / earnings_per_share
    return pe


def forward_price_to_earnings(share_price, predicted_earnings_per_share):
    fpe = share_price / predicted_earnings_per_share
    return fpe


def trailing_price_to_earnings(share_price, earnings_per_share_12m):
    tpe = share_price / earnings_per_share_12m
    return tpe


def price_earnings_to_growth(share_price, earnings_per_share, annual_eps_growth):
    pe = price_to_earnings(share_price, earnings_per_share)
    peg = pe / annual_eps_growth
    return peg


def price_to_sales(share_price, income_per_share):
    pts = share_price / income_per_share
    return pts


def price_to_book(share_price, book_value_share):
    pb = share_price / book_value_share
    return pb


def return_on_assets(net_income, total_assets):
    roa = net_income / total_assets
    return roa


def return_on_equity(net_income, shareholder_equity):
    roe = net_income / shareholder_equity
    return roe

# payout ratio / dividend
# liquidity ratios ( quick/current/cash ratio)
