# -*- coding:utf-8 -*-
from decimal import Decimal
from typing import List


class GoodsId:
    def __init__(self, value: int):
        self.value = value


class GoodsName:
    def __init__(self, value: str):
        self.value = value

    def as_text(self) -> str:
        return self.value


class Color:
    def __init__(self, value: str):
        self.value = value

    def as_text(self) -> str:
        return self.value


class PriceWithoutTax:
    def __init__(self, value: Decimal):
        self.value = value

    def as_text(self) -> str:
        return str(self.value)


class OrderGoodsCS:
    def __init__(self,
                 goods_id: GoodsId,
                 goods_name: GoodsName,
                 color: Color,
                 price_without_tax: PriceWithoutTax):
        self.goods_id = goods_id
        self.goods_name = goods_name
        self.color = color
        self.price_without_tax = price_without_tax

    def as_text(self):
        # TODO 個数と税抜金額を追加する
        return "{} / {}".format(self.goods_name.as_text(), self.color.as_text())

    @staticmethod
    def create(cs_dictionary: dict) -> 'OrderGoodsCS':

        goods_id = GoodsId(cs_dictionary["goods_id"])
        goods_name = GoodsName(cs_dictionary["goods_name"])
        color = Color(cs_dictionary["color"])
        price_without_tax = PriceWithoutTax(cs_dictionary["price_without_tax"])

        return OrderGoodsCS(goods_id, goods_name, color, price_without_tax)


class OrderGoodsCSList:
    def __init__(self, values: List[OrderGoodsCS]):
        self.values = values

    def subtotal_without_tax(self) -> Decimal:
        # TODO 集計
        pass

    def list_as_text(self) -> str:
        text = ""
        for order_goods_cs in self.values:
            text = "{}{}\n".format(text, order_goods_cs.as_text())

        return text

    @staticmethod
    def create(cs_list_dictionary: dict) -> 'OrderGoodsCSList':

        cs_list = []
        for cs_dictionary in cs_list_dictionary:
            cs_list.append(OrderGoodsCS.create(cs_dictionary))

        return OrderGoodsCSList(cs_list)