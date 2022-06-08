__author__ = 'Administrator'


import re,sys

import decimal
#UserInput = """1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"""

#简单的验证函数，比如一些括号输入多了会判断出来，只实现了简单的判断
def verify(UserInput):
    ErrorStr=[]
    LeftBracket = []
    RightBracket = []
    for singlestr in UserInput:
        #搜索用户输入的函数，判断下面的值，如果有下面的值
        str = re.search('\+|\-|\*|\/|\(|\)|\.|\d+| ',singlestr)
        if str==None:
            #如果上面search没有搜索到，判断条件就是如果不在上面正则里面的都是错误字符，比如字符,那么就放入ErrorStr里面（其实这一步也不需要，写着玩玩）
            ErrorStr.append(singlestr)
        #然后统计左括号和右括号
        elif str.group() == '(':
            LeftBracket.append(str.group())
        elif str.group() == ')':
            RightBracket.append(str.group())

    #如果有错误字符，那么打印出来
    if len(ErrorStr) > 0 :
        print ("有错误字符,错误字符有以下:",ErrorStr)

    #然后对比左括号和右括号是不是相同的数量，如果不是，肯定是多了或者少了
    elif len(LeftBracket) > len(RightBracket):
        print ("多了一个左括号")
    elif len(LeftBracket) < len(RightBracket):
        print ("多了一个右括号")
    else:
        return True

    return False

#这里也是主函数最重要的第三个函数，判断 是否值是负号，比如   1*-1  1/-1 1+-1 1--1
#可以看到，下面船进入的是2个参数，一个是符号，一个是公式。当然，这里的公式就不是说1+1了，因为没有括号的情况下，公式还有可能是1+1+1+1+1。给Cal主函数计算的时候，得让他知道先匹配有负数的，还是没有负数的。
#比如   1*-1*-1*1 这里怎么匹配？怎么判断*-1在前面，还是*1在前面，如果这里判断不好，Cal()函数只有简单的search搜索第一个带有 *的公式。并且给他一个明确的通知，你第一个匹配的值是有负号，还是没有负号。
def IfMinus(InputComuteSign,math):
# '1*-2*-1388335.8476190479'
    #print (math)
    ComuteSign = re.escape(InputComuteSign)
    if InputComuteSign == "*":
        # result = re.search("(\*|\/|\+|\-){1}\-{1}\d+(\.\d+)?\*\-?\d+(\.\d+)?",math)
        # result = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\*\-?\d+(\.\d+)?",math)
        #介绍函数的时候说过了，1*-1*-1*1，怎么判断  *-1在前面还是*1在前面， 毕竟Cal（）函数匹配这个的区别就是匹配的时候多加一个\-的匹配。所以这里就要详细告诉他，谁在前面，你直接用最简单的方法去匹配就可以了
        #result_minus，来匹配  *-1带有负号的，正则怎么表示呢？    就是    *-1,如果是负数，那么 - 前面一定是加减乘除这个符号。
        #反之，如果-号前面是数字或者小数，那么这个-号就是一个减号。
        result_minus = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\*\-?\d+(\.\d+)?",math)
        result_normal = re.search("(\d+(\.\d+)?(\-){1})\d+(\.\d+)?\*\-?\d+(\.\d+)?",math)
    elif InputComuteSign == "/":
        # result = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\/\-?\d+(\.\d+)?",math)
        result_minus = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\/\-?\d+(\.\d+)?",math)
        result_normal = re.search("(\d+(\.\d+)?(\-){1})\d+(\.\d+)?\/\-?\d+(\.\d+)?",math)
    elif InputComuteSign == "+":
        # result = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\+\-?\d+(\.\d+)?",math)
        result_minus = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\+\-?\d+(\.\d+)?",math)
        result_normal = re.search("(\d+(\.\d+)?(\-){1})\d+(\.\d+)?\+\-?\d+(\.\d+)?",math)
    elif InputComuteSign == "-":
        # result = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\-\-?\d+(\.\d+)?",math)
        result_minus = re.search("((\*|\/|\+|\-){1}(\-){1}|^\-)\d+(\.\d+)?\-\-?\d+(\.\d+)?",math)
        result_normal = re.search("(\d+(\.\d+)?(\-){1})\d+(\.\d+)?\-\-?\d+(\.\d+)?",math)
    else:
        print ("系统判断出错,退出程序")
        sys.exit()

    #那么，接上面的逻辑，如果2个都不为空，那么怎么判断第一个公式是有负号的，还是没负号的？
    #很简单，如果2个不为None，那么就是公式中，2种情况都有。那么看搜索出来的他们的下标，下标小的肯定在前面
    if result_minus is not None and result_normal is not None:
        if result_minus.span()[0] < result_normal.span()[1]:
            return True
        elif result_minus.span()[0] > result_normal.span()[1]:
            return False
        else:
            sys.exit("程序退出，不会有这种公式")
    #如果一个值有，一个没有，那么返回对应的标识就行，标识True是-号，或者False是负号即可。
    elif result_minus is not None and result_normal is  None:
        return True
    elif result_normal is not None and result_minus is None:
        return False
    elif result_normal is not None and result_minus is not None:
        return False
    # if result is not None:
    #     return True
    # else:
    #     return False

