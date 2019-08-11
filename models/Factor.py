# -*- coding:utf-8 -*-
from abc import abstractmethod, ABCMeta
import attr
from attr import attrs, attrib
from myhelpers.mytypings import _Number


@attrs
class FactorBase(metaclass=ABCMeta):
    """因子的基类"""
    name: str = attrib()
    value: _Number = attrib()
    @value.validator
    def within_zero_to_one(self, attribute, value_):
        if abs(value_) > 1:
            raise ValueError(f"the value of factor must be within -1 to 1.")
