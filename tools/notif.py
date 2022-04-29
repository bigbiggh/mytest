# -----------------------------
# -*- coding:utf-8-*-
# @Time     :2022/4/19 14:10
# @Author   :Administrator
# @File :notif.py
# @Description:
# ------------------------------
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from AutoTestProject.tools.readconfig import ReadConfig


class Email:
    @classmethod
    def send_email(cls):

        message = MIMEMultipart()

        send_email_data = ReadConfig.read_configAsjson('../config/config.json')
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        rep_list = sorted(os.listdir("../report/logs"),reverse = True)
        report_html_path = '../report/logs/{}'.format(rep_list[0])
        report_allure_path = '../report/logs/{}/html/index.html'.format(rep_list[0])
        msg = MIMEText(open(report_html_path, 'rb').read(), 'base64','utf-8')
        print(report_html_path)
        msg['Content-Type'] = 'application/octet-stream'
        msg['Content-Disposition'] = 'attachment;filename="{}"'.format(rep_list[0])

        message['Subject'] = "title"
        message['From'] = send_email_data['EMAIL_INFO']['sender']
        message['To'] = send_email_data['EMAIL_INFO']['receivers'][0]

        # 设置html格式参数
        # part1 = MIMEText(content, 'html', 'utf-8')
        # 接受方信息
        message.attach(msg)

        # try:
            # 连接服务器
        smtpObj = smtplib.SMTP_SSL(send_email_data['EMAIL_INFO']['host'], 465)
        # 登录到服务器
        smtpObj.login(send_email_data['EMAIL_INFO']['mail_user'], send_email_data['EMAIL_INFO']['mail_pass'])
        # 发送
        smtpObj.sendmail(send_email_data['EMAIL_INFO']['sender'], send_email_data['EMAIL_INFO']['receivers'],
                         message.as_string())
        # 退出
        smtpObj.quit()
        print('send success')
        #     return True
        # except smtplib.SMTPException as e:
        #     print('error', e)  # 打印错误
        #     return False


