#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/23 21:10
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : models.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm

import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Enum,
    DECIMAL,
    DateTime,
    Boolean,
    UniqueConstraint,
    Index
)
from sqlalchemy.ext.declarative import declarative_base

# 基础类
Base = declarative_base()


'''
echo=False -- 如果为真，引擎将记录所有语句以及 repr() 其参数列表的默认日志处理程序。
enable_from_linting -- 默认为True。如果发现给定的SELECT语句与将导致笛卡尔积的元素取消链接，则将发出警告。
encoding -- 默认为 utf-8
future -- 使用2.0样式
hide_parameters -- 布尔值，当设置为True时，SQL语句参数将不会显示在信息日志中，也不会格式化为 StatementError 对象。
listeners -- 一个或多个列表 PoolListener 将接收连接池事件的对象。
logging_name -- 字符串标识符，默认为对象id的十六进制字符串。
max_identifier_length -- 整数；重写方言确定的最大标识符长度。
max_overflow=10 -- 允许在连接池中“溢出”的连接数，即可以在池大小设置（默认为5）之上或之外打开的连接数。
pool_size=5 -- 在连接池中保持打开的连接数
plugins -- 要加载的插件名称的字符串列表。
'''
# 创建引擎
engine = create_engine(
    "mysql+pymysql://root:huawei@127.0.0.1:3306/lizexiong?charset=utf8mb4",
    # "mysql+pymysql://root@127.0.0.1:3306/lizexiong?charset=utf8mb4", # 无密码时

    # 超过链接池大小外最多创建的链接
    max_overflow=0,
    # 链接池大小
    pool_size=5,
    # 链接池中没有可用链接则最多等待的秒数，超过该秒数后报错
    pool_timeout=10,
    # 多久之后对链接池中的链接进行一次回收
    pool_recycle=1,
    # 查看原生语句（未格式化），如果为真，引擎将记录所有语句以及 repr() 其参数列表的默认日志处理程序。
    echo=True
)


# 绑定引擎
Session = sessionmaker(bind=engine)
# 创建数据库链接池，直接使用session即可为当前线程拿出一个链接对象conn
# 内部会采用threading.local进行隔离
session = scoped_session(Session)


class UserInfo(Base):
    """ 必须继承Base """
    # 数据库中存储的表名
    __tablename__ = "userInfo3"
    # 对于必须插入的字段，采用nullable=False进行约束，它相当于NOT NULL
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(32), index=True, nullable=False, comment="姓名")
    age = Column(Integer, nullable=False, comment="年龄")
    phone = Column(DECIMAL(6), nullable=False, unique=True, comment="手机号")
    address = Column(String(64), nullable=False, comment="地址")
    # 对于非必须插入的字段，不用采取nullable=False进行约束
    gender = Column(Enum("male", "female"), default="male", comment="性别")
    create_time = Column(
        DateTime, default=datetime.datetime.now, comment="创建时间")
    last_update_time = Column(
        DateTime, onupdate=datetime.datetime.now, comment="最后更新时间")
    delete_status = Column(Boolean(), default=False,
                           comment="是否删除")

    __table__args__ = (

        # UniqueConstraint("name", "age", "phone"),  # 联合唯一约束
        # Index("name", "addr", unique=True),       # 联合唯一索引
        Index("age", ),  # 联合唯一索引
    )

    def __str__(self):
        return f"object : <id:{self.id} name:{self.name}>"

    #执行的时候可以在终端看到返回的字段变量
    def __repr__(self):
        #return "执行的时候返回自定义字段测试"
        return f"object : <id:{self.id} name:{self.name}>"

if __name__ == "__main__":
    # 删除表
    Base.metadata.drop_all(engine)
    # 创建表
    Base.metadata.create_all(engine)
