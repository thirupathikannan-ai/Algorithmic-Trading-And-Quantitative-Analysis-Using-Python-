import numpy as np
import pandas as pd
import yfinance as yf


def download_data(
    symbol="SPY",
    start="2018-01-01",
    end="2026-01-01"
):
    data = yf.download(
        symbol,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        raise ValueError("No market data downloaded.")

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.dropna()

    return data


def prepare_data(data):
    data = data.copy()

    data["Return"] = data["Close"].pct_change()

    data["LogReturn"] = np.log(
        data["Close"] / data["Close"].shift(1)
    )

    data = data.dropna()

    return data
