#!/usr/bin/env python
# encoding: utf-8

affairs = ['信息收集', '医生拜访', '商务-结款', '科室会议', '其他']

PLAN_STATUS_FINISH = 1
PLAN_STATUS_UN_FINISH = 0
PLAN_STATUS_REVOKE = 2

RIGHT_CONSULT_DAY_PLAN = int('0b1', 2)  # 查阅批示日总结
RIGHT_CONSULT_WEEKLY_PLAN = int('0b10', 2)  # 查阅批示周总结
RIGHT_SUMMARY_WEEKLY_PLAN = int('0b100', 2)  # 查看周汇总
RIGHT_CHECKS_INSTRUCTIONS = int('0b1000', 2)  # 查阅批示功能
RIGHT_SAVE_PROVINCE_CONSULT = int('0b10000', 2)  # 编写查看省经理批示
RIGHT_SAVE_DISTRICT_CONSULT = int('0b100000', 2)  # 编写查看大区经理批示

# 职位
POSITION_ADMIN = 0  # 系统管理员(h5端使用,仅用于开发)
POSITION_GENERAL_MANAGER = 1  # 总经理
POSITION_DISTRICT_MANAGER = 2  # 大区经理
POSITION_PROVINCE_MANAGER = 3  # 主管经理
POSITION_PROVINCE_SALES = 4  # 销售

USER_POSITION_FOR_ADMIN = {
    POSITION_ADMIN: "系统管理员",
    POSITION_GENERAL_MANAGER: "总经理",
    POSITION_DISTRICT_MANAGER: "大区经理",
    POSITION_PROVINCE_MANAGER: "主管经理",
    POSITION_PROVINCE_SALES: "销售"
}

USER_POSITION = {
    # POSITION_ADMIN: "系统管理员",
    POSITION_GENERAL_MANAGER: "总经理",
    POSITION_DISTRICT_MANAGER: "大区经理",
    POSITION_PROVINCE_MANAGER: "主管经理",
    POSITION_PROVINCE_SALES: "销售"
}

POSITION_RIGHT_TABLE = {
    POSITION_ADMIN: sum([RIGHT_CONSULT_DAY_PLAN, RIGHT_CONSULT_WEEKLY_PLAN,
                         RIGHT_SUMMARY_WEEKLY_PLAN, RIGHT_CHECKS_INSTRUCTIONS,
                         RIGHT_SAVE_PROVINCE_CONSULT, RIGHT_SAVE_DISTRICT_CONSULT]),
    POSITION_GENERAL_MANAGER: sum([RIGHT_CONSULT_DAY_PLAN, RIGHT_CONSULT_WEEKLY_PLAN,
                                   RIGHT_SUMMARY_WEEKLY_PLAN, RIGHT_CHECKS_INSTRUCTIONS,
                                   RIGHT_SAVE_PROVINCE_CONSULT, RIGHT_SAVE_DISTRICT_CONSULT]),
    POSITION_DISTRICT_MANAGER: sum([RIGHT_CONSULT_DAY_PLAN, RIGHT_CONSULT_WEEKLY_PLAN,
                                    RIGHT_SUMMARY_WEEKLY_PLAN,
                                    RIGHT_SAVE_PROVINCE_CONSULT, RIGHT_SAVE_DISTRICT_CONSULT]),
    POSITION_PROVINCE_MANAGER: sum([RIGHT_CONSULT_DAY_PLAN, RIGHT_CONSULT_WEEKLY_PLAN,
                                    RIGHT_SUMMARY_WEEKLY_PLAN, RIGHT_SAVE_PROVINCE_CONSULT])
}

# 中国大区
REGION_PARTITION_CHINA = {
    1: [],
    2: ["上海市", "江苏省", "浙江省", "黑龙江省", "内蒙古自治区", "辽宁省", "吉林省"],
    3: ["广东省", "广西壮族自治区", "海南省", "福建省"],
    4: [],
    5: ["山东省", "河北省", "天津市", "河南省", "北京市", "安徽省", "山西省"],
    6: [],
    7: [],
    8: ["测试省"]
}

