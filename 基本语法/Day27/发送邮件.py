"""
发送邮件
@Date 2020.04.20
smtplib和email为python内置模块
"""
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
# 负责构造邮件头信息
from email.header import Header
# SMTP服务，这里使用QQ邮箱
mail_host = "smtp.qq.com"
# 发件人邮箱
mail_sender = "1836686674@qq.com"
# 邮箱授权码
mail_license = "xzmlvhvwppvgcigf"
# 收件人邮箱，可以为多个收件人
mail_receivers = ["1836686674@qq.com", "1401514686@qq.com"]
# 构建MIMEMultipart对象代表邮件本身，可以往里面添加文本，图片，附件等
mm = MIMEMultipart('related')
# 邮件主题
subject_content = """python邮件测试"""
# 设置发送者，注意格式，里面有邮箱为发件人邮箱
mm['From'] = "赵玉杰<1836686674@qq.com>"
# 设置接受者，注意格式，里面邮箱为接受者邮箱，可以设置多个
mm['To'] = "赵玉杰<1836686674@qq.com>,琪<1497636356@qq.com>"
# 设置邮件主题
mm['Subject'] = Header(subject_content, 'utf-8')
# 邮件正文内容
body_content = """hello,这是Python发出的邮件————赵玉杰"""
# 构造文本，参数1：正文内容，参数2：文本格式，参数3：编码方式
message_text = MIMEText(body_content, 'plain', 'utf-8')
# 想MIMEMultipart对象中添加文本对象
mm.attach(message_text)
# 构造附件
atta = MIMEText(open('./res/excel/excel_demo2.xlsx',
                     'rb').read(), 'base64', 'utf-8')
# 设置附件信息
atta["Content-Disposition"] = 'attachment;filename = "excel_demo2.xlsx"'
# 添加附件到邮件信息当中去
mm.attach(atta)
# 创建SMTP对象
stp = smtplib.SMTP()
# 设置房间人邮箱的域名和端口，端口地址为25
stp.connect(mail_host, 25)
# set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
stp.login(mail_sender, mail_license)
# 发送邮件，传递参数1：发送人邮箱地址，参数2：收件人邮箱地址
# 参数3：把邮件内容格式转成str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("邮件发送成功")
# 关闭SMTP对象
stp.quit()
