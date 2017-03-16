import pyDes
# f = open('test.txt','rb')
# f1 = open('out.txt','wb')
# # data = '123456@163.com'
k = pyDes.des("bfbf2333", pyDes.CBC, b"\x12\x34\x56\x78\x90\xAB\xCD\xEF", pad=None, padmode=pyDes.PAD_PKCS5)
# a = k.encrypt(f.read())
# f1.write(a)
# print ("Encrypted: %r" % a)

f = open('out.txt','rb')
a = k.decrypt(f.read())
print(a)