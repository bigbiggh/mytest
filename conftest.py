# -----------------------------
# '''
# -*- coding:utf-8-*-
# @Time     :2022/3/29 11:56
# @Author   :Sailheader
# @File :conftest.py.py
# @Description:
# '''


# ------------------------------
import datetime
import pytest
from selenium import webdriver
from py.xml import html
from AutoTestProject.script.login import Login
from AutoTestProject.tools.db import DB
from AutoTestProject.tools.notif import Email
from AutoTestProject.tools.readconfig import ReadConfig

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """当测试失败的时候，自动截图，展示到html报告中"""
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'οnclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

"""
@pytest.fixture()
如果不写参数，默认就是scope="function"，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例运行之后运行。
fixture为class级别的时候，如果一个class里面有多个用例，都调用了此fixture，那么此fixture只在该class里所有用例开始前执行一次
fixture为module级别时，在当前.py脚本里面所有用例开始前只执行一次
fixture为session级别是可以跨.py模块调用的,也就是当我们有多个.py文件的用例时候，如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里

conftest.py文件名称是固定的，pytest会自动识别该文件。放到工程的根目录下，就可以全局调用了，如果放到某个package包下，那就只在该package内有效
"""



@pytest.fixture(scope='session')
def driver():
    print('------------open browser------------')
    driver = webdriver.Chrome()
    driver.maximize_window()
    Login(driver).do_login()
    yield driver

    # 发送邮件

    if ReadConfig.read_configAsjson('../config/config.json')['Is_send_Email'] == "True":
        Email.send_email()
    else:
        pass

    print('------------close browser------------')
    driver.quit()




@pytest.mark.optionalhook
def pytest_html_report_title(report):
    """更改报告名称"""
    report.title = '{}_{}.html'.format((datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')), "test")

# @pytest.mark.optionalhook
# def pytest_configure(config):
#     # config._metadata.clear()
#     config.metadata['Project Name'] = '192.168.1.235'


def pytest_html_results_summary(prefix):
    # prefix.clear() # 清空summary中的内容
    prefix.extend([html.p("所属部门: 赛瀚德测试部")])
    prefix.extend([html.p("Module Name: 仓库模块")])
    prefix.extend([html.p("测试执行人: 郭辉")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))  # 添加描述列（Description）
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))  # 添加可排序时间（Time）列
    cells.pop()  # 删除链接（Link）列


@pytest.mark.optionalhook
def pytest_html_results_table_row(cells):
    # cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.datetime.now(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