#这是最主要的第二个函数，所有的加减乘除运算都在这个里面
#当然这里面有个最复杂的逻辑不在里面处理，那就是怎么判断是负号还是减号。单独出来一个函数等会讲解。
def Cal(math):
    #print ("math",math)
    #这里先匹配到，传进来的值是公式还是一个值，如果是一个值，比如1111，那么就不需要计算了，直接返回就可以了
    if re.match('^(\-|\+)?\d+(\.\d+)?$',math):return math
    # nlms = re.search('\/|\*|\+|\-',math)
    #下面两条过滤出计算符号，因为传进来的肯定是 1*1，或者1*1-1+1这样的公式
    #nlms = re.findall('((\-?\d+(\.\d+)?)?(\/|\*|\+|\-)(\-?\d+(\.\d+)?)?)?',math)   两条都可以过滤出计算符号，就是下标有点变动，下面的会更简洁，但是这里保留2条
    nlms = re.findall('(\-?\d+(\.\d+)?)?(\/|\*|\+|\-)(\-?\d+(\.\d+)?)?',math)
    #创建一个统计的所有符号个数的列表
    ComputeSign = list()
    for InnerTulple in nlms:
        ComputeSign.append(InnerTulple[2])

    #如果有符号，那么代表就是一个公式，那么就会开始计算。其实这里和函数第一行的判断重复了，都是判断需不需要计算，但是多一层保险也无所谓
    #如果符号列表大于0，那么就是说就是一个公式
    if len(ComputeSign) > 0:
        #如果有符号，不管什么符号，肯定先算乘除，后算加减，乘和除，谁先匹配到，就先算谁。
        #当然search前，要用join把列表转换为字符串。
        MulOrDiv = re.search('\/|\*',''.join(ComputeSign))
        if MulOrDiv is not None:
            #如果第一个匹配的是乘法
            if MulOrDiv.group() == "*":
                #MulMath = re.search('\d+ ?\* ?\d+',math)
                #这里就是一个比较重要的函数，判断到底是负号还是减号，比如1--1.这里有2个--，上述的正则要么全匹配，要么全部匹配，怎么办？
                #所以ifMinus专门判断这个公式，然后返回True或者false告诉你是匹配有负号的还是减号，这里详细逻辑，Ifminus函数会详细讲解。
                result = IfMinus(MulOrDiv.group(),math)

                #如果返回的是True，那么代表，这个公式的值里面一定有一个负号。那么就匹配整个公式的时候，多匹配一个-号
                if result == True:
                    MulMath = re.search('\-?\d+(\.\d+)?\*\-?\d+(\.\d+)?',math)
                else:
                    #否则，那么正常匹配第一个带有 *号的公式，前面不管是不是-号都不用管。
                    MulMath = re.search('\d+(\.\d+)?\*\-?\d+(\.\d+)?',math)

                #由于传过来的肯定是   1+1 这样一个简单的公式，所以用 计算符号分割他们就可以了，然后进行计算。
                MultiplyResult = str(float(re.split('\*',MulMath.group())[0]) * float(re.split('\*',MulMath.group())[1]))
                #匹配到的原始公式肯定有一个 计算公式符号，加上转义，不然替换的时候会当特殊字符处理
                ComMulMath = re.escape(MulMath.group())
                #然后替换整个计算好的字符串，然后交给  return Cal()这个函数递归计算下一个公式
                ToReplace = re.sub(ComMulMath,MultiplyResult,math)

            #和乘法一样的逻辑
            elif MulOrDiv.group() == "/":
                result = IfMinus(MulOrDiv.group(),math)
                if result == True:
                    DivMath = re.search('\-?\d+(\.\d+)?\/\-?\d+(\.\d+)?',math)
                else:
                    DivMath = re.search('\d+(\.\d+)?\/\-?\d+(\.\d+)?',math)
                DirResult = str(float(re.split('\/',DivMath.group())[0]) / float(re.split('\/',DivMath.group())[1]))
                ComDivMath = re.escape(DivMath.group())
                ToReplace = re.sub(ComDivMath,DirResult,math)
            #这里开始，肯定是不管乘法和除法，都要递归计算替换好的公式。所以if执行完成后，都会执行这个函数。
            return Cal(ToReplace)


        else:
            #如果不是乘法或者除法之后，那么才能算加减法。所以这里这里是else
            AddOrSub = re.search('\+|\-',''.join(ComputeSign))
            if AddOrSub is not None:
                #加法的逻辑就不多做说明。和乘法除法一样的，就是正则的时候，把乘法或者除法改成加法即可。
                if AddOrSub.group() == "+":
                    result = IfMinus(AddOrSub.group(),math)
                    if result == True:
                        AddMath = re.search('\-?\d+(\.\d+)?\+\-?\d+(\.\d+)?',math)
                    else:
                        AddMath = re.search('\d+(\.\d+)?\+\-?\d+(\.\d+)?',math)

                    AddtiplyResult = str(float(re.split('\+',AddMath.group())[0]) + float(re.split('\+',AddMath.group())[1]))
                    ComAddMath = re.escape(AddMath.group())
                    ToReplace = re.sub(ComAddMath,AddtiplyResult,math)

                #否则就是减法，减法和 乘法、除法、加法可不一样，因为减法更复杂，因为减法可能出现 1--1两个-号，分不清是负号还是减号，所以要做特殊处理。
                elif AddOrSub.group() == "-":
                    #print (math)
                    if AddOrSub is not None:
                        if AddOrSub.group() == "-":
                            #当然判断公式里面有没有负数的主要逻辑还是在ifMinus函数里面。下面的就和 上面三个计算符号的代码一样。
                            result = IfMinus(AddOrSub.group(),math)
                            if result == True:
                                SubMath = re.search('\-?\d+(\.\d+)?\-\-?\d+(\.\d+)?',math)
                            else:
                                SubMath = re.search('\d+(\.\d+)?\-\-?\d+(\.\d+)?',math)
                            SubSplit = SubMath.group().split('-')


                            #print (SubSplit)
                        #但是这里开始，可能会有多个减号，你不知道用那个-号来进行分割。可能 -1--1，三个减号，无法准确的识别是哪个减号。所以，就有了以下的特殊处理。
                        #如果公式通过split('-') 等于4，那么举个例子-12--12，如果split分割,如果是-，那么在列表里面就是一个空格。['', '12', '', '12']
                        #所以通过空格判断这个公式里面哪个是负号，是空格就是负号。因为前面说过，这个公式不管有多长，只会先计算一个公式，所以即使2个数都是负数，分割之后，列表最多长度就是4。
                        #判断拼接到底是负号还是减号
                            if len(SubSplit) == 4 and SubSplit[0] == "" and SubSplit[2]=="":
                                #判断得到的值是正数，所以这里通过判断手动加负号
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
                            #然后得到2个值，继续下去就和乘法、除法+加法一样了
                            SubResult = str(FirstNum - SecondNum)
                            ComSubMath = re.escape(SubMath.group())
                            ToReplace = re.sub(ComSubMath,SubResult,math)
                return Cal(ToReplace)
    else:
        return (math)

