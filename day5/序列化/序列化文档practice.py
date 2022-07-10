__author__ = 'Administrator'


# import json
# dic = {'lizexiong': 'lizexiong1234'}
# with open('StoreUserDB', 'a', encoding='utf-8') as f:
#     json.dump(dic, f)
#     f.flush()
# with open('StoreUserDB', 'r', encoding='utf-8') as f1:
#     d = json.load(f1)
#     print(d)



# import json
# dic = {'lizexiong': 'lizexiong1234'}
# with open('StoreUserDB', 'a', encoding='utf-8') as f:
#     for i in range(3):
#         json.dump(dic, f)
#         f.write('\n')
#         f.flush()
# with open('StoreUserDB', 'r', encoding='utf-8') as f1:
#     for j in f1:
#         print(json.loads(j), type(json.loads(j)))    # 这里我们是对字符串操作，而不是文件，所以需要使用loads而不是load


import pickle
lst = [1, 2, 3, 4, 5]
for i in range(3):
    lst.append(i)
    with open('test', 'ab') as f:    # pickle写入的是字节，所以需要使用带b的方法
        pickle.dump(lst, f)
        f.flush()

with open('test', 'rb') as f1:
    for i in range(3):
        a = pickle.load(f1)
        print(a)
