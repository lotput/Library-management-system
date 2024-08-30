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
writelog(u+"登录")
while True:
    a = int(input("借阅【1】 归还【2】 挂失【3】取消挂失【4】 查询【5】其他退出>"))

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
        print("取消挂失")
        quxiaoguashi(u)
        a = 0
        
    elif a == 5:
        print("查询")
        chaxun(u, 1)

    else:
        exit(0)
