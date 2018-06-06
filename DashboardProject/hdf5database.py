import pandas as pd

from yahoofinance import get_symbol_data

symbol = 'SPY'
df = get_symbol_data(symbol)

path = '/home/alexpetit/Databases/ts_storage.h5'
group = symbol


def write_df_to_hdfstorage(df, path_to_storage, group):
    hdf = pd.HDFStore(path_to_storage)
    hdf.put(group, df)
    hdf.close()


def read_df_from_hdfstorage(path_to_storage, group):
    return pd.read_hdf(path_to_storage, group)


write_df_to_hdfstorage(df, path, group)
df = read_df_from_hdfstorage(path, group)
