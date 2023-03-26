#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/3/24 14:34
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : models.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm




from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import relationship

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Date,
    String,
    Enum,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base

# 基础类
Base = declarative_base()

# 创建引擎
engine = create_engine(
    "mysql+pymysql://root:huawei@127.0.0.1:3306/lizexiong?charset=utf8mb4",
    # "mysql+pymysql://tom@127.0.0.1:3306/db1?charset=utf8mb4", # 无密码时
    # 超过链接池大小外最多创建的链接
    max_overflow=0,
    # 链接池大小
    pool_size=5,
    # 链接池中没有可用链接则最多等待的秒数，超过该秒数后报错
    pool_timeout=10,
    # 多久之后对链接池中的链接进行一次回收
    pool_recycle=1,
    # 查看原生语句
    # echo=True
)

# 绑定引擎
Session = sessionmaker(bind=engine)
# 创建数据库链接池，直接使用session即可为当前线程拿出一个链接对象
# 内部会采用threading.local进行隔离
session = scoped_session(Session)


class StudentsNumberInfo(Base):
    """学号表"""
    __tablename__ = "studentsNumberInfo"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    number = Column(Integer, nullable=False, unique=True, comment="学生编号")
    admission = Column(Date, nullable=False, comment="入学时间")
    graduation = Column(Date, nullable=False, comment="毕业时间")


class TeachersInfo(Base):
    """教师表"""
    __tablename__ = "teachersInfo"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    number = Column(Integer, nullable=False, unique=True, comment="教师编号")
    name = Column(String(64), nullable=False, comment="教师姓名")
    gender = Column(Enum("male", "female"), nullable=False, comment="教师性别")
    age = Column(Integer, nullable=False, comment="教师年龄")


class ClassesInfo(Base):
    """班级表"""
    __tablename__ = "classesInfo"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    number = Column(Integer, nullable=False, unique=True, comment="班级编号")
    name = Column(String(64), nullable=False, unique=True, comment="班级名称")
    # 一对一关系必须为连接表的连接字段创建UNIQUE的约束，这样才能是一对一，否则是一对多
    fk_teacher_id = Column(
        Integer,
        ForeignKey(
            "teachersInfo.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        unique=True,
        comment="班级负责人"
    )
    # 下面这2个均属于逻辑字段，适用于正反向查询。在使用ORM的时候，我们不必每次都进行JOIN查询，而恰好正反向的查询使用频率会更高
    # 这种逻辑字段不会在物理层面上创建，它只适用于查询，本身不占据任何数据库的空间
    # sqlalchemy的正反向概念与Django有所不同，Django是外键字段在那边，那边就作为正
    # 而sqlalchemy是relationship字段在那边，那边就作为正
    # 比如班级表拥有 relationship 字段，而老师表不曾拥有
    # 那么用班级表的这个relationship字段查老师时，就称为正向查询
    # 反之，如果用老师来查班级，就称为反向查询
    # 另外对于这个逻辑字段而言，根据不同的表关系，创建的位置也不一样：
    #  - 1 TO 1：建立在任意一方均可，查询频率高的一方最好
    #  - 1 TO M：建立在M的一方
    #  - M TO M：中间表中建立2个逻辑字段，这样任意一方都可以先反向，再正向拿到另一方
    #  - 遵循一个原则，ForeignKey建立在那个表上，那个表上就建立relationship
    #  - 有几个ForeignKey，就建立几个relationship
    # 总而言之，使用ORM与原生SQL最直观的区别就是正反向查询能带来更高的代码编写效率，也更加简单
    # 甚至我们可以不用外键约束，只创建这种逻辑字段，让表与表之间的耦合度更低，但是这样要避免脏数据的产生

    # 班级负责人，这里是一对一关系，一个班级只有一个负责人
    leader_teacher = relationship(
        # 正向查询时所链接的表，当使用 classesInfo.leader_teacher 时，它将自动指向fk的那一条记录
        "TeachersInfo",
        # 反向查询时所链接的表，当使用 teachersInfo.leader_class 时，它将自动指向该老师所管理的班级
        backref="leader_class",
    )


class ClassesAndTeachersRelationship(Base):
    """任教老师与班级的关系表"""
    __tablename__ = "classesAndTeachersRelationship"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    # 中间表中注意不要设置单列的UNIQUE约束，否则就会变为一对一
    fk_teacher_id = Column(
        Integer,
        ForeignKey(
            "teachersInfo.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        comment="教师记录"
    )

    fk_class_id = Column(
        Integer,
        ForeignKey(
            "classesInfo.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        comment="班级记录"
    )
    # 多对多关系的中间表必须使用联合唯一约束，防止出现重复数据
    __table_args__ = (
        UniqueConstraint("fk_teacher_id", "fk_class_id"),
    )

    # 逻辑字段
    # 给班级用的，查看所有任教老师
    mid_to_teacher = relationship(
        "TeachersInfo",
        backref="mid",
    )

    # 给老师用的，查看所有任教班级
    mid_to_class = relationship(
        "ClassesInfo",
        backref="mid"
    )


class StudentsInfo(Base):
    """学生信息表"""
    __tablename__ = "studentsInfo"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(64), nullable=False, comment="学生姓名")
    gender = Column(Enum("male", "female"), nullable=False, comment="学生性别")
    age = Column(Integer, nullable=False, comment="学生年龄")
    # 外键约束
    # 一对一关系必须为连接表的连接字段创建UNIQUE的约束，这样才能是一对一，否则是一对多
    fk_student_id = Column(
        Integer,
        ForeignKey(
            "studentsNumberInfo.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        nullable=False,
        comment="学生编号"
    )
    # 相比于一对一，连接表的连接字段不用UNIQUE约束即为多对一关系
    fk_class_id = Column(
        Integer,
        ForeignKey(
            "classesInfo.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        comment="班级编号"
    )
    # 逻辑字段
    # 所在班级, 这里是一对多关系，一个班级中可以有多名学生
    from_class = relationship(
        "ClassesInfo",
        backref="have_student",
    )
    # 学生学号，这里是一对一关系，一个学生只能拥有一个学号
    number_info = relationship(
        "StudentsNumberInfo",
        backref="student_info",
    )


if __name__ == "__main__":
    # 删除表
    Base.metadata.drop_all(engine)
    # 创建表
    Base.metadata.create_all(engine)