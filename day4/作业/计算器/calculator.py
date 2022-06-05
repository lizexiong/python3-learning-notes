__author__ = 'Administrator'


import re,sys

# UserInput = """1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"""
UserInput = """ (4--3*-3+-1)+ 1--2+-100*-100*(-4*-300/-100)"""

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


def IfMinus(InputComuteSign,math):
# '1*-2*-1388335.8476190479'
    #print (math)
    ComuteSign = re.escape(InputComuteSign)
    if InputComuteSign == "*":
        # result = re.search("(\*|\/|\+|\-){1}\-{1}\d+(\.\d+)?\*\-?\d+(\.\d+)?",math)
        result = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\*\-?\d+(\.\d+)?",math)
    elif InputComuteSign == "/":
        result = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\/\-?\d+(\.\d+)?",math)
    elif InputComuteSign == "+":
        result = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\+\-?\d+(\.\d+)?",math)
    elif InputComuteSign == "-":
        result = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\-\-?\d+(\.\d+)?",math)
    else:
        print ("系统判断出错,退出程序")
        sys.exit()
    if result is not None:
        return True
    else:
        return False


def Cal(math):
    #print ("math",math)
    if re.match('^(\-|\+)?\d+(\.\d+)?$',math):return math

    # nlms = re.search('\/|\*|\+|\-',math)
    #nlms = re.findall('((\-?\d+(\.\d+)?)?(\/|\*|\+|\-)(\-?\d+(\.\d+)?)?)?',math)   两条都可以过滤出计算符号，就是下标有点变动，下面的会更简洁，但是这里保留2条
    nlms = re.findall('(\-?\d+(\.\d+)?)?(\/|\*|\+|\-)(\-?\d+(\.\d+)?)?',math)
    ComputeSign = list()
    for InnerTulple in nlms:
        ComputeSign.append(InnerTulple[2])

    if len(ComputeSign) > 0:
        MulOrDiv = re.search('\/|\*',''.join(ComputeSign))
        if MulOrDiv is not None:
            if MulOrDiv.group() == "*":
                #MulMath = re.search('\d+ ?\* ?\d+',math)
                result = IfMinus(MulOrDiv.group(),math)

                if result == True:
                    MulMath = re.search('\-?\d+(\.\d+)?\*\-?\d+(\.\d+)?',math)
                else:
                    MulMath = re.search('\d+(\.\d+)?\*\-?\d+(\.\d+)?',math)
                #print (MulMath.group())

                MultiplyResult = str(float(re.split('\*',MulMath.group())[0]) * float(re.split('\*',MulMath.group())[1]))
                # print ('MultiplyResult',MultiplyResult)

                ComMulMath = re.escape(MulMath.group())
                print ('math',math)
                print ("ComMulMath",ComMulMath)

                ToReplace = re.sub(ComMulMath,MultiplyResult,math)
                # print ('before math',math)
                print ("Toreplace",ToReplace)

            elif MulOrDiv.group() == "/":
                result = IfMinus(MulOrDiv.group(),math)
                if result == True:
                    DivMath = re.search('\-?\d+(\.\d+)?\/\-?\d+(\.\d+)?',math)
                else:
                    DivMath = re.search('\d+(\.\d+)?\/\-?\d+(\.\d+)?',math)
                DirResult = str(float(re.split('\/',DivMath.group())[0]) / float(re.split('\/',DivMath.group())[1]))
                ComDivMath = re.escape(DivMath.group())
                ToReplace = re.sub(ComDivMath,DirResult,math)
            return Cal(ToReplace)

        else:
            AddOrSub = re.search('\+|\-',''.join(ComputeSign))
            #print ('test',''.join(ComputeSign),'Addor',AddOrSub.group())
            if AddOrSub is not None:
                if AddOrSub.group() == "+":
                    result = IfMinus(AddOrSub.group(),math)
                    if result == True:
                        AddMath = re.search('\-?\d+(\.\d+)?\+\-?\d+(\.\d+)?',math)
                    else:
                        AddMath = re.search('\d+(\.\d+)?\+\-?\d+(\.\d+)?',math)

                    # AddMath = re.search('\-?\d+(\.\d+)?\+\-?\d+(\.\d+)?',math)
                    AddtiplyResult = str(float(re.split('\+',AddMath.group())[0]) + float(re.split('\+',AddMath.group())[1]))
                    ComAddMath = re.escape(AddMath.group())
                    ToReplace = re.sub(ComAddMath,AddtiplyResult,math)

                elif AddOrSub.group() == "-":
                    if AddOrSub is not None:
                        if AddOrSub.group() == "-":
                            result = IfMinus(AddOrSub.group(),math)
                            if result == True:
                                SubMath = re.search('\-?\d+(\.\d+)?\-\-?\d+(\.\d+)?',math)
                            else:
                                SubMath = re.search('\d+(\.\d+)?\-\-?\d+(\.\d+)?',math)
                            #print ('subMath',SubMath.group())
                    #SubMath = re.search('\-?\d+(\.\d+)?\-\-?\d+(\.\d+)?',math)
                            #print ("SubMath",SubMath.group())
                            SubSplit = SubMath.group().split('-')

                    #print (SubSplit)
                    #判断拼接到底是负号还是减号
                            if len(SubSplit) == 4 and SubSplit[0] == "" and SubSplit[2]=="":
                                FirstNum = -float(SubSplit[1])
                                SecondNum = -float(SubSplit[3])
                            elif len(SubSplit) == 3 and SubSplit[0] == "" and SubSplit[2]!="":
                                FirstNum = -float(SubSplit[1])
                                SecondNum = float(SubSplit[2])
                            elif len(SubSplit) == 3 and SubSplit[0] != "" and SubSplit[1]=="":
                                FirstNum = float(SubSplit[0])
                                SecondNum = -float(SubSplit[2])
                            else:
                                FirstNum = float(SubSplit[0])
                                SecondNum = float(SubSplit[1])
                            SubResult = str(FirstNum - SecondNum)
                            ComSubMath = re.escape(SubMath.group())
                            ToReplace = re.sub(ComSubMath,SubResult,math)
                return Cal(ToReplace)
    else:
        return (math)

