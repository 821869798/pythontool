from proto_out.test_pb2 import *
p = Person()
p.id = 1
p.name = '张三'
p.email = '123456@163.com'
a = p.SerializeToString()
p = Person()
p.ParseFromString(a)
print(p)