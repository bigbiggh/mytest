import time
# x = time.time()
# time.sleep(1)
# y = time.time()
# print(y-x)
# import time
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# from AutoTestProject.script.login import Login
# from selenium import webdriver
#
# from AutoTestProject.tools.Common import common
#
# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=option)
# driver.maximize_window()
# driver.get('http://192.168.1.203')
# driver.implicitly_wait(5)
# driver.find_element(By.NAME, "userName").send_keys("admin")
# driver.find_element(By.NAME, "password").send_keys("123")
# driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
# driver.find_element(By.XPATH, "//p[contains(.,\'生产管理\')]").click()
# driver.find_element(By.XPATH, "//div[@id=\'PRODUCE_MGT\']/ul/li[4]/a").click()
# driver.find_element(By.XPATH,
#                     "/html/body/ngb-modal-window/div/div/stationsettingmodal/div[2]/div/div/form/div[1]/div/select/option[2]").click()
# driver.find_element(By.XPATH,
#                     "/html/body/ngb-modal-window/div/div/stationsettingmodal/div[2]/div/div/form/div[2]/div/select/option[2]").click()
# driver.find_element(By.XPATH,
#                     "/html/body/ngb-modal-window/div/div/stationsettingmodal/div[2]/div/div/form/div[3]/div/select/option[2]").click()
# driver.find_element(By.XPATH,
#                     "/html/body/ngb-modal-window/div/div/stationsettingmodal/div[2]/div/div/form/div[4]/button").click()
# driver.find_element(By.NAME, "workOrderNo").send_keys("22-A-03-072")
# driver.find_element(By.NAME, "workOrderNo").send_keys(Keys.ENTER)
# driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(8) > .item-info").click()
# driver.find_element(By.NAME, "packId").send_keys("1904047637/1910092218Q0160S000153")
# driver.find_element(By.NAME, "packId").send_keys(Keys.ENTER)
# list1 = []
# list2 = []
# x = 100
#
# for i in range(200):
#     x = x + 1
#     chanpinbianma = "1904047637/1910092218S000{}".format(str(x))
#     print(chanpinbianma)
#     tim1 = time.time()
#     common.send_input(driver.find_element(By.NAME, "productSerialNo"), chanpinbianma)
#     driver.find_element(By.NAME, "productSerialNo").send_keys(Keys.ENTER)
#     driver.implicitly_wait(5)
#     # driver.find_element(By.NAME, "productSerialNo").send_keys(chanpinbianma)
#     msg = driver.find_element(By.XPATH, '//*[@id="mCSB_2_container"]/p').text
#     print(msg)
#     list1.append(msg)
#     tim2 = time.time()
#     list2.append(tim2 - tim1)
#
# print(list1)
# print(list2)
