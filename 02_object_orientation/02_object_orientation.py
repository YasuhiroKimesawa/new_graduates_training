# -*- coding:utf-8 -*-
from decimal import Decimal

from model.order.order import Order


def get_input_order_dictionary() -> dict:
    return {
        "order_id": 1,
        "order_goods_cs_list": [
            {
                "goods_id": 31837681,
                "goods_name": "MILANO LIB ノースリーブニットプルオーバー【ウォッシャブル】",
                "color": "ベージュ",
                "price_without_tax": Decimal(10000)
            },
            {
                "goods_id": 30960300,
                "goods_name": "FLORAL PRINT DRESS フラワープリントワンピース",
                "color": "ターコイズブルー",
                "price_without_tax": Decimal(15000)
            }],
        "use_point": 3000
    }


if __name__ == '__main__':

    # 注文
    order_dictionary: dict = get_input_order_dictionary()
    # Order作成
    order: Order = Order.create(order_dictionary)

    # 表のタイトルを出力
    print("商品名 / 色 / 個数 / 税抜金額")
    # 商品情報を出力
    print(order.order_goods_cs_list.list_as_text())
    # 出力
    print("税抜小計: ¥{:,}".format(order.subtotal_without_tax()))
    # TODO 税・使用ポイント・合計金額を出力

