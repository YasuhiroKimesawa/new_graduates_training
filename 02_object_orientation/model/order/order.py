# -*- coding:utf-8 -*-
from decimal import Decimal

from model.order.order_goods_cs import OrderGoodsCSList
from model.order.order_price import OrderPrice


class OrderId:
    def __init__(self, value: int):
        self.value = value


class Order:
    def __init__(self,
                 order_id: OrderId,
                 order_goods_cs_list: OrderGoodsCSList,
                 order_price: OrderPrice):
        self.order_id = order_id
        self.order_goods_cs_list = order_goods_cs_list
        self.order_price = order_price

    def subtotal_without_tax(self) -> Decimal:
        return self.order_goods_cs_list.subtotal_without_tax()

    def tax(self) -> Decimal:
        return self.order_price.tax(self.subtotal_without_tax())

    def total(self) -> Decimal:
        return self.order_price.total(self.subtotal_without_tax())

    @staticmethod
    def create(order_dictionary: dict) -> 'Order':
        order_id = order_dictionary["order_id"]
        order_goods_cs_list = OrderGoodsCSList.create(order_dictionary["order_goods_cs_list"])
        order_price = OrderPrice.create(order_dictionary["use_point"])

        return Order(
            order_id,
            order_goods_cs_list,
            order_price
        )