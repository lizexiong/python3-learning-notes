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


def Cal(math):

    nlms = re.search('\/|\*|\+|/-',math)
    if nlms is None:
        print ("math",math)


    MulOrDiv = re.search('\/|\*',math)
    #print (math)
    if MulOrDiv is not None:
        if MulOrDiv.group() == "*":
            #MulMath = re.search('\d+ ?\* ?\d+',math)
            MulMath = re.search('\d+(\.\d+)? ?\* ?\d+(\.\d+)?',math)
            MultiplyResult = str(float(re.split('\*',MulMath.group())[0]) * float(re.split('\*',MulMath.group())[1]))
            ComMulMath = re.escape(MulMath.group())
            FormulaToReplace = re.sub(ComMulMath,MultiplyResult,math)

            Cal(FormulaToReplace)
        elif MulOrDiv.group() == "/":
            DivMath = re.search('\d+(\.\d+)? ?\/ ?\d+(\.\d+)?',math)
            DirResult = str(float(re.split('\/',DivMath.group())[0]) / float(re.split('\/',DivMath.group())[1]))
            ComMulMath = re.escape(DivMath.group())
            FormulaToReplace = re.sub(ComMulMath,DirResult,math)
            Cal(FormulaToReplace)

    else:
        AddOrSub = re.search('\+|\-',math)
        if AddOrSub is not None:
            if AddOrSub.group() == "+":
                AddMath = re.search('\d+(\.\d+)? ?\+ ?\d+(\.\d+)?',math)
                AddtiplyResult = str(float(re.split('\+',AddMath.group())[0]) + float(re.split('\+',AddMath.group())[1]))
                ComMulMath = re.escape(AddMath.group())
                FormulaToReplace = re.sub(ComMulMath,AddtiplyResult,math)

            elif AddOrSub.group() == "-":
                SubMath = re.search('\d+(\.\d+)? ?\- ?\d+(\.\d+)?',math)
                SubResult = str(float(re.split('\-',SubMath.group())[0]) - float(re.split('\-',SubMath.group())[1]))
                ComMulMath = re.escape(SubMath.group())
                FormulaToReplace = re.sub(ComMulMath,SubResult,math)
            Cal(FormulaToReplace)




def test(User):
    str = re.findall(".+?\(.+?\)",User)
    print (str)

    for i in str:
        InnerStr = re.findall("\((.+?)\)",i)
        if i is not None:
            #print ("InnerStr",InnerStr)
            for k in InnerStr:
                print (k)
        else:
            print ("None")


# test(UserInput)
# Cal('9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ')

li = Cal('9-3.3333333333333335 + 2.3333333333333335*99/4*2998 +10 * 568/14')
print ('li',li)

# Cal(' 9-3.3333333333333335 + 7 /3*24.75*2998 +10 * 40.57142857142857')




