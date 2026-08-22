import numpy as np


def annualized_return(returns):
    returns = returns.dropna()

    if len(returns) == 0:
        return 0.0

    return (1 + returns).prod() ** (
        252 / len(returns)
    ) - 1


def annualized_volatility(returns):
    return returns.std() * np.sqrt(252)


def sharpe_ratio(returns):
    volatility = annualized_volatility(returns)

    if volatility == 0 or np.isnan(volatility):
        return 0.0

    return (
        returns.mean() * 252
    ) / volatility


def sortino_ratio(returns):
    downside = returns[returns < 0].std()

    if downside == 0 or np.isnan(downside):
        return 0.0

    return (
        returns.mean() * 252
    ) / (downside * np.sqrt(252))


def maximum_drawdown(returns):
    equity = (1 + returns).cumprod()

    running_max = equity.cummax()

    drawdown = (
        equity / running_max
    ) - 1

    return drawdown.min()


def win_rate(returns):
    non_zero = returns[returns != 0]

    if len(non_zero) == 0:
        return 0.0

    return (non_zero > 0).mean()


def calculate_metrics(returns):
    return {
        "Annualized Return": annualized_return(returns),
        "Annualized Volatility": annualized_volatility(returns),
        "Sharpe Ratio": sharpe_ratio(returns),
        "Sortino Ratio": sortino_ratio(returns),
        "Maximum Drawdown": maximum_drawdown(returns),
        "Win Rate": win_rate(returns),
    }
