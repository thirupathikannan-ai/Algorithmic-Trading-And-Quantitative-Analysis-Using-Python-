import numpy as np


def moving_average_strategy(data):
    signal = np.where(
        data["MA_Fast"] > data["MA_Slow"],
        1,
        -1
    )

    signal[
        data["MA_Fast"].isna()
        | data["MA_Slow"].isna()
    ] = 0

    return signal


def momentum_strategy(data):
    signal = np.where(
        data["Momentum"] > 0,
        1,
        -1
    )

    signal[
        data["Momentum"].isna()
    ] = 0

    return signal


def mean_reversion_strategy(
    data,
    entry_threshold=1.0
):
    signal = np.zeros(len(data))

    z = data["ZScore"].values

    signal[z < -entry_threshold] = 1
    signal[z > entry_threshold] = -1

    return signal
