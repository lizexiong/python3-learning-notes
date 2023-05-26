#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/26 23:26
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : 简单工厂.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm



#
# class Shape(object):
#     pass
#
# class  Triangle(Shape):
#
#     def draw(self):
#         print("画三角形")
#
# class  Square(Shape):
#
#     def draw(self):
#         print("画正方形")
#
#
# s1 = Triangle()
# s2 = Square()
#
# s1.draw()
# s2.draw()



class Shape(object):
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print('draw circle')

class Rectangle(Shape):
    def draw(self):
        print('draw Rectangle')

class ShapeFactory(object):
    def create(self, shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Rectangle':
            return Rectangle()
        else:
            return None

fac = ShapeFactory()
obj = fac.create('Circle')
obj.draw()