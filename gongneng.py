import copy


def jieyue(sb):
    book = copy.deepcopy(readList("books.book"))
    jieyue = copy.deepcopy(readList("jieyue.book"))
    read = readDictionary("jieyue.ss")

    if sb in read:
        print("你借阅了一本书，不能再借阅")
    else:
        a = ""

        while True:
            a = str(input("借阅的书名（无需加书名号）:"))

            if a in book and not (a in jieyue):
                break
            else:
                print("你借阅的书不在书库里、已被借走或丢失，检查你的书名")

                continue
        read[sb] = a
        jieyue.append(a)
        writeDictionary("jieyue.ss", **read)
        writeList("jieyue.book",*jieyue)
        print("成功")

    # print()


def guihuan(sb):
    administrator = " "
    teacher = " "
    file = open("administrator.pp")
    administrator = file.read()
    file.close()

    file = open("teacher.pp")
    teacher = file.read()
    file.close()
    print("归还")
    read = copy.deepcopy(readDictionary("jieyue.ss"))
    jieyue = copy.deepcopy(readList("jieyue.book"))
    while True:
        b = str(input("书名:"))
        if b in jieyue:
            break
        else:
            print("没有此书，请检查书名")
    while True:

        a_t1 = str(input("验证管理员或老师密码："))
        if a_t1.__eq__(administrator) or a_t1.__eq__(teacher):
            break
        else:
            print("密码错误，请重试！！")

    del read[sb]

    for i in range(len(jieyue)):
        if b.__eq__(jieyue[i]):
            del jieyue[i]
            break
    writeList("jieyue.book",*jieyue)
    writeDictionary("jieyue.ss", **read)
    print("成功")


def guashi(sb):
    book=readList("books.book")
    jieyue=readList("jieyue.book")
    read=readDictionary("jieyue.ss")
    guashibook=readList("guashi.book")
    guashi=readDictionary("guashi.ss")
    if not (sb in read):

       print("你没有借阅任何书籍")
    else:
        a=""


        while True:
            a = str(input("挂失的书名（无需加书名号）"))
            if not (a in jieyue):
                print("没有此书，请检查书名")
                continue
            else:
                break
        del read[sb]
        for i in range(len(jieyue)):
            if a.__eq__(jieyue[i]):
                del jieyue[i]
                break
        guashibook.append(a)
        guashi[sb]=a
        print("成功，加紧寻找，或理赔，然后取消挂失，在挂失过程中，不能借阅书籍")
        writeDictionary("guaishi.ss",guashi)
        writeList("guashi.book",guashibook)

        writeDictionary("jieyue.ss",read)
        writeList("jieyue.book",readList)








    print()

def chaxun(sb, quanxina=1):

    print()


def readDictionary(filename):
    dictionary = {}
    file = open(filename, 'r')

    
    a=len(file.readlines())==0
    if a:
        return {}
    else:
    

       for line in file.readlines():
           line = line.strip()
           k = line.split(' ')[0]
           v = line.split(' ')[1]
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
    if len(file.readlines()) == 0:
        return []

    for line in file.readlines():
        line = line.split()
        b = line
        list.append(*b)
        file.close()
    return list


def writeList(filename, *list):
    file = open(filename, "w")
    for i in list:
        file.write(str(i) + "\n")
