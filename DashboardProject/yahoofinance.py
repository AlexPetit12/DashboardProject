import io
import re
import requests

import pandas as pd


def get_symbol_data(symbol, start_date=(2000, 1, 1), end_date=None):
    assert end_date is None or \
           type(end_date) == tuple \
           and len(end_date) == 3 \
           and type(end_date[0]) == int \
           and type(end_date[1]) == int \
           and type(end_date[2]) == int

    if end_date is None:
        period2 = int(pd.datetime.today().timestamp())
    else:
        period2 = int(pd.datetime(*end_date).timestamp())

    period1 = int(pd.datetime(*start_date).timestamp())

    crumb, cookie = get_token()

    params = (symbol, period1, period2, crumb)

    url = "https://query1.finance.yahoo.com/v7/finance/download/" \
          "{0}?period1={1}&period2={2}&interval=1d&events=history&crumb={3}".format(*params)

    data = requests.get(url, cookies={'B': cookie})
    data.raise_for_status()

    buf = io.StringIO(data.text)
    df = pd.read_csv(buf, index_col=0, parse_dates=True, na_values=['null'])

    df.columns = map(str.lower, df.columns)

    return df.round(3)


def get_symbol_data_today(symbol):
    datetime_today = pd.datetime.today()
    today = (datetime_today.year, datetime_today.month, datetime_today.day)
    return get_symbol_data(symbol, start_date=today, end_date=today)


def get_token():
    url = 'https://uk.finance.yahoo.com/quote/AAPL/history'
    r = requests.get(url)

    html = r.text

    cookie = r.cookies['B']

    pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')

    for line in html.splitlines():
        m = pattern.match(line)
        if m is not None:
            crumb = m.groupdict()['crumb']

    assert r.status_code == 200

    return crumb, cookie
