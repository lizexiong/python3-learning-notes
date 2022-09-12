import shelve

d = shelve.open('shelve_test')  # 打开一个文件


class Test(object):
    def __init__(self, n):
        self.n = n


t1 = Test(123)
t2 = Test(456)

name = ["lizexiong", "rain", "test"]
d["test"] = name  # 持久化列表
d["t1"] = t1  # 持久化类
d["t2"] = t2

d.close()