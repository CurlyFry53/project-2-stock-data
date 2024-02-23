import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

'''
# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:
# - Fidelity ZERO Large Cap Index: FNILX
fnilx = yf.Ticker("FNLIX")
# get all stock info
fnilx.info
# get historical market data
hist = fnilx.history(period="1mo")
# show meta information about the history (requires history() to be called first)
fnilx.history_metadata
# show actions (dividends, splits, capital gains)
fnilx.actions
fnilx.dividends
fnilx.splits
fnilx.capital_gains  # only for mutual funds & etfs
# show share count
fnilx.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
fnilx.income_stmt
fnilx.quarterly_income_stmt
# - balance sheet
fnilx.balance_sheet
fnilx.quarterly_balance_sheet
# - cash flow statement
fnilx.cashflow
fnilx.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
fnilx.major_holders
fnilx.institutional_holders
fnilx.mutualfund_holders
fnilx.insider_transactions
fnilx.insider_purchases
fnilx.insider_roster_holders
# show recommendations
fnilx.recommendations
fnilx.recommendations_summary
fnilx.upgrades_downgrades
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use fnilx.get_earnings_dates(limit=XX) with increased limit argument.
fnilx.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
fnilx.isin
# show options expirations
fnilx.options
# show news
fnilx.news
# get option chain for specific expiration
opt = fnilx.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts
'''
# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:

import yfinance as yf

voo = yf.Ticker("VOO")
# get all stock info
voo.info
# get historical market data
hist = voo.history(period="1mo")
# show meta information about the history (requires history() to be called first)
voo.history_metadata
# show actions (dividends, splits, capital gains)
voo.actions
voo.dividends
voo.splits
voo.capital_gains  # only for mutual funds & etfs
# show share count
voo.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
voo.income_stmt
voo.quarterly_income_stmt
# - balance sheet
voo.balance_sheet
voo.quarterly_balance_sheet
# - cash flow statement
voo.cashflow
voo.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
voo.major_holders
voo.institutional_holders
voo.mutualfund_holders
voo.insider_transactions
voo.insider_purchases
voo.insider_roster_holders
# show recommendations
voo.recommendations
voo.recommendations_summary
voo.upgrades_downgrades
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use voo.get_earnings_dates(limit=XX) with increased limit argument.
voo.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
voo.isin
# show options expirations
voo.options
# show news
voo.news
# get option chain for specific expiration
opt = voo.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts

# SPDR S&P 500 ETF : SPY
# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:

import yfinance as yf

spy = yf.Ticker("SPY")
# get all stock info
spy.info
# get historical market data
hist = spy.history(period="1mo")
# show meta information about the history (requires history() to be called first)
spy.history_metadata
# show actions (dividends, splits, capital gains)
spy.actions
spy.dividends
spy.splits
spy.capital_gains  # only for mutual funds & etfs
# show share count
spy.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
spy.income_stmt
spy.quarterly_income_stmt
# - balance sheet
spy.balance_sheet
spy.quarterly_balance_sheet
# - cash flow statement
spy.cashflow
spy.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
spy.major_holders
spy.institutional_holders
spy.mutualfund_holders
spy.insider_transactions
spy.insider_purchases
spy.insider_roster_holders
# show recommendations
spy.recommendations
spy.recommendations_summary
spy.upgrades_downgrades
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use spy.get_earnings_dates(limit=XX) with increased limit argument.
spy.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
spy.isin
# show options expirations
spy.options
# show news
spy.news
# get option chain for specific expiration
opt = spy.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts
 
# iShares Core S&P 500 ETF: IVV
# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:
ivv = yf.Ticker("IVV")
# get all stock info
ivv.info
# get historical market data
hist = ivv.history(period="1mo")
# show meta information about the history (requires history() to be called first)
ivv.history_metadata
# show actions (dividends, splits, capital gains)
ivv.actions
ivv.dividends
ivv.splits
ivv.capital_gains  # only for mutual funds & etfs
# show share count
ivv.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
ivv.income_stmt
ivv.quarterly_income_stmt
# - balance sheet
ivv.balance_sheet
ivv.quarterly_balance_sheet
# - cash flow statement
ivv.cashflow
ivv.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
ivv.major_holders
ivv.institutional_holders
ivv.mutualfund_holders
ivv.insider_transactions
ivv.insider_purchases
ivv.insider_roster_holders
# show recommendations
ivv.recommendations
ivv.recommendations_summary
ivv.upgrades_downgrades
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use ivv.get_earnings_dates(limit=XX) with increased limit argument.
ivv.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
ivv.isin
# show options expirations
ivv.options
# show news
ivv.news
# get option chain for specific expiration
opt = ivv.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts

#Schwab S&P Index Fund :SWPPX
# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:

import yfinance as yf

swppx = yf.Ticker("SWPPX")
# get all stock info
swppx.info
# get historical market data
hist = swppx.history(period="1mo")
# show meta information about the history (requires history() to be called first)
swppx.history_metadata
# show actions (dividends, splits, capital gains)
swppx.actions
swppx.dividends
swppx.splits
swppx.capital_gains  # only for mutual funds & etfs
# show share count
swppx.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
swppx.income_stmt
swppx.quarterly_income_stmt
# - balance sheet
swppx.balance_sheet
swppx.quarterly_balance_sheet
# - cash flow statement
swppx.cashflow
swppx.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
swppx.major_holders
swppx.institutional_holders
swppx.mutualfund_holders
swppx.insider_transactions
swppx.insider_purchases
swppx.insider_roster_holders
# show recommendations
swppx.recommendations
swppx.recommendations_summary
swppx.upgrades_downgrades
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use swppx.get_earnings_dates(limit=XX) with increased limit argument.
swppx.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
swppx.isin
# show options expirations
swppx.options
# show news
swppx.news
# get option chain for specific expiration
opt = swppx.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts

