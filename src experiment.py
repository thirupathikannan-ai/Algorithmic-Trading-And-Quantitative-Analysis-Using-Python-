import pandas as pd
import matplotlib.pyplot as plt

from .data import download_data, prepare_data
from .indicators import calculate_indicators
from .strategies import (
    moving_average_strategy,
    momentum_strategy,
    mean_reversion_strategy,
)
from .backtest import backtest
from .metrics import calculate_metrics


def run_experiment(
    symbol="SPY",
    start="2018-01-01",
    end="2026-01-01"
):
    data = download_data(
        symbol=symbol,
        start=start,
        end=end
    )

    data = prepare_data(data)

    data = calculate_indicators(data)

    strategies = {
        "Moving Average": moving_average_strategy(data),
        "Momentum": momentum_strategy(data),
        "Mean Reversion": mean_reversion_strategy(data),
    }

    performance = {}

    backtests = {}

    for name, signal in strategies.items():

        result = backtest(
            data["Return"],
            signal
        )

        backtests[name] = result

        performance[name] = calculate_metrics(
            result["NetReturn"]
        )

    performance = pd.DataFrame(performance).T

    best_strategy = performance[
        "Sharpe Ratio"
    ].idxmax()

    return {
        "data": data,
        "backtests": backtests,
        "performance": performance,
        "best_strategy": best_strategy,
    }


def make_plots(results):

    for name, result in results["backtests"].items():

        plt.figure(figsize=(10, 5))

        plt.plot(
            result.index,
            result["Equity"],
            label=name
        )

        plt.title(
            f"{name} Strategy Equity Curve"
        )

        plt.xlabel("Date")
        plt.ylabel("Equity")

        plt.legend()
        plt.grid(True)

        plt.tight_layout()

        plt.show()
