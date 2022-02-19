# %%
import pandas as pd

import asos
import consumption

# %%


def run(BASEDIR_PATH: str) -> pd.DataFrame:

    x = asos.run(BASEDIR_PATH)  # ASOS
    y = consumption.run(BASEDIR_PATH)    # entire consumption
    print(x.shape, type(x), y.shape, type(y))

    dataset = x.copy()
    dataset[['전기']] = y[['전기']]

    return dataset

# %%

# test


run("../../data/")
