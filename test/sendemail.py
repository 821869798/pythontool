from email.mime.text import MIMEText
from email.header import Header
import smtplib
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['Subject'] = Header('测试啊啊啊啊啊啊+++++++', 'utf-8')
msg['From'] = 'qq821869798@163.com'
msg['To'] = "821869798@qq.com" 

server = smtplib.SMTP("smtp.163.com", 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login("qq821869798@163.com", "xxxxx") #发送者邮箱账号密码
server.sendmail("qq821869798@163.com", ["821869798@qq.com"], msg.as_string())
server.quit()