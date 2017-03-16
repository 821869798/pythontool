import urllib
import http.cookiejar
import re
import time
from email.mime.text import MIMEText
from email.header import Header
import datetime
import smtplib

igxe_url = 'http://www.igxe.cn/search?search_page_no=1&search_relate_price=&search_product_type_id=&search_category_id=&search_sort_key=0&search_sort_rule=1&search_is_sticker=0&search_key=&search_price_gte=100.0&search_price_lte=300.0&search_rarity_id=&search_exterior_id=&search_is_stattrak=0&search_type=730'

def send_mail(title):
    msg = MIMEText(str(datetime.datetime.now())+'\n'+igxe_url, 'plain', 'utf-8')
    msg['Subject'] = Header(title, 'utf-8')
    msg['From'] = 'qq821869798@163.com'
    msg['To'] = "821869798@qq.com" 
    server = smtplib.SMTP("smtp.163.com", 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login("qq821869798@163.com", "bfo87081856O")
    server.sendmail("qq821869798@163.com", ["821869798@qq.com"], msg.as_string())
    server.quit()
    server.close()

if __name__ == "__main__":
    file_in = open("logs.txt",'a',encoding='utf-8')
    request = urllib.request.Request(igxe_url)
    while True:
        response = urllib.request.urlopen(request) 
        text = response.read().decode('utf-8', 'ignore')

        myre = re.compile(r"比例: (.*?)\n",re.S)
        text = myre.findall(text)
        for bili in text:
            bili = float(bili)
            if bili <= 0.75:
                date = str(datetime.datetime.now())
                send_mail("IGXE有"+str(bili)+"比例了"+ date)
                file_in.write("比例:"+str(bili)+" "+date + "\n")
                file_in.close()
                quit()
        time.sleep(10)
