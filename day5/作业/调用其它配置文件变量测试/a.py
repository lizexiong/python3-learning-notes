



global test

test=1
print ("id",id(test))


def setX(new):
    global test
    test = new
    print ('a:',test)
    print('id(a):', id(test))



def aa():

    test=2
    print ('a:',test)
    print('id(a):', id(test))
