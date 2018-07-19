# -*- coding:utf-8 -*-
from decimal import Decimal


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
    order: dict = get_input_order_dictionary()

    # 他にもこんなタスクが・・・
    # DBに永続化
    # 決済代行(クレジットなど)への通知

    # 消費税
    tax_rate: Decimal = Decimal(8)

    # 表のタイトルを出力
    print("商品名 / 色 / 個数 / 税抜金額")

    # 商品情報を出力
    for order_goods_cs in order["order_goods_cs_list"]:
        # TODO 個数と税抜金額を追加する
        print("{} / {}".format(order_goods_cs["goods_name"], order_goods_cs["color"]))

    # 税抜きの小計金額を集計
    # TODO 集計
    subtotal_without_tax = 0

    # 税を計算(今回は四捨五入しなくていい)
    # TODO 計算
    tax = 0

    # 税込小計金額
    # TODO 計算
    subtotal_with_tax = 0

    # 使用ポイント
    use_point = int(order["use_point"])

    # 合計金額を計算(使用ポイントが税込合計金額以上であれば0円)
    # TODO 計算
    total = 0
    if use_point >= subtotal_with_tax:
        pass

    # 出力
    print("税抜小計: ¥{:,}".format(subtotal_without_tax))
    # TODO 税・使用ポイント・合計金額を出力

