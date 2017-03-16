import json
f = open('test/test.level','r',encoding='utf-8')
strs = f.read()
f.close()
level = json.loads(strs)["level_data"]
print(level)
strs = "GG思密达"
b = bytes(level)
print(b)
print(list(b))