Hard Exercise
===============

The goal of this exercise is to present a semi-real-world problem in which stock market quotes are retrieved from the yahoo finance service

## Intro ##

Yahoo Finance publishes a csv api of all the stock data. CSV stands for Comma Separated Values, and you won't need to know anything about the stock market for this. What CSV means is that I can organise columns separated by commas so:

      bill, 10, 20
      bob, 20, 10

Is 3 Values. Your job is to pull down:

- Stock Price
- Stock Exchange
- Market Cap

From the API for the stock you prompt for.

## Using the API ##

Normally, companies will publish a pretty API Doc of the API but yahoo isn't a normal company so for now, here's what people have found out about how it works:

    http://finance.yahoo.com/d/quotes.csv

is the base URL. Then, provide on the end:

    ?s=STOCK

Where STOCK is a Stock ticker (from finance.yahoo.com, check below for examples).

You can then provide 'format operators' to signal what data you want (here are the ones you want, don't worry about them):
    
    &f=pj1x

Will give:

     price, market cap, exchange, market cap

on just one line (if using one stock).

In full:

    http://finance.yahoo.com/d/quotes.csv?s=GOOG&f=pj1x

Will pull down the data for google. Note that not all of the fields need to be used later, this will give:

    677.14, 221.4B, "NasdaqNM"

(price: 677.14, exchange: Nasdaq, market cap: 221.4B)


## Example Stocks ##

Here's a list of a few stocks to try out (techy for the audience):

- GOOG (google)
- YHOO (yahoo)
- FB (facebook)
- AAPL (Apple)
- LNKD (LinkedIn)

## Example ##

   Stock: GOOG
   
   Price: 677.14
   Exchange: NasdaqNM
   Market Cap: 221.4B