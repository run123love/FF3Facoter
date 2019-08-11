# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import List
import attr
from attr import attrs, attrib
import pandas as pd


def calc_returns(prices: List[float]) -> float:
    ...


@attrs(frozen=True)
class Asset(metaclass=ABCMeta):
    """资产的基类 """
    name: str = attrib()
    prices: List[float] = attrib()
    returns: List[float] = attrib(factory=calc_returns)


