




import pickle
f = open("pickle_test.txt","rb")
a = pickle.load(f)
print (a)

b = pickle.load(f)
print (b)

c = pickle.load(f)
print (c)