



# import yaml
# f = open(r'./config.yaml')
# #y = yaml.load(f)  #yaml5.1后废弃这种方法
# #下面三种方法都可以
# # y=yaml.load(f,Loader=yaml.FullLoader)
# # y=yaml.safe_load(f)
# y=yaml.load(f, Loader=yaml.CLoader)
# print (y)


# import yaml
# f = '''
# ---
# name: James
# age: 20
# ---
# name: Lily
# age: 19
# '''
# y = yaml.load_all(f,Loader=yaml.FullLoader)
# for data in y:
#     print(data)


# import yaml
# aproject = {'name': 'Silenthand Olleander',
#             'race': 'Human',
#             'traits': ['ONE_HAND', 'ONE_EYE']
#             }
#
# print(yaml.dump(aproject))

# import yaml
#
# aproject = {'name': 'Silenthand Olleander',
#             'race': 'Human',
#             'traits': ['ONE_HAND', 'ONE_EYE']
#             }
# f = open(r'./config2.yaml','w')
# print(yaml.dump(aproject,f))


import yaml

obj1 = {"name": "James", "age": 20}
obj2 = ["Lily", 19]

with open(r'./config3.yaml', 'w') as f:
    yaml.dump_all([obj1, obj2], f)