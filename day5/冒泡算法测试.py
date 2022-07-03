__author__ = 'Administrator'
#!/usr/bin/env python




#这里我们一点点来进化这个版本，让自己更加理解。
#第一版

# data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
#
# #枚举，index是索引，i是列表的值
# for index,i in enumerate(data[0:-1]):
#     #i代表当前列表下标值，index+1就是他前面一个
#     #如果当前值大于前面一个，那么就和前面那个值换个位置
#     if i > data[index+1]:
#         tmp = data[index]
#         data[index] = data[index+1]
#         data[index+1] = tmp
#
# print (data)

#结果输出
#可以看到，结果就调换了前后2个结果，很多没有调整，所以直接来下一版。
#
#[4, 10, 21, 33, 3, 54, 8, 5, 11, 2, 1, 22, 13, 6, 17]



#第二版
# data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
#
# for i in range((len(data)-1)):
#     if data[i] > data[i+1]:
#         tmp = data[i]
#         data[i] = data[i+1]
#         data[i+1] = tmp
#
# print (data)
# #这一版本冒失可以，把最大的放到最前面了。如果按照这个思路，每一次调整一个最大数到最前面，那么是不是循环完列表的长度，顺序就好了？
# #对，就是这样，所以，结果来看第三版
# #[4, 10, 21, 33, 3, 8, 11, 5, 22, 2, 1, 17, 13, 6, 54]


#第三版-完结版版本
data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]


#为什么要有两层循环？因为循环一次，就只把一个数放到了最前面
for i in range(1,len(data)):
    #为什么这里是len(data)-i,因为每对比完成一次，最大的就在最前面，没有必要在多比对一次，依次循环，就可以减少很多次对比
    for j in range(len(data)-i):
        if data[j] > data[j+1]:
            tmp = data[j]
            data[j] = data[j+1]
            data[j+1] = tmp

print (data)

#[1, 2, 3, 4, 5, 6, 8, 10, 11, 13, 17, 21, 22, 33, 54]