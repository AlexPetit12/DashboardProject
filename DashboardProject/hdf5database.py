import pandas as pd


def write_df_to_hdfstorage(df, path_to_storage, group):
    hdf = pd.HDFStore(path_to_storage)
    hdf.put(group, df)
    hdf.close()


def read_df_from_hdfstorage(path_to_storage, group):
    return pd.read_hdf(path_to_storage, group)
