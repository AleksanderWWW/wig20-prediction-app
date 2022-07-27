import pandas as pd

from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame, test_size: float):
    idx = len(df) - int(len(df) * test_size)
    train_set = df.iloc[:idx]
    test_set = df.iloc[idx+1:]
    return train_set, test_set
