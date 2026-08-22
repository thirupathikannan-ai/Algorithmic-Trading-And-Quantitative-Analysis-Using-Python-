import pandas as pd

from src.indicators import (
    moving_average,
    momentum,
    zscore,
)


def test_moving_average():
    series = pd.Series([1, 2, 3, 4, 5])

    result = moving_average(series, 3)

    assert result.iloc[-1] == 4


def test_momentum():
    series = pd.Series([100, 110])

    result = momentum(series, 1)

    assert round(result.iloc[-1], 5) == 0.10


def test_zscore():
    series = pd.Series(
        [1, 2, 3, 4, 5]
    )

    result = zscore(series, 3)

    assert not result.iloc[-1] != result.iloc[-1]
