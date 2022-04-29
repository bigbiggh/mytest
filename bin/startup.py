# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/3/28 17:22
# @Author   :Sailheader
# @File :startup.py
# @Description:脚本执行的入口
# ------------------------------
'''
    脚本执行的入口：
    pytest.main(['.case','-v'])   运行case目录下的用例
    pytest.main(['.test_**py','-v'])   运行test_**.py用例
    pytest.main(['./test_**.py::Test**'])   运行模块中的指定用例，例如：运行test_summary.py里面的TestSummary
    pytest.main(['./test_**.py::Test**::test_01'])   运行类中的指定用例，例如：运行test_summary.py里面的TestSummary类的test_01
    pytest.main(['-k','king','-v'])   匹配包含king的用例(匹配目录名、模块名、类名、用例名)
    pytest.main(['-k','king','./test_**.py','-v'])   匹配test_summary.py模块下包含king的用例


    怎样选择用例，指定路径后，pytest会自动搜索目录下所有符合命名规则的方法作为一条测试用例来执行，当然也可以指定具体某一条或者指定执行顺序
            ['../case/test_warehouse.py::Test_warehouse::test_Complete_process',

'''
import datetime
import pytest

# todo：1、部分模块缺少断言；2、计划将完整流程分开、改为小模块组合成完整流程；改成小模块之后组合大模块方式执行测试用例时，可适当增加脚本运行时延以及按小模块增加断言，出现问题方便精确定位具体模块;.
# todo：3、按业务分
# todo：2、脚本上库；集成上jenkins

if __name__ == '__main__':
    pytest.main(
        ['../case/Huada/test_material',
         '--html=../report/logs/{}_{}.html'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), "test"),
         '--self-contained-html',
         '-v', '-s'])
    # pytest.main(["-s", "--alluredir={}".format(log_path), "../case/test_warehouse.py"])
    # os.system("allure generate {} -o {}/html".format(log_path,log_path))

    # os.system("allure serve {} -o {}/html".format(log_path,log_path))
