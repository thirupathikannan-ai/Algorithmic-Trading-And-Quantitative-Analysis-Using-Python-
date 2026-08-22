import pandas as pd


def backtest(
    returns,
    signal,
    transaction_cost=0.0005
):
    result = pd.DataFrame(index=returns.index)

    result["MarketReturn"] = returns

    result["Signal"] = signal

    # Trade using the signal available before the next return.
    result["Position"] = result["Signal"].shift(1).fillna(0)

    result["GrossReturn"] = (
        result["Position"] * result["MarketReturn"]
    )

    result["Turnover"] = (
        result["Position"]
        .diff()
        .abs()
        .fillna(0)
    )

    result["TransactionCost"] = (
        transaction_cost * result["Turnover"]
    )

    result["NetReturn"] = (
        result["GrossReturn"]
        - result["TransactionCost"]
    )

    result["Equity"] = (
        1 + result["NetReturn"]
    ).cumprod()

    return result
