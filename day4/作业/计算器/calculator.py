__author__ = 'Administrator'





import re

UserInput = """1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"""


# str = re.findall('\+|\-|\*|\/|\(|\)|\d+',UserInput)

def verify():
    ErrorStr=[]
    LeftBracket = []
    RightBracket = []
    for singlestr in UserInput:
        str = re.search('\+|\-|\*|\/|\(|\)|\d+| ',singlestr)
        if str==None:
            ErrorStr.append(singlestr)
        elif str.group() == '(':
            LeftBracket.append(str.group())
        elif str.group() == ')':
            RightBracket.append(str.group())


    if len(ErrorStr) > 0 :
        print ("有错误字符,错误字符有以下:",ErrorStr)
    elif len(LeftBracket) > len(RightBracket):
        print ("多了一个左括号")
    elif len(LeftBracket) < len(RightBracket):
        print ("多了一个右括号")

def test(User):
    str = re.findall("\((.+?)\)",User)

    for i in str:
        InnerStr = re.findall("\((.+?)\(",i)
        if InnerStr is not None:
            print (InnerStr)
        else:
            print ("None")



test(UserInput)








