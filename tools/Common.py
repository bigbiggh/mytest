import logging
import os

import requests, shutil

from AutoTestProject.tools.readconfig import ReadConfig
from functools import wraps
from AutoTestProject.tools.log import *
import traceback
from AutoTestProject.tools.log import get_logger
from selenium.webdriver.common.action_chains import ActionChains


class common:
    """
    description:打印错误日志
    """
    @classmethod
    def is_element_present(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    @classmethod
    def decoratore(cls, func):
        @wraps(func)
        def log(*args, **kwargs):
            try:
                print("当前运行用例", func.__name__)
                return func(*args, **kwargs)
            except Exception as e:
                get_logger().error(f"{func.__name__} is error,here are details:{traceback.format_exc()}")

        return log

    '''
    description: 输入(输入前先清空)
    '''

    @classmethod
    def send_input(cls, ele, value):
        ele.click()
        ele.clear()
        ele.send_keys(value)
        get_logger().info('输入%s' % value)

    @classmethod
    def double_click(cls, driver, ele):
        actions = ActionChains(driver)
        actions.double_click(ele).perform()

    '''
    description: 点击
    '''

    @classmethod
    def is_click(cls, ele):
        ele.click()
        get_logger().info('点击%s' % ele)

    '''
    description:    # 是判断元素否存在
    '''

    @classmethod
    def is_element_present(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    '''
    description:        get_random_num
                        # 生成随机数
    '''

    @classmethod
    def get_random_num(cls, start, end):
        import random
        return random.randint(start, end)

    '''
    description:        get_ctime
                        # 时间模块
    '''

    @classmethod
    def get_ctime(cls):
        import time
        time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())

    '''
    description:        get_dataForsheet
                         # 参数说明：testfile，文件路径，默认data目录下，只填文件名.xlsx;n：默认每次只取一行数据，n输入行数
    '''

    @classmethod
    def get_dataForsheet_old(cls, testfile, sheetNo, n):
        from AutoTestProject.data.read_excel import ReadExcel
        test_excel_sheet1 = ReadExcel(testfile).read_excel(index=sheetNo)
        rows = test_excel_sheet1.nrows
        cols = test_excel_sheet1.ncols
        list1 = []
        list2 = []
        for row in range(n, n + 1):
            for col in range(4, cols):
                ctype = test_excel_sheet1.cell(row, col).ctype
                cellData = test_excel_sheet1.cell_value(row, col)
                if ctype == 2 and cellData % 1 == 0.0:  # ctype为2且为浮点
                    cell = int(cellData)  # 浮点转成整型
                    list1.append(cell)
                list1.append(cellData)
        x = tuple(list1)
        list2.append(x)
        return list1

    '''
    description:        get_dataForsheet
                         # 参数说明：testfile，文件路径，默认data目录下，只填文件名.xlsx；n：默认每次只取一行数据，n输入行数
    '''
    @classmethod
    def get_dataForsheet(cls, testfile, sheetNo, n):
        from AutoTestProject.data.read_excel import ReadExcel
        test_excel_sheet1 = ReadExcel(testfile).read_excel(index=sheetNo)
        rows = test_excel_sheet1.nrows
        cols = test_excel_sheet1.ncols
        list1 = []
        for row in range(n, n + 1):
            for col in range(10, 11):
                ctype = test_excel_sheet1.cell(row, col).ctype
                cell = test_excel_sheet1.cell_value(row, col)
                cellData = eval(cell)
                list1.append(cellData)
        return list1

    '''
    description:        send_email
                        发送邮件;
    '''



    # '''
    # 参数化查询
    # #list参数化查询
    # #sql = "select * from pg_tables where schemaname=%s and tablename=%s"
    # #csor.execute(sql, ['internal_app_bsaata', 'event_ip_real'])
    # #dict参数化查询
    # sql = "select * from pg_tables where schemaname=%(db_name)s and tablename=%(tb_name)s"
    # csor.execute(sql, {'db_name':'internal_app_bsaata', 'tb_name':'event_ip_real'})
    #
    # ##多条数据处理
    # namedict = ({"first_name":"Joshua", "last_name":"Drake"},
    #             {"first_name":"Steven", "last_name":"Foo"},
    #             {"first_name":"David", "last_name":"Bar"})
    # cur = conn.cursor()
    # cur.executemany("""INSERT INTO bar(first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)
    # '''





