# import hashlib
#
#
# def jm_md5(password):
#     m = hashlib.md5()  # 构建MD5对象
#     m.update(password.encode(encoding='utf-8'))  # 设置编码格式 并将字符串添加到MD5对象中
#     password_md5 = m.hexdigest()  # hexdigest()将加密字符串 生成十六进制数据字符串值
#     return password, password_md5
#
#
# g = jm_md5('123456')
# print (g)


import hashlib

USER_LIST = []
def pwd_Md5(password):
    password = password+'hello python'  # 字符串混淆加盐，可以设置更复杂一点
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def register():
    print('**************用户注册**************')
    while True:
        user = input('请输入用户名:')
        if user.isalpha():
            break
    while True:
        password1 = input('请输入密码>>>:').strip()
        passwprd2 = input('请重复密码>>>：').strip()
        if password1 == passwprd2:
            password = pwd_Md5(password1)  # 将密码进行Md5加密
            break
        else:
            print('密码不正确，重新输入！')
    temp = {'username':user,'password':password}
    USER_LIST.append(temp)


def login():
    print('**************用户登陆**************')
    user = input('请输入用户名:')
    pwd = input('请输入密码:')

    for item in USER_LIST:
        if item['username'] == user and item['password'] == pwd_Md5(pwd):
            return True

if __name__=='__main__':

    register()
    if login():
        print('登陆成功')
    else:
        print('登陆失败')

