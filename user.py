#TODO 代码逻辑整体优化
#TODO 日志记录功能

import copy

import gongneng


print("图书角管理系统 \nV1.0 (账户)")

userAndPassword = copy.deepcopy(gongneng.readDictionary("PasswordAndUser.ss"))

file = open("administrator.pp")
administrator = file.read()
file.close()

file = open("teacher.pp")
teacher = file.read()
file.close()

while True:
    a = int(input("注册【1】 密码修改【2】>"))
    if a == 1:
        u = str(input("用户："))
        if u in userAndPassword:
            print("已有此用户")
            continue
        p = str(input("密码："))
        userAndPassword[u] = p
        gongneng.writeDictionary("PasswordAndUser.ss", **userAndPassword)
        print("成功")
    elif a == 2:

        while True:
            u = str(input("修改的用户名："))
            if u in userAndPassword:

                while True:
                    p1 = str(input("原密码："))
                    if userAndPassword.get(u).__eq__(p1):
                        break
                    else:
                        print("密码错误！！")
                        continue
                while True:
                    sp = str(input("验证管理员或老师密码:"))
                    if sp.__eq__(teacher) or sp.__eq__(administrator):
                        p2 = str(input("新密码："))
                        userAndPassword[u] = p2
                        gongneng.writeDictionary("PasswordAndUser.ss",**userAndPassword)
                        print("成功")
                        break
                    else:
                        continue
                break
            else:
                print("无此用户")
                continue
    else:
        print("请输入1-2")
