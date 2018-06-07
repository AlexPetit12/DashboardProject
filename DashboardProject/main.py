import hdf5database
import yahoofinance

from constants import path_to_hdf_db


def update_data(symbols):
    yf = yahoofinance.YahooFinance()
    for symbol in symbols:
        df = yf.get_symbol_data(symbol)
        hdf5database.write_df_to_hdfstorage(df, path_to_hdf_db, symbol)


if __name__ == '__main__':
    symbols = ['FB', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    update_data(symbols)
