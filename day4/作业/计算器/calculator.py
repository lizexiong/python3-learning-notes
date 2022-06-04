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
    print (math)
    nlms = re.search('\/|\*|\+|\-',math)
    if nlms is not None:
        MulOrDiv = re.search('\/|\*',math)
        if MulOrDiv is not None:
            if MulOrDiv.group() == "*":
                #MulMath = re.search('\d+ ?\* ?\d+',math)
                MulMath = re.search('\d+(\.\d+)? ?\* ?\d+(\.\d+)?',math)
                MultiplyResult = str(float(re.split('\*',MulMath.group())[0]) * float(re.split('\*',MulMath.group())[1]))
                ComMulMath = re.escape(MulMath.group())
                ToReplace = re.sub(ComMulMath,MultiplyResult,math)

            elif MulOrDiv.group() == "/":
                DivMath = re.search('\d+(\.\d+)? ?\/ ?\d+(\.\d+)?',math)
                DirResult = str(float(re.split('\/',DivMath.group())[0]) / float(re.split('\/',DivMath.group())[1]))
                ComDivMath = re.escape(DivMath.group())
                ToReplace = re.sub(ComDivMath,DirResult,math)
            return Cal(ToReplace)

        else:
            AddOrSub = re.search('\+|\-',math)
            if AddOrSub is not None:
                if AddOrSub.group() == "+":
                    AddMath = re.search('\d+(\.\d+)? ?\+ ?\d+(\.\d+)?',math)
                    AddtiplyResult = str(float(re.split('\+',AddMath.group())[0]) + float(re.split('\+',AddMath.group())[1]))
                    ComAddMath = re.escape(AddMath.group())
                    ToReplace = re.sub(ComAddMath,AddtiplyResult,math)

                elif AddOrSub.group() == "-":
                    SubMath = re.search('\d+(\.\d+)?\-\d+(\.\d+)?',math)
                    #print (SubMath.group())
                    SubResult = str(float(re.split('\-',SubMath.group())[0]) - float(re.split('\-',SubMath.group())[1]))
                    ComSubMath = re.escape(SubMath.group())
                    ToReplace = re.sub(ComSubMath,SubResult,math)
                return Cal(ToReplace)
    else:
        return (math)

def MainLogic(User):
    # str = re.findall(".+?\(.+?\)",User)
    UserHandle = User.replace(' ','')
    brackets = re.search("\(\-?(?:\d+(?:\.\d+)?(?:\/|\*|\+|\-)\d+(?:\.\d+)?(?:\/|\*|\+|\-)?\d?(?:\.\d+)?)+\)",UserHandle)
    if brackets is not None:
        #BracketsInner = re.search('\-?(\d+(\.\d+)?(\/|\*|\+|\-)\d+(\.\d+)?(\/|\*|\+|\-)?\d?(\.\d?)?)+',brackets.group())
        BracketsInner = re.findall('\((.+?)\)',brackets.group())
        # print (BracketsInner[0])
        FormulaComputing = Cal(BracketsInner[0])
        ComBracketsMath = re.escape(brackets.group())
        ToReplace = re.sub(ComBracketsMath,FormulaComputing,UserHandle)
        # print (ToReplace)
        return MainLogic(ToReplace)
    else:
        print("u",User)
        #(MainLogic(User))

        pass


#test = Cal('9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ')
# test = Cal('-4*3')
# print (test)


#MainLogic(UserInput)
#MainLogic('1 - 2 * ( (60-30 +(40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (4*3.1)/ (16-3*2.2) )')
test = MainLogic('1 - 2 * ( (60-30 +8.0 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (4*3.1)/ (16-3*2.2) )')
#Cal('9-2*5/3+7/3*99/4*2998+10*568/14')
print (test)


