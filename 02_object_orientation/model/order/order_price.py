# -*- coding:utf-8 -*-
from decimal import Decimal


class TaxRate:
    def __init__(self):
        self.value = Decimal(8)


class UsePoint:
    def __init__(self, value: int):
        self.value = value


class OrderPrice:
    def __init__(self,
                 tax_rate: TaxRate,
                 use_point: UsePoint):
        self.tax_rate = tax_rate
        self.use_point = use_point

    def tax(self, subtotal: Decimal) -> Decimal:
        # TODO 計算
        return Decimal(0)

    def total(self, subtotal: Decimal) -> Decimal:
        # TODO 計算
        if self.use_point.value >= subtotal:
            pass

        return Decimal(0)

    @staticmethod
    def create(use_point: int) -> 'OrderPrice':
        return OrderPrice(
            TaxRate(),
            UsePoint(use_point)
        )