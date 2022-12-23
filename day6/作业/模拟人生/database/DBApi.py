




import json
from conf import setting
from module.common import write_file


def AppendDB(contant,filename):
    """
    将信息以 json 格式写入数据表文件(追加)
    :return:
    """
    try:
        with open(filename,'r+') as f:
            f.write(json.dumps(contant))
            f.write("\n")
    except Exception as e:
        write_file(e, 'error', setting.LOG_PATH + "/sql.log")

#从指定数据库文件中读取数据
def LoadDataFromDB(tablename):
    """
    从指定数据库文件中获取所有数据,通过json方式返回
    :param tablename: 数据库文件名
    :return: 返回数据库文件信息
    """
    try:
        with open(tablename,"r+") as f:
            return json.load(f)
    except Exception as e:
        write_file(e, 'error', setting.LOG_PATH + "/sql.log")

#从指定数据库修改数据
def ModifyDB(name,key,value,filename):
    """
    修改数据库用户的属性值
    :param name: 修改的名字
    :param value:  修改的值
    :return:
    """
    try:
        with open(filename,"r+") as r:
            ALlInfo = json.load(r)
    except Exception as e:
        write_file(e, 'error', setting.LOG_PATH + "/sql.log")

    try:
        with open(filename,"w+") as w:
            ALlInfo[name][key] = value
            w.write(json.dumps(ALlInfo))
    except Exception as e:
        write_file(e, 'error', setting.LOG_PATH + "/sql.log")
