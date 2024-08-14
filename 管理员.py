from gongneng import *

NAME = "admin"

print("图书角管理系统 \nV1.0 (管理员)")

file = open("administrator.pp")
admin = file.read()
file.close()

while True:
    p = str(input("密码："))
    if admin.__eq__(p):
        break
    else:
        print("密码错误！！")
        continue

writelog("管理员登录")

print(
    "相信你已经取得了管理员权限，作为权限拥有者，您务必清楚以下几点: \n(1)权力越大，责任越大; \n(2)做决策三思而后行; \n(3)公平公正。")

while True:
    a = int(input("借阅【1】 归还【2】 挂失【3】取消挂失【4】 查询【5】修改【6】>"))

    if a == 1:
        print("借阅")
        jieyue(NAME)

        a = 0

    elif a == 2:
        guihuan(NAME)
    elif a == 3:

        print("挂失")
        guashi(NAME)
        a = 0
    elif a == 4:
        print("取消挂失")
        quxiaoguashi(NAME)
        a = 0
    elif a == 5:
        print("查询")
        leixing = int(input("查询所有人【1】查询自身【2】>"))
        if leixing == 1:
            chaxun(NAME, 2)
            a = 0
        elif leixing == 2:
            chaxun(NAME, 1)
            a = 0
    elif a == 6:
        print("修改书籍")
        leixing = int(input("删除书籍【1】添加书籍【2】>"))
        if leixing == 1:
            xiugaiSuji(1)
            a = 0
        elif leixing == 2:
            xiugaiSuji(2)
            a = 0
    else:
        exit(0)