#抛弃验证，这里是计算的第一个主函数，这里功能就是判断括号，然后计算，然后递归判断括号。直到括号没有
def MainLogic(User):
    #print (User)
    # str = re.findall(".+?\(.+?\)",User)
    #先把输入的空格拿掉，不然后面正则的时候很麻烦，如果为了锻炼眼里，可以不拿掉空格
    UserHandle = User.replace(' ','')
    #brackets = re.search("\(\-?(?:\d+(?:\.\d+)?(?:\/|\*|\+|\-)\d+(?:\.\d+)?(?:\/|\*|\+|\-)?\d?(?:\.\d+)?)+\)",UserHandle)
    #这条正则就不详细解释了。简单来说 就是过滤出最里面的第一个括号
    # brackets = re.search("\(\-?(?:\d+(?:\.\d+)?(?:\/|\*|\+|\-)\-?\d+(?:\.\d+)?(?:\/|\*|\+|\-)?\-?\d?(?:\.\d+)?)+\)",UserHandle)
    brackets = re.search("\(\-?(?:\d+(?:\.\d+)?(?:\/|\*|\+|\-)\-?\d+(?:\.\d+)?(?:\/|\*|\+|\-)?\-?\d?(?:\.\d+)?(?:\/|\*|\+|\-)?\-?\d?(?:\.\d+)?)+\)",UserHandle)
    #print (brackets)
    if brackets is not None:
        #如果有括号，
        #BracketsInner = re.search('\-?(\d+(\.\d+)?(\/|\*|\+|\-)\d+(\.\d+)?(\/|\*|\+|\-)?\d?(\.\d?)?)+',brackets.group())
        #那么匹配出括号里面的所有内容，并去除()符号
        BracketsInner = re.findall('\((.+?)\)',brackets.group())
        #把正则匹配到的（）里面的公式丢给专门的计算函数去计算，并返回一个值。
        FormulaComputing = Cal(BracketsInner[0])
        #因为匹配出来的可能是 1+1 ，这里+号就是特殊符号，必须转义后面才能替换，不然会当特殊字符处理，escape就是给特殊字符加上\，来变成普通字符
        ComBracketsMath = re.escape(brackets.group())
        #然后将计算好的值替换没计算之前的字符串，这里就算好了一个（）里面的内容。就是一个新的表达式
        ToReplace = re.sub(ComBracketsMath,FormulaComputing,UserHandle)
        #然后将表达是递归给自己处理，看看还有没有括号，重复以上的步骤
        return MainLogic(ToReplace)
    else:
        # return Cal(User)
        #直到没有search到括号了，那么就可能会是一个公式，比如1+1+1，那么丢给专门计算的函数去解决，专门计算的函数里面有判断，里面是一个公式还是一个值。
        return Cal(UserHandle)


