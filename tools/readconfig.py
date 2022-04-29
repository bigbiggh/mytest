# -----------------------------
'''
-*- coding:utf-8-*-
@Time     :2022/4/6 13:41
@Author   :Sailheader
@File :readconfig.py
@Description:读取config.py文件内容
'''


# ------------------------------
class ReadConfig:
    @classmethod
    def read_configAsjson(cls, path):
        import json
        with open(path, encoding='utf8') as file:
            data = json.load(file)
        return data
