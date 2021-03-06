import pandas as pd
from pandas import DataFrame


def capitalize_column_names(df: DataFrame) -> DataFrame:
    return df.rename(columns={key: key.capitalize() for key in df.columns})


def set_datetime_index(df: DataFrame) -> DataFrame:
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
    return df.set_index(['date'])


def format_df_backtest(df: DataFrame) -> DataFrame:
    df = set_datetime_index(df)
    df = df[['open', 'close', 'high', 'low', 'volume']]
    df = capitalize_column_names(df)
    return df
