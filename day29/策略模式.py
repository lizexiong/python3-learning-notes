#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/28 0:26
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : 策略模式.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm


class TravelStrategy(object):
    '''
    出行策略
    '''

    def travelAlgorithm(self):
        pass

class AirplaneStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("坐飞机出行....")

class TrainStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("坐高铁出行....")


class CarStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("自驾出行....")

class BicycleStrategy(TravelStrategy):
    def travelAlgorithm(self):
        print("骑车出行....")


class TravelInterface(object):
    def __init__(self,travel_strategy):
        self.travel_strategy = travel_strategy

    def set_strategy(self,travel_strategy):
        self.travel_strategy = travel_strategy
    def travel(self):
        return self.travel_strategy.travelAlgorithm()



#坐飞机
travel = TravelInterface(AirplaneStrategy())

travel.travel()

#改开车
travel.set_strategy(CarStrategy())
travel.travel()