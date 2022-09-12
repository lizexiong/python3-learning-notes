




import pickle






name = ["lizexiong", "rain", "test"]

t1 = "123"
t2 = "456"

f = open("pickle_test.txt","wb")
pickle.dump(name,f)     #第一次dump
pickle.dump(t1,f)     #第二次dump
pickle.dump(t2,f)     #第三次dump
f.close()