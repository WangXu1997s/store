import smtplib
#发送字符串的邮件
from email.mime.text import MIMEText
#处理多种形态的邮件主体我们需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart
#处理图片需要 MIMEImage 类
from email.mime.image import MIMEImage


from email.mime.application import MIMEApplication







# #设置服务器所需信息
# fromaddr = 'wangxu-1030@qq.com'#邮件发送方邮箱地址
# password = 'bdwrdnrfdfjubedg'#密码(部分邮箱为授权码)
# toaddrs = ['1620913558@qq.com']#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
#
#
#
#
# #设置email信息
# #---------------------------发送字符串的邮件-----------------------------
# #邮件内容设置
# message = MIMEText('hello,ziqiiii','plain','utf-8')
# #邮件主题
# message['Subject'] = 'ziqiiii test email'
# #发送方信息
# message['From'] = fromaddr
# #接受方信息
# message['To'] = toaddrs[0]
# #---------------------------------------------------------------------


# 登录并发送邮件
# try:
#     server = smtplib.SMTP("SMTP.qq.com")  # 163邮箱服务器地址，端口默认为25
#     server.login(fromaddr, password)
#     server.sendmail(fromaddr, toaddrs, message.as_string())
#     print('success')
#     server.quit()
#
# except smtplib.SMTPException as e:
#     print('error', e)  # 打印错误

if __name__ == '__main__':
    fromaddr = 'wangxu-1030@qq.com'
    password = 'bdwrdnrfdfjubedg'
    toaddrs = ['1620913558@qq.com']



    content = '你好这是我的测试报告'
    textApart = MIMEText(content)

    # imageFile = '1.png'
    # imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    # imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
    #
    # pdfFile = '算法设计与分析基础第3版PDF.pdf'
    # pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    # pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
    #
    # zipFile = '算法设计与分析基础第3版PDF.zip'
    # zipApart = MIMEApplication(open(zipFile, 'rb').read())
    # zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    htmlFile='计算器.html'
    htmlApart=MIMEText(open(htmlFile, 'rb').read(), _subtype='html', _charset='utf-8')
    htmlApart.add_header('content-Disposition','attachment',filename=htmlFile)

    m = MIMEMultipart()
    m.attach(textApart)
    # m.attach(imageApart)
    # m.attach(pdfApart)
    # m.attach(zipApart)
    m.attach(htmlApart)

    m['Subject']='测试报告'
    m['From'] = fromaddr
    # 接受方信息
    m['To'] = toaddrs[0]
    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误
