import copy
import time




def jieyue(sb):
    writelog(sb+"尝试借阅书籍")
    book = copy.deepcopy(readList("books.book"))
    jieyuebook = copy.deepcopy(readList("jieyue.book"))
    jieyue = copy.deepcopy(readDictionary("jieyue.ss"))
    guashi = copy.deepcopy(readDictionary("guashi.ss"))
    guashibook = copy.deepcopy(readList("guashi.book"))

    if sb in jieyue:
        print("你借阅了一本书，不能再借阅")
        writelog(sb+"借阅书籍失败")
    elif sb in guashi:
        print("请先取消挂失丢失的书籍")
        writelog(sb + "借阅书籍失败")


    else:
        a = ""


        a = str(input("借阅的书名（无需加书名号）:"))

        if a in book and ((not a in guashibook) and (not a in jieyuebook) and not (a.__eq__(" "))):

            jieyue[sb] = a
            jieyuebook.append(a)
            writeDictionary("jieyue.ss", **jieyue)
            writeList("jieyue.book", *jieyuebook)
            print("成功")
            writelog(sb+"借阅了书籍 "+"《"+a+"》")
        else:
            print("你借阅的书不在书库里、已被借走或丢失，检查你的书名")
            writelog(sb+"借阅书籍失败")



    # print()


def guihuan(sb):
    writelog(sb+"尝试归还书籍")
    file = open("administrator.pp")
    admin = file.read()
    file.close()

    file = open("teacher.pp")
    teacher = file.read()
    file.close()
    print("归还")
    jieyue = copy.deepcopy(readDictionary("jieyue.ss"))
    jieyuebook = copy.deepcopy(readList("jieyue.book"))

    b = str(input("书名:"))
    if b in jieyuebook:
        i=0
        while True:
            i=i+1

            a_t1 = str(input("验证管理员或老师密码(回车退出)："))
            if a_t1.__eq__(admin) or a_t1.__eq__(teacher):
                break
            elif a_t1.__eq__(""):
                writelog(sb + "管理员或老师密码验证失败")
                writelog(sb + "归还书籍失败")
                return 0
            else:
                print("密码错误，请重试！！")
                writelog(sb + "第"+str(i)+"次"+"管理员或老师密码尝试错误")


        del jieyue[sb]

        for i in range(len(jieyuebook)):
            if b.__eq__(jieyuebook[i]):
                del jieyuebook[i]
                break
        writeList("jieyue.book", *jieyuebook)
        writeDictionary("jieyue.ss", **jieyue)
        print("成功")
        writelog(sb+"归还了书籍 "+b)

    else:
        print("没有此书，请检查书名")
        writelog(sb+"归还书籍失败")



def guashi(sb):
    writelog(sb+"尝试挂失书籍")
    #book=readList("books.book")
    jieyuebook = copy.deepcopy(readList("jieyue.book"))
    jieyue = copy.deepcopy(readDictionary("jieyue.ss"))
    guashibook = copy.deepcopy(readList("guashi.book"))
    guashi = copy.deepcopy(readDictionary("guashi.ss"))
    if not (sb in jieyue):

        print("你没有借阅任何书籍，或借阅的书籍正在挂失")
        writelog(sb+"挂失书籍失败")
    else:
        a = ""


        a = str(input("挂失的书名（无需加书名号）"))
        if not (a in jieyuebook):
            print("没有此书，请检查书名")
            writelog(sb+"挂失书籍失败")

        else:
            del jieyue[sb]
            for i in range(len(jieyuebook)):
                if a.__eq__(jieyuebook[i]):
                    del jieyuebook[i]
                    break
            guashibook.append(a)
            guashi[sb] = a
            print("成功，加紧寻找，或理赔，然后取消挂失，在挂失期间，不能借阅书籍")
            writeDictionary("guashi.ss", **guashi)
            writeList("guashi.book", *guashibook)
            writeDictionary("jieyue.ss", **jieyue)
            writeList("jieyue.book", *jieyuebook)
            writelog(sb+"挂失了"+"《"+a+"》")



def quxiaoguashi(sb):

    writelog(sb+"取消尝试挂失书籍")
    guash = copy.deepcopy(readDictionary("guashi.ss"))
    guashibook = copy.deepcopy(readList("guashi.book"))
    file = open("administrator.pp")
    admin = file.read()
    file.close()

    file = open("teacher.pp")
    teacher = file.read()
    file.close()

    leixing = int(input("找到后(购买相同书后)取消挂失【1】 理赔后取消挂失【2】输入其他数离开 >"))
    if leixing == 1:
        writelog(sb+"选择了类型1")

        a = str(input("取消挂失的书名（无需加书名号）"))
        if not (a in guashibook):
            print("没有此书，请检查书名")
        i=0
        while True:
            i=i+1

            a_t1 = str(input("验证管理员或老师密码(回车退出)："))
            if a_t1.__eq__(admin) or a_t1.__eq__(teacher):
                break
            elif a_t1.__eq__(""):
                writelog(sb + "管理员或老师密码验证失败")
                writelog(sb + "取消挂失书籍失败")
                
            else:
                writelog("第"+str(i)+"次老师管理员或老师密码尝试错误")
                print("密码错误，请重试！！")
        a = ""



        del guash[sb]
        for i in range(len(guashibook) - 1):
            if a.__eq__(guashibook[i]):
                del guashibook[i]
            writeDictionary("guashi.ss", **guash)
            writeList("guashi.book", *guash)
            print("成功")
            writelog(sb + "取消挂失了(类型1)" + "《" + a + "》")


    elif leixing == 2:
        writelog(sb+"选择了类型2")
        a = ""


        a = str(input("取消挂失的书名（无需加书名号）"))
        if not (a in guashibook):
            print("没有此书，请检查书名")
        while True:
            i = i + 1

            a_t1 = str(input("验证管理员或老师密码(回车退出)："))
            if a_t1.__eq__(admin) or a_t1.__eq__(teacher):
                break
            elif a_t1.__eq__(""):
                writelog(sb + "管理员或老师密码验证失败")
                writelog(sb + "取消挂失书籍失败")

            else:
                writelog("第" + str(i) + "次老师管理员或老师密码尝试错误")
                print("密码错误，请重试！！")



        del guash[sb]

        writeDictionary("guashi.ss", **guash)
        print("成功")
        writelog(sb + "取消挂失了(类型2)" + "《" + a + "》")




