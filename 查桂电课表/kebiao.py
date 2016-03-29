# -*- coding: utf-8 -*-
import urllib
import http.cookiejar
import re

hosturl = "http://bkjw.guet.edu.cn/student/public/login.asp"
infourl = "http://bkjw.guet.edu.cn/student/Info.asp"
caselisturl = "http://bkjw.guet.edu.cn/student/selectterm.asp"
caseurl = "http://bkjw.guet.edu.cn/student/coursetable.asp"

cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)  
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)  
urllib.request.install_opener(opener)  
#先get访问获取cookie
h = urllib.request.urlopen(hosturl)  

headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    }

username = input("请输入账号：")
password = input("请输入密码：")
#封装post数据
postData = {
    "username" : username,
    "passwd" : password,
    "login" : "\u767b\u0020\u9646"
    }
#post发送账号密码并且带上cookie
postData = urllib.parse.urlencode(postData).encode('utf-8')  
request = urllib.request.Request(hosturl, postData,headers)  
response = urllib.request.urlopen(request) 
text = response.read().decode('gbk', 'ignore')
if re.findall("用户名或口令错",text):
    print("账号或密码错误")
    exit()

#登陆成功后，会带上cookie访问
#获取个人信息，入学年份
h = urllib.request.urlopen(infourl) 
text = h.read().decode('gbk', 'ignore')
grade = re.findall("年级:(.*?)</p>",text)[0]
grade = grade+"-"+str(int(grade)+1)+"_1"

#获取学期列表
h = urllib.request.urlopen(caselisturl)
text = h.read().decode('gbk', 'ignore')
myre = re.compile('<option value="(.*?)">')
templist = myre.findall(text)
gradelist = []
for i in templist:
    gradelist.append(i)
    if i == grade:
        break
print("请选择学期获取课表(输入对应得数字)")
for i in range(len(gradelist)):
    print(str(i)+":"+gradelist[i])
caseIndex = int(input("选择学期："))
if caseIndex<0 or caseIndex>=len(gradelist):
    print("输入错误")
    exit()

#post获取课表
caseData = {
    "term":gradelist[caseIndex]
    }
caseData = urllib.parse.urlencode(caseData).encode('utf-8')
request = urllib.request.Request(caseurl, caseData,headers)  
response = urllib.request.urlopen(request) 
text = response.read().decode('gbk', 'ignore') #得到所有课表的页面
#print(text)


#正则提取课表
myre1 = re.compile(r"星期日</th>\r\n  </tr>\r\n  (.*?)\r\n\r\n  <tr>\r\n    <th>备注</th>",re.S)
myre2 =re.compile("<td align='center'>(.*?)</td></tr>",re.M)
text = myre1.findall(text)[0]
text = myre2.findall(text) 
result = [[]*7 for row in range(5)]
#保存到文件
out = open("case.txt","w")
for i in range(len(text)):
    result[i] = re.split("</td><td align='center'>",text[i])
    out.write(result[i][0])
    for j in range(1,len(result[i])):
        out.write(" "+result[i][j])
    out.write("\n")
out.close()
print("已得到所有课表，在case.txt")