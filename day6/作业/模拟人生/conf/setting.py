


import os,sys

#程序主目录文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#添加主目录到环境变量
sys.path.append(BASE_DIR)

#定义角色数据库信息
DATABASE = dict(engineer="file", dbpath=os.path.join(BASE_DIR, "database"), tables={"role" : "role",})

#角色初始体力值
vit = 5

#睡觉的状态
sleeping = 'False'