def MainLogic(User):
    #print (User)
    # str = re.findall(".+?\(.+?\)",User)
    UserHandle = User.replace(' ','')
    #brackets = re.search("\(\-?(?:\d+(?:\.\d+)?(?:\/|\*|\+|\-)\d+(?:\.\d+)?(?:\/|\*|\+|\-)?\d?(?:\.\d+)?)+\)",UserHandle)
    brackets = re.search("\(\-?(?:\d+(?:\.\d+)?(?:\/|\*|\+|\-)\-?\d+(?:\.\d+)?(?:\/|\*|\+|\-)?\-?\d?(?:\.\d+)?)+\)",UserHandle)
    if brackets is not None:
        #BracketsInner = re.search('\-?(\d+(\.\d+)?(\/|\*|\+|\-)\d+(\.\d+)?(\/|\*|\+|\-)?\d?(\.\d?)?)+',brackets.group())
        BracketsInner = re.findall('\((.+?)\)',brackets.group())
        FormulaComputing = Cal(BracketsInner[0])
        ComBracketsMath = re.escape(brackets.group())
        ToReplace = re.sub(ComBracketsMath,FormulaComputing,UserHandle)
        return MainLogic(ToReplace)
    else:
        # return Cal(User)
        return Cal(UserHandle)



# def calctest(user):
#     nlms = re.findall('((\-?\d+(\.\d+)?)?(\/|\*|\+|\-)(\-?\d+(\.\d+)?)?)?',user)
#     print (nlms)



# test = MainLogic('1-2*-1388335.8476190479')
# print (test)
          #  1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
#MainLogic('1 - 2 * ( (60-30 +(40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (4*3.1)/ (16-3*2.2) )')
# test1 = MainLogic('1 - 2 * ( (60-30 +8.0 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (4*3.1)/ (16-3*2.2) )')
# print (test1)
#Cal('9-2*5/3+7/3*99/4*2998+10*568/14')
# print (test)


# calctest('9--2*5/3+7/3*99/-4*2998+10*568/14')
# Cal('9-2*5/3+7/3*99/-4*2998-100+-10*-568/14')
# Cal('-172823.11904761908')



# MultiplyResult 2776671.6952380957
# ComMulMath \-2\*\-1388335\.8476190479
# math 1-2*-1388335.8476190479
# before math 1-2*-1388335.8476190479
# Toreplace 12776671.6952380957
# 12776671.6952380957



# test = Cal('1-2*100')
# print (test)

#test = MainLogic('-50*-1000*-200-(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)*(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)/(-1000*-200/200+111--1000*200--100)')
test = MainLogic('-50*-1000*-200-(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)*(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)/(-1000*-200/200+111--1000*200--100)*-10022231/1545454+-12545454-(-5*-983/-12+12323)*13--9')
#test = MainLogic('-10000000.0-100*-100/10000*-10000*99965456--100')
print (test)

# test = IfMinus('*','1-2*-1388335.8476190479')
# print (test)