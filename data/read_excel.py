# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         read_excel
# Author:       wjy
# Date:         2020/5/26
# Description:  读取excel文件内容
# -------------------------------------------------------------------------------
import xlrd, os
from AutoTestProject.tools.readconfig import ReadConfig

class ReadExcel:
    def __init__(self, filename):

        self.basepath = ReadConfig.read_configAsjson("../config/config.json")['test_data_path']
        self.filepath = os.path.join(self.basepath, filename)

    def read_excel(self, index):
        book = xlrd.open_workbook(self.filepath)
        # 读出具体页面
        sheet = book.sheet_by_index(index)
        return sheet
