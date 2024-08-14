from gongneng import *

NAME = "admin"

print("图书角管理系统 \nV1.0 (管理员)")

file = open("teacher.pp")
teacher = file.read()
file.close()

while True:
    p = str(input("密码："))
    if teacher.__eq__(p):
        break
    else:
        print("密码错误！！")
        continue
writelog("老师登录")
while True:
    a = int(input("查询【1】修改【2】>"))
    if a == 1:
        print("查询")
        chaxun(NAME, 2)
        a = 0
    elif a == 2:
        print("修改书籍")
        leixing = int(input("删除书籍【1】添加书籍【2】其他退出>"))
        if leixing == 1:
            xiugaiSuji(1)
            a = 0
        elif leixing == 2:
            xiugaiSuji(2)
            a = 0
    else:
        exit(0)
