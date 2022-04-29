# -----------------------------
'''
-*- coding:utf-8-*-
@Time     :2022/3/26 17:03
@Author   :Sailheader
@File :login.py
@Description:
'''
# ------------------------------
from selenium.webdriver.common.by import By
from AutoTestProject.tools.readconfig import ReadConfig
from AutoTestProject.tools.Common import common
class Login:

    def __init__(self, driver):
        self.driver = driver

    def do_login(self):
        login_data = ReadConfig.read_configAsjson('../config/config.json')
        self.driver.get(login_data['login info']['url'])
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, "userName").send_keys(login_data['login info']['username'])
        self.driver.find_element(By.NAME, "password").send_keys(login_data['login info']['password'])
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
        # assert self.driver.find_element(By.LINK_TEXT, "系统功能")
        if common.is_element_present(self.driver,By.LINK_TEXT,"仪表板"):
            print("登录成功")
        else:
            print("登录失败")
    def do_login_APP(self):
        login_data = ReadConfig.read_configAsjson('../config/config.json')
        self.driver.get(login_data['login info']['url']+":81")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, "userName").send_keys(login_data['login info']['username'])
        self.driver.find_element(By.NAME, "password").send_keys(login_data['login info']['password'])
        self.driver.find_element(By.CSS_SELECTOR, "button.aui-btn").click()
    def exit_login(self):
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown:nth-child(4) > .dropdown-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "exit_to_app退出用户").click()


