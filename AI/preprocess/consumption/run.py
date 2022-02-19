# %%
import pandas as pd

from preprocess.consumption import weather_asos
from preprocess.consumption import user_consumption

# %%


def run(BASEDIR_PATH: str) -> pd.DataFrame:

    x = weather_asos.run(BASEDIR_PATH)  # ASOS
    y = user_consumption.run(BASEDIR_PATH)    # entire consumption

    dataset = x.copy()
    dataset[['전력사용량']] = y[['전기']]

    return dataset

# %%

# test


# run("../../data/")
