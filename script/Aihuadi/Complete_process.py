# -----------------------------
# '''
# -*- coding:utf-8-*-
# @Time     :2022/3/26 17:46
# @Author   :Sailheader
# @File :Complete_process.py
# @Description:
# '''
# ------------------------------
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from AutoTestProject.script.login import Login
from AutoTestProject.tools.Common import *
import time

element_bztm = ''


@common.decoratore
class Complete_process:
    def __init__(self, driver):
        self.driver = driver
        self.log = get_logger()

    def add_material(self, test_data):
        """mes添加物料"""

        self.log.info('添加物料数据')
        self.driver.find_element(By.CSS_SELECTOR, ".collapse-list:nth-child(5) p").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#MATERIEL_MGT .collapse-list:nth-child(1) .sidebar-normal").click()
        self.driver.find_element(By.CSS_SELECTOR, ".active > .sidebar-normal")

        self.driver.find_element(By.CSS_SELECTOR, ".active > .sidebar-normal")

        self.driver.find_element(By.CSS_SELECTOR, ".btn-success:nth-child(2) .test_material-icons")

        self.driver.find_element(By.CSS_SELECTOR, ".btn-success:nth-child(2) .test_material-icons").click()

        self.driver.find_element(By.NAME, "partNo").send_keys(test_data['wlbm'])
        self.driver.find_element(By.NAME, "zhCnName").send_keys(test_data['wlmc'])
        self.driver.find_element(By.NAME, "partSpecifications").send_keys(test_data['wlxh'])
        self.driver.find_element(By.CSS_SELECTOR, ".ng-dirty > .text-right > .btn-primary").click()
        msg = self.driver.find_element(By.XPATH,
                                       "/html/body/app-my-app/app-layout/div/div[2]/div/partmaster-manage/div/div[1]/div/div/div/div/div/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div[1]/div[1]").text
        return msg

    def add_PurchaseOrder(self, test_data):
        """mes新建采购单"""
        self.log.info('添加采购单')
        self.driver.find_element(By.ID, "search-input").send_keys("采购单")
        self.driver.find_element(By.LINK_TEXT, "采购单管理").click()
        self.log.info('点击添加采购单')
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > app-my-app > app-layout > div > div.main-panel > div > purchaseorder > div.main-content > div > div > div > div > div > div > button:nth-child(2) > span > i").click()

        self.driver.find_element(By.CSS_SELECTOR, ".input-group-addon:nth-child(2)").click()
        self.log.info('输入供应商名称搜索---输入：供应商名称')
        element = self.driver.find_element(By.XPATH,
                                           "/html/body/ngb-modal-window/div/div/common-modal-template/div[2]/form/div[1]/dynamic-form/div[2]/div/div/div/input")
        common.send_input(element, test_data['gys_name'])

        element = self.driver.find_element(By.XPATH,
                                           "/html/body/ngb-modal-window/div/div/common-modal-template/div[2]/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div[1]/div[1]")
        common.double_click(self.driver, element)

        self.log.info('点击添加物料')
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success:nth-child(1)").click()
        self.log.info('采购单管理-选择物料-根据物料编码查询---输入：物料编码')
        element = self.driver.find_element(By.XPATH,
                                           '/html/body/ngb-modal-window/div/div/multiple-modal-template/div[2]/div[1]/div[1]/form/div[1]/dynamic-form/div[2]/div/div/div/input')
        common.send_input(element, test_data['wlbm'])

        self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted > .row .btn-info").click()

        element = self.driver.find_element(By.XPATH,
                                           '/html/body/ngb-modal-window/div/div/multiple-modal-template/div[2]/div[2]/div[1]/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div[1]/div[1]')
        common.double_click(self.driver, element)

        self.log.info('点击提交')
        self.driver.find_element(By.CSS_SELECTOR, ".ng-untouched > .btn-primary").click()
        self.log.info('双击输入应收数量')
        element = self.driver.find_element(By.XPATH,
                                           "/html/body/app-my-app/app-layout/div/div[2]/div/purchaseorder/div[3]/div/div/div[2]/form/fieldset/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div/div[6]")
        common.double_click(self.driver, element)
        element = self.driver.find_element(By.CSS_SELECTOR, '.ag-cell-focus > input:nth-child(1)')
        common.send_input(element, '100')

        self.driver.find_element(By.XPATH,
                                 "/html/body/app-my-app/app-layout/div/div[2]/div/purchaseorder/div[3]/div/div/div[2]/form/fieldset/div[3]/button[2]").click()

    def Receipt_PurchaseOrder(self, test_data):
        """mes有采购单收货"""
        self.log.info("有采购单收货-根据物料编码搜索采购订单---输入物料编码")
        element = self.driver.find_element(By.ID, "search-input")
        common.send_input(element, "采购单")
        self.driver.find_element(By.LINK_TEXT, "有采购单收货").click()
        self.driver.find_element(By.XPATH, "/html/body/app-my-app/app-layout/div/div[2]/div/in-coming-purchase/div/div/div/div[2]/div[1]/div[1]/form/div[1]/div/span").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "div.form-horizontal:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys(
            test_data['wlbm'])

        self.driver.find_element(By.CSS_SELECTOR, "button.btn-info:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "ag-grid-angular.ag-theme-test_material:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
        common.double_click(self.driver, element)

        self.driver.find_element(By.CSS_SELECTOR,
                                 "div.col-lg-3:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys(
            test_data['wlbm'])
        self.driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "div.ag-cell-value:nth-child(1)").click()
        self.driver.find_element(By.NAME, "receiveQuantity").send_keys("10")
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-my-app/app-layout/div/div[2]/div/in-coming-purchase/div/div/div/div[2]/div[1]/div[1]/form/div[10]/div/input").send_keys(
            "10")
        self.driver.find_element(By.CSS_SELECTOR, "#submitBtn")

    def check_MaterialReceiptReport(self, test_data):
        '''mes查看料品数据'''
        element = self.driver.find_element(By.ID, "search-input")
        common.send_input(element, "收料报表")
        # self.driver.find_element(By.CSS_SELECTOR, ".text").click()
        self.driver.find_element(By.CSS_SELECTOR, "#searchMenu > li:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           'div.col-lg-2:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
        common.send_input(element, test_data['wlbm'])
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn-md:nth-child(1)').click()
        self.driver.find_element(By.XPATH, '/html/body/app-my-app/app-layout/div/div[2]/div/receivingorder/div[1]/div/div/div/div/div/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div[1]/div[1]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn-success:nth-child(2)').click()
        time.sleep(3)

        element = common.get_api_res('GET',
                                     'http://192.168.1.235/mes/cloud/v1/module/warehouse/api/part/recived/7039/part/stock/main')
        global element_bztm
        element_bztm = element['data'][0]['packId']

        self.driver.find_element(By.CSS_SELECTOR, ".close > span").click()
        # todo:根据什么来查看收料报表，物料编码+采购单号？

    def MesApp_do_Warehousing(self):
        """
            进入MESapp，做入库操作
        """
        self.log.info("-----MESAPP")
        Login(self.driver).do_login_APP()
        self.driver.find_element(By.CSS_SELECTOR, "div.aui-col-xs-3:nth-child(5) > div:nth-child(1)").click()
        element = self.driver.find_element(By.XPATH,
                                           "/html/body/app-my-app/app-layout/div/batch-pkg-instore/div[1]/form/ul/li[1]/div/div[2]/input")
        common.send_input(element, "9527")
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "li.aui-list-item:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
        common.send_input(element, element_bztm)
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "li.aui-list-item:nth-child(8) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
        common.send_input(element, "10")
        self.driver.find_element(By.CSS_SELECTOR, "button.aui-btn").click()
        self.log.info("-----MESAPP----\nAPP收料包装条码为%s" % element_bztm)
