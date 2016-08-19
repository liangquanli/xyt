# !/usr/bin/env python
# encoding: utf-8
from core.db.base_model import BaseModel, EmbeddedModel, EmbeddedModelField
from core.db.fields import *


class DeliveryOrder(EmbeddedModel):
    receivable_num = IntField()  # 回款量
    receivable_order_id = IntField()   # 出库单号


class ProductList(EmbeddedModel):
    product_key = IntField()
    product_name = StringField()   # 商品名
    order_list = ListField(field=EmbeddedModelField(base_document=DeliveryOrder))


class BusinessDeliveryOrderInfo(BaseModel):
    """
    产品出库单明细信息
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "business_delivery_order_info"
        }
    }

    business_id = IntField()  # 商户ID
    receivable_id = IntField(primary_key=True)    # 商户回款ID
    receivable_date = StringField()  # 回款日期  字符串
    receivable_date_stamp = TimeField()   # 回款日期  时间戳
    create_date = TimeField()     # 创建(更新)时间
    receivable_money = FloatField()    # 回款额
    certificate_img_name = StringField()    # 凭证
    sale_id = IntField()
    product_list = ListField(field=EmbeddedModelField(base_document=ProductList))
