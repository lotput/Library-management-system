import copy

from gongneng import *

print("图书角管理系统 \nV1.0 (学生)")
userandpassword = copy.deepcopy(readDictionary("PasswordAndUser.ss"))

u = ""

while True:
    u = str(input("用户名："))
    if u in userandpassword:

        while True:
            p = str(input("密码："))
            if userandpassword.get(u).__eq__(p):
                break
            else:
                print("密码错误！！")
                continue

        break
    else:
        print("无此用户")
        continue
print("借阅【1】 归还【2】 挂失【3】 查询【4】")

while True:
    a = int(input(">"))

    if a == 1:
        print("借阅")
        jieyue(u)

        a = 0

    elif a == 2:
        guihuan(u)
    elif a == 3:
        
        print("挂失")
        guashi(u)
        a = 0
    elif a == 4:
        print("查询")
        chaxun(u,1)
        a = 0
    else:
        print("输入1-4！")
        a = 0
        continue
