import copy


def jieyue(sb):
    book = copy.deepcopy(readList("books.book"))
    jieyuebook = copy.deepcopy(readList("jieyue.book"))
    jieyue = copy.deepcopy(readDictionary("jieyue.ss"))
    guashi= copy.deepcopy(readDictionary("guashi.ss"))
    guashibook= copy.deepcopy(readList("guashi.book"))


    if sb in jieyue:
        print("你借阅了一本书，不能再借阅")
    elif sb in guashi:
        print("请先取消挂失丢失的书籍")

    
    else:
        a = ""

        while True:
            a = str(input("借阅的书名（无需加书名号）:"))

            if a in book and ((not a in guashibook) and (not a in jieyuebook)):
                break
            else:
                print("你借阅的书不在书库里、已被借走或丢失，检查你的书名")

                continue
        jieyue[sb] = a
        jieyuebook.append(a)
        writeDictionary("jieyue.ss", **jieyue)
        writeList("jieyue.book",*jieyuebook)
        print("成功")

    # print()


def guihuan(sb):
    admin = " "
    teacher = " "
    file = open("administrator.pp")
    admin = file.read()
    file.close()

    file = open("teacher.pp")
    teacher = file.read()
    file.close()
    print("归还")
    jieyue = copy.deepcopy(readDictionary("jieyue.ss"))
    jieyuebook = copy.deepcopy(readList("jieyue.book"))
    while True:
        b = str(input("书名:"))
        if b in jieyuebook:
            break
        else:
            print("没有此书，请检查书名")
    while True:

        a_t1 = str(input("验证管理员或老师密码："))
        if a_t1.__eq__(admin) or a_t1.__eq__(teacher):
            break
        else:
            print("密码错误，请重试！！")

    del jieyue[sb]

    for i in range(len(jieyuebook)):
        if b.__eq__(jieyuebook[i]):
            del jieyuebook[i]
            break
    writeList("jieyue.book",*jieyuebook)
    writeDictionary("jieyue.ss", **jieyue)
    print("成功")


def guashi(sb):
    #book=readList("books.book")
    jieyuebook=copy.deepcopy(readList("jieyue.book"))
    jieyue=copy.deepcopy(readDictionary("jieyue.ss"))
    guashibook=copy.deepcopy(readList("guashi.book"))
    guashi=copy.deepcopy(readDictionary("guashi.ss"))
    if not (sb in jieyue):

       print("你没有借阅任何书籍")
    else:
        a=""


        while True:
            a = str(input("挂失的书名（无需加书名号）"))
            if not (a in jieyuebook):
                print("没有此书，请检查书名")
                continue
            else:
                break
        del jieyue[sb]
        for i in range(len(jieyuebook)):
            if a.__eq__(jieyuebook[i]):
                del jieyuebook[i]
                break
        guashibook.append(a)
        guashi[sb]=a
        print("成功，加紧寻找，或理赔，然后取消挂失，在挂失过程中，不能借阅书籍")
        writeDictionary("guashi.ss",**guashi)
        writeList("guashi.book",*guashibook)

        writeDictionary("jieyue.ss",**jieyue)
        writeList("jieyue.book",*jieyuebook)
        print()

def chaxun(sb, quanxian=1):
    userandpassword=readDictionary("PasswordAndUser.ss")
    
    jieyue=copy.deepcopy(readDictionary("jieyue.ss"))
    guashi=copy.deepcopy(readDictionary("guashi.ss"))
    if quanxian ==1 :
        
        print(sb+"\t:目前的借阅 "+(jieyue[sb] if sb in jieyue else "无"),end=" ")
        print("目前的挂失 "+(guashi[sb] if sb in guashi  else "无"))
    elif quanxian ==2 and ("teacher".__eq__(sb) or "admin".__eq__(sb)):
        for chaxunSb in userandpassword.values():
            print(chaxunSb+"\t目前的借阅 "+(jieyue[chaxunSb] if chaxunSb in jieyue else "无"),end=" ")
            print("目前的挂失 "+guashi[chaxunSb] if chaxunSb in guashi  else "无")


    


def readDictionary(filename):
    dictionary = {}
    file = open(filename, 'r')
    
    linesInFile=file.readlines()
    
    if  len(linesInFile)== 0:
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
    linesInFile=file.readlines()
    
    if len(linesInFile) == 0:
        return []

    for line in linesInFile:
        line = line.split()
        list.append(*line)
    file.close()
    return list


def writeList(filename, *list):
    file = open(filename, "w")
    for i in list:
        file.write(str(i) + "\n")
