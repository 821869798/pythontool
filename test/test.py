import json
import hashlib
f = open('test.level','r',encoding='utf-8')
strs = f.read()
f.close()
js = json.loads(strs)
level = js["level_data"]
print(level)
strs = "GG思密达"
b = bytes(level)
print(b)
print(list(b))
m2 = hashlib.md5()   
m2.update(b)
print(m2.hexdigest().upper())
print(js["level_id"])