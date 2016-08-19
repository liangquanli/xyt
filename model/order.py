#!/usr/bin/env python
# encoding: utf-8
from core.db.fields import *
from core.db.base_model import BaseModel
from model.embedded.area import Area
from model.embedded.item import Item
from model.embedded.consignee_order import ConsigneeOrder


class Order(BaseModel):
    """
    订单,订单管理里面的订单
    """

    _schema = {
        'mongo': {
            "database": "sales_tools",
            "collection": "order"
        }
    }

    ds_id = IntField()  # 药店id
    ds_name = StringField()  # 药店名字
    actor_id = IntField()  # 业务员id
    actor_display_name = StringField()  # 业务员显示名字

    order_state = IntField()  # 订单状态

    urgent_state = IntField()  # 加急状态
    order_id = IntField(primary_key=True)  # 订单id
    order_number = IntField()  # 订单编号
    area = EmbeddedModelField(base_document=Area)  # 地区信息
    items = ListField(field=EmbeddedModelField(base_document=Item))  # 商品
    consignees = EmbeddedModelField(base_document=ConsigneeOrder)  # 收货信息
    consignee_id = IntField()  # 收货地址id
    create_time = DateTimeField()  # 订单创建时间
    finish_time = TimeField(default=0)  # 订单完成时间

    messages = StringField()  # 备注信息
    reissue_messages = StringField()  # 补发备注信息
    advise_messages = StringField()  # 建议信息
    return_messages = StringField()  # 退货原因

    total_price = FloatField()  # 产品总价格
    total_product_amount = IntField()  # 产品总数量

    shipping_price = IntField()  # 运费
    shipping_status = IntField()  # 物流状态
    shipping_number = StringField()  # 物流单号

    total_price_coupon = IntField()  # 总优惠金额
    total_discount = FloatField()  # 总折扣

    payment_status = IntField()  # 支付状态

    system_discount = FloatField(default=0)  # 总价折扣

    canceled_time = DateTimeField()  # 取消时间
    free_items = EmbeddedModelField(base_document=Item)  # 赠送礼品

    combination_status = IntField()  # 组合状态

    verified_time = DateTimeField()  # 审核通过时间
    return_goods_verified_time = DateTimeField()  # 退货审核通过时间

    is_verified = BooleanField()  # 是否审核通过
    is_sign_in = BooleanField(default=False)

    again_order_id = IntField(default=0)  # 补发订单id
    old_order_id = IntField(default=0)  # 补发的新订单里面对老订单的管理
    old_order_number = IntField(default=0)  # 补发的新订单里面对老订单的管理

    again_order_number = IntField(default=0)  # 补发订单号
