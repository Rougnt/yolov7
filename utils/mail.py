'''
Author: Rogunt abc847111391@hotmail.com
Date: 2022-09-09 10:25:47
LastEditors: Rogunt abc847111391@hotmail.com
LastEditTime: 2023-01-27 18:32:23
FilePath: /Python_test/mail.py
Description: 发送邮件，可以附加一个文件

Copyright (c) 2022 by Rogunt abc847111391@hotmail.com, All Rights Reserved. 
'''
# smtplib 用于邮件的发信动作
from base64 import encode
from email.mime.multipart import MIMEMultipart
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header
from email.headerregistry import Address

def sentEmain(mail_subject: str,content: str,file_name: str=None):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '221307040023@hhu.edu.cn'
    password = '26Ub*7o&an*B'
    # 收信方邮箱
    to_addr = 'abc847111391@hotmail.com'
    # 发信服务器
    smtp_server = 'smtphz.qiye.163.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEMultipart()
    # 邮件头信息
    msg['From'] = '魏子尊<221307040023@hhu.edu.cn>'
    msg['To'] = 'Ron Wei<abc847111391@hotmail.com'
    subject = '实验：'+mail_subject
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题
    msg.attach(MIMEText(content, 'plain', 'utf-8'))
    # 构造附件1，传送当前目录下的 test1.txt 文件
    if file_name:
        att1 = MIMEText(open('for.py', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="{}"'.format(file_name)
        msg.attach(att1)

    try:
        smtpobj = smtplib.SMTP_SSL(smtp_server)
        # 建立连接--qq邮箱服务和端口号（可百度查询）
        smtpobj.connect(smtp_server, 465)    
        # 登录--发送者账号和口令
        smtpobj.login(from_addr, password)   
        # 发送邮件
        smtpobj.sendmail(from_addr, to_addr, msg.as_string()) 
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")
    finally:
        # 关闭服务器
        smtpobj.quit()

if __name__== '__main__':
    sentEmain("实验：Python SMTP 邮件测试4","使用python发送邮件测试","for.py")
