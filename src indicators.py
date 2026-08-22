import numpy as np
import pandas as pd


def moving_average(series, window):
    return series.rolling(window).mean()


def momentum(series, lookback=20):
    return series.pct_change(lookback)


def rolling_volatility(returns, window=20):
    return returns.rolling(window).std() * np.sqrt(252)


def zscore(series, window=20):
    mean = series.rolling(window).mean()
    std = series.rolling(window).std()

    return (series - mean) / std.replace(0, np.nan)


def calculate_indicators(data):
    data = data.copy()

    data["MA_Fast"] = moving_average(
        data["Close"],
        20
    )

    data["MA_Slow"] = moving_average(
        data["Close"],
        50
    )

    data["Momentum"] = momentum(
        data["Close"],
        20
    )

    data["Volatility"] = rolling_volatility(
        data["Return"],
        20
    )

    data["ZScore"] = zscore(
        data["Close"],
        20
    )

    return data
