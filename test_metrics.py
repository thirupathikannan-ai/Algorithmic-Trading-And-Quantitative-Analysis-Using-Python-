import pandas as pd

from src.metrics import (
    annualized_volatility,
    maximum_drawdown,
    win_rate,
)


def test_volatility():
    returns = pd.Series(
        [0.01, -0.01, 0.02, -0.02]
    )

    result = annualized_volatility(returns)

    assert result > 0


def test_maximum_drawdown():
    returns = pd.Series(
        [0.10, -0.20, 0.05]
    )

    result = maximum_drawdown(returns)

    assert result < 0


def test_win_rate():
    returns = pd.Series(
        [0.01, -0.01, 0.02]
    )

    result = win_rate(returns)

    assert result == 2 / 3
