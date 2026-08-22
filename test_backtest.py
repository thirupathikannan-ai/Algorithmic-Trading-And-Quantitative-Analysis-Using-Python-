import pandas as pd

from src.backtest import backtest


def test_backtest():

    returns = pd.Series(
        [0.01, 0.02, -0.01]
    )

    signal = pd.Series(
        [1, 1, -1]
    )

    result = backtest(
        returns,
        signal,
        transaction_cost=0
    )

    assert "NetReturn" in result.columns
    assert "Equity" in result.columns
    assert len(result) == 3
