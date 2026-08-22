import numpy as np
import pandas as pd


def rolling_sharpe(returns, window=60):
    mean = returns.rolling(window).mean()
    std = returns.rolling(window).std()

    return (
        mean / std.replace(0, np.nan)
    ) * np.sqrt(252)


def volatility_target_position(
    returns,
    target_volatility=0.10,
    window=20
):
    volatility = (
        returns.rolling(window).std()
        * np.sqrt(252)
    )

    position = (
        target_volatility
        / volatility.replace(0, np.nan)
    )

    return position.clip(
        lower=0,
        upper=1
    )


def drawdown_series(returns):
    equity = (1 + returns).cumprod()

    peak = equity.cummax()

    return equity / peak - 1
