# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/24 17:51
# @Author   :Administrator
# @File :test_material.py
# @Description:
# ------------------------------
import pytest
from AutoTestProject.script.Huada.material.Sc_material import Sc_material
from AutoTestProject.tools.Common import common
from AutoTestProject.tools.db import DB


class Test_material:
    # test_info = common.get_dataForsheet('测试用例.xlsx', 0, 3)
    #
    # @pytest.mark.parametrize("test_data", test_info)
    # def test_add_material(self, driver, test_data):
    #     query_sql = "SELECT count(*) FROM md_part_master"
    #     old_count = DB.query_one_forsql(query_sql)
    #     res_add_material = Sc_material(driver=driver).add_material(test_data)
    #     new_count = DB.query_one_forsql(query_sql)
    #     actual = 0
    #     assert test_data['wlbm'] == res_add_material, 'mes添加物料失败'
    #     actual += 1
    #     if new_count - old_count == 1:
    #         actual += 1
    #     assert actual == 2
    #
    # test_info2 = common.get_dataForsheet('测试用例.xlsx', 0, 4)
    # @pytest.mark.parametrize("test_data2", test_info2)
    # def test_del_material_01(self, driver, test_data2):
    #     # query_sql = "SELECT count(*) FROM md_part_master"
    #     res_del_material = Sc_material(driver=driver).del_material_01(test_data2)
    #     actual = 0
    #     if res_del_material == "没有搜索结果":
    #         actual += 1
    #     assert actual == 1
        # assert test_data2['wlbm'] in res_del_material, 'mes删除物料失败'

    test_info3 = common.get_dataForsheet('测试用例.xlsx', 0, 5)
    @pytest.mark.parametrize("test_data3", test_info3)
    def test_del_material_02(self, driver, test_data3):
        # query_sql = "SELECT count(*) FROM md_part_master"
        res_del_material = Sc_material(driver=driver).del_material_02(test_data3)
        # actual = 0
        # if res_del_material == test_data3['wlbm']:
        #     actual += 1
        # assert actual == 1
