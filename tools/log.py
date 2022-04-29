# -----------------------------
'''
-*- coding:utf-8-*-
@Time     :2022/4/6 9:31
@Author   :Sailheader
@File :log.py
@Description:
'''
# ------------------------------
import os
import time
import logging
import sys, datetime
from logging import handlers

log_dir1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), r"report\logs")
today = time.strftime('%Y%m%d', time.localtime(time.time()))
full_path = os.path.join(log_dir1, today)
log_name = "{}_{}".format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), "test")
# if not os.path.exists(full_path):
#     os.makedirs(full_path)
log_path = os.path.join(log_dir1, log_name)


def get_logger():
    # 获取logger实例，如果参数为空则返回root logger
    logger = logging.getLogger("{}_{}".format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), "test"))
    if not logger.handlers:
        # 指定logger输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

        # # 文件日志
        # file_handler = handlers.TimedRotatingFileHandler(log_path, encoding="utf8")
        # file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

        # 控制台日志
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter  # 也可以直接给formatter赋值

        # 为logger添加的日志处理器
        # logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        # 指定日志的最低输出级别，默认为WARN级别
        logger.setLevel(logging.DEBUG)
    # 添加下面一句，在记录日志之后移除句柄
    return logger
