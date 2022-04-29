# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/24 17:53
# @Author   :Administrator
# @File :Sc_material.py
# @Description:
# ------------------------------
from selenium.webdriver.common.by import By
from AutoTestProject.tools.Common import *
import time


@common.decoratore
class Sc_material:
    def __init__(self, driver):
        self.driver = driver
        self.log = get_logger()

    def add_material(self, test_data):
        """mes添加物料"""

        self.log.info('添加物料数据')
        self.driver.find_element(By.XPATH, "//p[contains(.,\'物料配置\')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(@href, \'#/materialconfig/partmaster-manage\')]").click()
        self.driver.find_element(By.XPATH, "//div/div/div/button[2]").click()
        common.send_input(self.driver.find_element(By.XPATH, '//*[@id="materialInfoModal"]/div/div/div[2]/form/fieldset/div/dynamic-form[1]/div[1]/div/div/div/input'),test_data['wlbm'])
        common.send_input(self.driver.find_element(By.XPATH, '//*[@id="materialInfoModal"]/div/div/div[2]/form/fieldset/div/dynamic-form[1]/div[2]/div/div/div/input'),test_data['wlmc'])
        common.send_input(self.driver.find_element(By.XPATH, '//*[@id="materialInfoModal"]/div/div/div[2]/form/fieldset/div/dynamic-form[1]/div[3]/div/div/div/input'),test_data['wlfl'])
        dropdown = self.driver.find_element(By.CSS_SELECTOR, ".custom-drop-down")
        dropdown.find_element(By.XPATH, "//option[. = '原材料']").click()
        self.driver.find_element(By.XPATH, "//option[@value=\'MATERIAL\']").click()
        self.driver.find_element(By.XPATH, "(//button[@type=\'submit\'])[2]").click()
        msg = self.driver.find_element(By.XPATH,
                                       "/html/body/app-my-app/app-layout/div/div[2]/div/partmaster-manage/div/div[1]/div/div/div/div/div/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div[1]/div[1]").text
        return msg


    def del_material_01(self,test_data):

        self.add_material(test_data)
        # self.driver.find_element(By.XPATH, "//p[contains(.,\'物料配置\')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id=\'MATERIEL_MGT\']/ul/li/a").click()
        common.send_input(self.driver.find_element(By.NAME, "md_part_master.partNo"),test_data['wlbm'])
        self.driver.find_element(By.CSS_SELECTOR, ".btn-md:nth-child(1) .material-icons").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '/html/body/app-my-app/app-layout/div/div[2]/div/partmaster-manage/div/div[1]/div/div/div/div/div/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div/div[1]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        self.driver.find_element(By.LINK_TEXT, "确认").click()
        common.send_input(self.driver.find_element(By.NAME, "md_part_master.partNo"),test_data['wlbm'])
        self.driver.find_element(By.CSS_SELECTOR, ".btn-md:nth-child(1) .material-icons").click()
        self.log.info('删除未审核的物料数据pass')
        msg = self.driver.find_element(By.XPATH, '//*[@id="borderLayout_eGridPanel"]/div[2]/div/div/ng-component/p').text
        return msg


    def del_material_02(self,test_data):

        self.add_material(test_data)

        common.send_input(self.driver.find_element(By.NAME, "md_part_master.partNo"),test_data['wlbm'])
        self.driver.find_element(By.CSS_SELECTOR, ".btn-md:nth-child(1) > .btn-label").click()
        self.driver.find_element(By.XPATH, '/html/body/app-my-app/app-layout/div/div[2]/div/partmaster-manage/div/div[1]/div/div/div/div/div/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div/div[1]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
        self.driver.find_element(By.LINK_TEXT, "合格").click()

        if self.driver.find_element(By.XPATH,'//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div[1]/div[9]/span/span').text == "合格":
            print('物料数据审批合格完成')

        # self.driver.find_element(By.XPATH, "//p[contains(.,\'物料配置\')]").click()
        # self.driver.find_element(By.XPATH, "//div[@id=\'MATERIEL_MGT\']/ul/li/a").click()
        common.send_input(self.driver.find_element(By.NAME, "md_part_master.partNo"),test_data['wlbm'])
        self.driver.find_element(By.CSS_SELECTOR, ".btn-md:nth-child(1) .material-icons").click()
        self.driver.implicitly_wait(5)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[1]').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "确认").click()
        time.sleep(3)
        common.send_input(self.driver.find_element(By.NAME, "md_part_master.partNo"),test_data['wlbm'])
        self.driver.find_element(By.CSS_SELECTOR, ".btn-md:nth-child(1) .material-icons").click()
        self.log.info('删除已审核的物料数据')
        msg = self.driver.find_element(By.XPATH, '/html/body/app-my-app/app-layout/div/div[2]/div/partmaster-manage/div/div[1]/div/div/div/div/div/ag-grid-angular/div/div[2]/div[2]/div/div[1]/div/div[4]/div[3]/div/div/div[1]/div[1]').text
        self.log.info(msg)
        return msg

    def query_material(self):
        pass
    def modify_material(self):
        pass