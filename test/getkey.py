import re
f = open("keys.txt",'r')
src = f.read()
f.close()
des = re.findall(r'\w{5}-\w{5}-\w{5}',src,re.M)
out = open("asf.txt",'w')
if len(des) > 0:
    out.write(des[0])
    for i in range(1,len(des)):
        out.write(','+des[i])
out.close()