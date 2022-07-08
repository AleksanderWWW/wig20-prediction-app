import pandas as pd

from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame, col: str, test_size: float = 0.3):
    sub_df = df[col]
    train_set, test_set = train_test_split(sub_df, test_size=test_size)
    return train_set, test_set