def chaxun(sb, quanxian=1):

    userandpassword = readDictionary("PasswordAndUser.ss")

    jieyue = copy.deepcopy(readDictionary("jieyue.ss"))
    jieyuebook = copy.deepcopy(readList("jieyue.book"))
    guashi = copy.deepcopy(readDictionary("guashi.ss"))
    guashibook = copy.deepcopy(readList("guashi.book"))
    book = copy.deepcopy(readList("books.book"))
    if quanxian == 1:
        writelog(sb + "查询了书籍")
        print(sb + ": 目前的借阅 " + (jieyue[sb] if sb in jieyue else "无"), end=" ")
        print("目前的挂失 " + (guashi[sb] if sb in guashi else "无"))
    elif quanxian == 2 and ("teacher".__eq__(sb) or "admin".__eq__(sb)):
        writelog(sb+"以管理员或老师权限查询了书籍")
        print("总览")
        print("所有书籍：")
        for i in book:
            print(i, end=" ")

        print("\n借走的书籍:")
        for i in jieyuebook:
            print(i, end=" ")
        print("\n丢失的书籍:")
        for i in guashibook:
            print(i, end=" ")
        print("\n目前可借阅:")
        for i in book:
            if not ((i in jieyuebook) or (i in guashibook)):
                print(i, end=" ")
        print("\n分览")
        for chaxunSb in userandpassword.keys():
            print(chaxunSb + "\t: 目前的借阅 " + (jieyue[chaxunSb] + "\t" if chaxunSb in jieyue else "无\t"), end=" ")
            print("目前的挂失 " + (guashi[chaxunSb] + "\t" if chaxunSb in guashi else "无\t"))
        print("admin" + "\t: 目前的借阅 " + (jieyue["admin"] + "\t" if "admin" in jieyue else "无\t"), end=" ")
        print("目前的挂失 " + (guashi[chaxunSb] + "\t" if chaxunSb in guashi else "无\t"))

    elif quanxian == 2 and not ("teacher".__eq__(sb) or "admin".__eq__(sb)):
        writelog(sb + "以管理员或老师权限查询了书籍")
        print(sb + "\t:目前的借阅 " + (jieyue[sb] if sb in jieyue else "无"), end=" ")
        print("目前的挂失 " + (guashi[sb] if sb in guashi else "无"))
        print("此用户权限来源不当，拒绝访问其他用户的信息")
        writelog(sb + "越权，其他用户信息访问被驳回")


def xiugaiSuji(leixing):
    #TODO 日志记录功能
    book = copy.deepcopy(readList("books.book"))
    if leixing == 1:
        print("你必须确认此书不在挂失或借阅序列中，否则会出现不可预估的后果")
        a = ""

        a = str(input("要删除的的书籍(无需加书名号)"))

        if a in book:
            for i in range(len(book) - 1):
                if a.__eq__(book[i]):
                   del book[i]
                   writeList("books.book", *book)
                   print("成功")
                   break
                else:
                   print("没有此书,请检查书名")
                   continue
    elif leixing == 2:

        a = str(input("要添加的的书籍(无需加书名号)"))

        if not (a in book):
            book.append(a)
            writeList("books.book", *book)
        else:
            print("已经存在书籍")


def readDictionary(filename):
    dictionary = {}
    file = open(filename, 'r')

    linesInFile = file.readlines()

    if len(linesInFile) == 0:
        return {}
    else:
        for line in linesInFile:
            line = line.strip()
            k, v = line.split(' ')
            dictionary[k] = v

    file.close()
    return dictionary


def writeDictionary(filename, **dictionary):
    file = open(filename, 'w')
    for k, v in dictionary.items():
        file.write(str(k) + ' ' + str(v) + '\n')
    file.close()


def readList(filename):
    list = []
    file = open(filename, "r")
    linesInFile = file.readlines()

    if len(linesInFile) == 0:
        return []

    for line in linesInFile:
        line = line[0:len(line) - 1]

        list.append(line)

    file.close()
    return list


def writeList(filename, *list):
    file = open(filename, "w")
    for i in list:
        file.write(str(i) + "\n")

def writelog(neirong):

    # localtime = time.localtime(time.time())
    #localtime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    file = open("log.log","a")
    
    file.write("["+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))+"]"+neirong+"\n")
    file.close()
