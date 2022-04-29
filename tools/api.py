# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/19 14:18
# @Author   :Administrator
# @File :api.py
# @Description:
# ------------------------------
import requests

from AutoTestProject.tools.Common import common
from AutoTestProject.tools.readconfig import ReadConfig


class API:
    @classmethod
    def get_token(cls):
        url = ReadConfig.read_configAsjson('../config/config.json')['login_api']
        headers = {}
        response = requests.request("POST", url, headers=headers)
        response_dict = eval(response.text)
        return response_dict['access_token']


    '''
    description:        get_api_res
                        获取对应接口messageCode;
    '''
    @classmethod
    def get_api_res(cls, func, url):
        API_info = {
            "headers":
                {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Authorization": "Bearer %s" % common.get_token(),
                    "Connection": "keep-alive",
                    "Content-Type": "application/json; charset=UTF-8"
                },
            "payload": "{\"exported\":false,\"paging\":{\"page\":1,\"size\":12,\"sortings\":[]}}"
        }
        response = requests.request(func, url=url, headers=API_info["headers"], data=API_info["payload"]).json()
        return response