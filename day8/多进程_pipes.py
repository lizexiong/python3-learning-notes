#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/18 22:18
# @Author  : 李泽雄
# @Site    : 
# @File    : 多进程_pipes.py
# @Project : python3
# @Software: PyCharm


from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    #子进程写入数据
    p = Process(target=f, args=(child_conn,))
    p.start()
    #父进程接收数据
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()