if __name__ == "__main__":
#test = MainLogic('-50*-1000*-200-(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)*(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)/(-1000*-200/200+111--1000*200--100)')
#test = MainLogic('-10000000.0-100*-100/10000*-10000*99965456--100--50*-1000*-200-(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)*(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)/(-1000*-200/200+111--1000*200--100)*-10022231/1545454+-12545454-(-5*-983/-12+12323)*13--9')
#test = MainLogic('-10000000.0-100*-100/10000*-10000*99965456--100--50*-1000*-200-(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100-(100*1-2-(-200*3-2/(-1200*10-12/3))))*(4--3*-3+-1)+1--2+-100*-100*(-4*-300/-100)/(-1000*-200/200+111--1000*200--100)*-10022231/1545454+-12545454-(-5*-983/-12+12323)*13--9')
#test = MainLogic('-10000000.0-100*-100/10000*-10000*99965456--100')
#test = MainLogic('-10000000.0+100/100/10000*-10000*99965456--100')
#test = MainLogic(UserInput)
    while True:
        UserInput = input("请输入正确的公式，或者按q退出计算器")
        if UserInput == 'q':
            sys.exit()
        else:
            VerifyResult = verify(UserInput)
            if VerifyResult == True:
                result = MainLogic(UserInput)
                print (result)
            else:
                pass


#调试ifMinus遗留代码
# test = IfMinus('*','1-2*-1388335.8476190479')
# print (test)