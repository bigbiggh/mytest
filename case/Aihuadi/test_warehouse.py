# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/3/28 11:10
# @Author   :Sailheader
# @File :test_warehouse.py
# ------------------------------
"""
    @Description:脚本运行以及断言
    调用xlsx模块测试数据
    断言：1、判断接口返回值
        2、判断数据库返回值
        3、判断UI返回值
"""

import pytest

from AutoTestProject.script.Aihuadi.Complete_process import Complete_process
from AutoTestProject.tools.Common import common


class Test_warehouse:
    """
        test_info0 = common.get_dataForsheet('TestData.xlsx', 0, 1)
        get_dataForsheet(a,b,c),a为测试数据文件名称；b测试数据sheet页，0为第一页；c测试数据行数，表头下第一行为1
    """
    test_info2 = common.get_dataForsheet('TestData.xlsx', 0, 3)

    @pytest.mark.parametrize("test_data", test_info2)
    def test_Complete_process(self, driver, test_data):
        res_add_material = Complete_process(driver=driver).add_material(test_data)
        assert test_data['wlxh'] in res_add_material, 'mes添加物料失败'
        res_add_PurchaseOrder = Complete_process(driver=driver).add_PurchaseOrder(test_data)

        # except Exception:
        #     print(traceback.print_exc())

    @pytest.mark.parametrize("test_data", test_info2)
    def test_Complete_process2(self, driver, test_data):
        Complete_process(driver=driver).Receipt_PurchaseOrder(test_data)
        Complete_process(driver=driver).check_MaterialReceiptReport(test_data)
        # with allure.step("mesapp入库"):
        #     Complete_process(driver=driver).MesApp_do_Warehousing()
