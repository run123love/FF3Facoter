# -*- coding:utf-8 -*-
from .mytypings import DataFrame, pd


def get_head_and_tail(df: DataFrame, n: int = 5):
    return pd.concat([df.head(n), df.tail(n)])