# Invesco QQQ Trust ETF: QQQ
# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:

qqq = yf.Ticker("QQQ")
# get all stock info
qqq.info
# get historical market data
hist = qqq.history(period="1mo")
# show meta information about the history (requires history() to be called first)
qqq.history_metadata
# show actions (dividends, splits, capital gains)
qqq.actions
qqq.dividends
qqq.splits
qqq.capital_gains  # only for mutual funds & etfs
# show share count
qqq.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
qqq.income_stmt
qqq.quarterly_income_stmt
# - balance sheet
qqq.balance_sheet
qqq.quarterly_balance_sheet
# - cash flow statement
qqq.cashflow
qqq.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
qqq.major_holders
qqq.institutional_holders
qqq.mutualfund_holders
qqq.insider_transactions
qqq.insider_purchases
qqq.insider_roster_holders
# show recommendations
qqq.recommendations
qqq.recommendations_summary
qqq.upgrades_downgrades
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use qqq.get_earnings_dates(limit=XX) with increased limit argument.
qqq.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
qqq.isin
# show options expirations
qqq.options
# show news
qqq.news
# get option chain for specific expiration
opt = qqq.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts

#Vanguard Russel 2000 ETF: VTWO
# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:

vtwo = yf.Ticker("VTWO")
# get all stock info
vtwo.info
# get historical market data
hist = vtwo.history(period="1mo")
# show meta information about the history (requires history() to be called first)
vtwo.history_metadata
# show actions (dividends, splits, capital gains)
vtwo.actions
vtwo.dividends
vtwo.splits
vtwo.capital_gains  # only for mutual funds & etfs
# show share count
vtwo.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
vtwo.income_stmt
vtwo.quarterly_income_stmt
# - balance sheet
vtwo.balance_sheet
vtwo.quarterly_balance_sheet
# - cash flow statement
vtwo.cashflow
vtwo.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
vtwo.major_holders
vtwo.institutional_holders
vtwo.mutualfund_holders
vtwo.insider_transactions
vtwo.insider_purchases
vtwo.insider_roster_holders
# show recommendations
vtwo.recommendations
vtwo.recommendations_summary
vtwo.upgrades_downgrades
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use vtwo.get_earnings_dates(limit=XX) with increased limit argument.
vtwo.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
vtwo.isin
# show options expirations
vtwo.options
# show news
vtwo.news
# get option chain for specific expiration
opt = vtwo.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts

#Vanguard Stock Market ETF :VTSAX

# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:

vtsax = yf.Ticker("VTSAX")
# get all stock info
vtsax.info
# get historical market data
hist = vtsax.history(period="1mo")
# show meta information about the history (requires history() to be called first)
vtsax.history_metadata
# show actions (dividends, splits, capital gains)
vtsax.actions
vtsax.dividends
vtsax.splits
vtsax.capital_gains  # only for mutual funds & etfs
# show share count
vtsax.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
vtsax.income_stmt
vtsax.quarterly_income_stmt
# - balance sheet
vtsax.balance_sheet
vtsax.quarterly_balance_sheet
# - cash flow statement
vtsax.cashflow
vtsax.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
vtsax.major_holders
vtsax.institutional_holders
vtsax.mutualfund_holders
vtsax.insider_transactions
vtsax.insider_purchases
vtsax.insider_roster_holders
# show recommendations
vtsax.recommendations
vtsax.recommendations_summary
vtsax.upgrades_downgrades
# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use vtsax.get_earnings_dates(limit=XX) with increased limit argument.
vtsax.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
vtsax.isin
# show options expirations
vtsax.options
# show news
vtsax.news
# get option chain for specific expiration
opt = vtsax.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts

# SPDR Dow Jones Industrial Average ETF Trust: DIA
# ticker module from the yahoo finance library documentation
# https://pypi.org/project/yfinance/ 
# The Ticker module, which allows you to access ticker data in a more Pythonic way:

dia = yf.Ticker("DIA")
# get all stock info
dia.info
# get historical market data
hist = dia.history(period="1mo")
# show meta information about the history (requires history() to be called first)
dia.history_metadata
# show actions (dividends, splits, capital gains)
dia.actions
dia.dividends
dia.splits
dia.capital_gains  # only for mutual funds & etfs
# show share count
dia.get_shares_full(start="2022-01-01", end=None)
# show financials:
# - income statement
dia.income_stmt
dia.quarterly_income_stmt
# - balance sheet
dia.balance_sheet
dia.quarterly_balance_sheet
# - cash flow statement
dia.cashflow
dia.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options
# show holders
dia.major_holders
dia.institutional_holders
dia.mutualfund_holders
dia.insider_transactions
dia.insider_purchases
dia.insider_roster_holders

# show recommendations
dia.recommendations
dia.recommendations_summary
dia.upgrades_downgrades

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use dia.get_earnings_dates(limit=XX) with increased limit argument.
dia.earnings_dates
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
dia.isin
# show options expirations
dia.options
# show news
dia.news
# get option chain for specific expiration
opt = dia.option_chain('2026-12-18')
# data available via: opt.calls, opt.puts