PRODUCT_DICT = {
    1: '莱思纽卡菊C饮液',
    2: '莱思纽卡F26饮液',
    3: '莱思纽卡阳光饮液',
    4: '莱思纽卡C20饮液',
    5: '莱思纽卡Z30饮液',
    6: '莱思纽卡AD饮液',
    7: '莱思纽卡植物DHA饮液',
    8: '莱思纽卡孕妇多维饮液',
    9: '莱思纽卡孕妇DHA饮液',
    10: '莱思纽卡孕妇叶酸饮液'
}
PRODUCT_NUM = {
    1: 10,
    2: 11,
    3: 12,
    4: 13,
    5: 14,
    6: 15,
    7: 16,
    8: 17,
    9: 18,
    10: 19
}

PRODUCT_PRICE = {
    1: 298,
    2: 188,
    3: 188,
    4: 198,
    5: 188,
    6: 188,
    7: 358,
    8: 298,
    9: 358,
    10: 188
}
# 订单状态 状态
ORDER_STATE = ['已完成', '待审批', '已审批', '已完成', '退货', '补发', '已关闭']

# 订单状态 审核
ORDER_VERIFIED = [000000, 100000]
ORDER_VERIFIED_DICT = {
    000000: {'status': u'未审批', 'status2': 1},
    100000: {'status': u'未通过', 'status2': 1}
}
# 订单状态 出库
ORDER_WAREHOUSE = [200000, 210000]
ORDER_WAREHOUSE_DICT = {
    200000: {'status': u'待出库', 'status2': 2},
    210000: {'status': u'待收货', 'status2': 2}
}
# 订单状态 签收
ORDER_SIGN_IN = [211000]
ORDER_SIGN_IN_DICT = {
    211000: {'status': u'已收货', 'status2': 3}

}
# 订单状态 退货
ORDER_RETURN = [211100, 211200, 211300]
ORDER_RETURN_DICT = {
    211100: {'status': u'退货中', 'status2': 4},
    211200: {'status': u'退货完成', 'status2': 4},
    211300: {'status': u'已审核退货', 'status2': 4},
    211400: {'status': u'禁止退货', 'status2': 4}
}
# 订单状态 补货
ORDER_AGAIN = [211010, 211020, 211030]
ORDER_AGAIN_DICT = {
    211010: {'status': u'申请补货', 'status2': 5},
    211020: {'status': u'完成补货', 'status2': 5},
    211030: {'status': u'补货确认', 'status2': 5}
}
# 订单状态 关闭
ORDER_CLOSE = [000001, 100001, 200001, 210001, 211001, 211101, 211201, 211011, 211021]
ORDER_CLOSE_DICT = {
    000001: {'status': u'已关闭', 'status2': 6},
    100001: {'status': u'已关闭', 'status2': 6},
    200001: {'status': u'已关闭', 'status2': 6},
    210001: {'status': u'已关闭', 'status2': 6},
    211001: {'status': u'已收货之后的关闭', 'status2': 6},
    211101: {'status': u'关闭', 'status2': 6},
    211201: {'status': u'关闭', 'status2': 6},
    211011: {'status': u'关闭', 'status2': 6},
    211021: {'status': u'关闭', 'status2': 6}
}
# 订单状态 集合
ORDER_STATE_DICT = {}
ORDER_STATE_DICT.update(ORDER_VERIFIED_DICT)
ORDER_STATE_DICT.update(ORDER_WAREHOUSE_DICT)
ORDER_STATE_DICT.update(ORDER_SIGN_IN_DICT)
ORDER_STATE_DICT.update(ORDER_RETURN_DICT)
ORDER_STATE_DICT.update(ORDER_AGAIN_DICT)
ORDER_STATE_DICT.update(ORDER_CLOSE_DICT)

WAREHOUSE_VOLUME_DAY = 500
