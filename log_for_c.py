# coding=utf-8

startstring='''    LOGD("++%s",__func__); \n'''
returnstring='''     LOGD("--%s",__func__); \n'''

list=['int','int8_t','int16_t','int32_t',
      'void','fp_image_t','fp_image_t*','static','struct','FILE','const',
      'uint','uint8_t','uint16_t','uint32_t',
      'int*','int8_t*','int16_t*','int32_t*',
      'uint*','uint8_t*','uint16_t*','uint32_t*']

s1='('
s2='{'

testlist=['qwe','rty','uio','asd']


def remove_duplicate(list):
    ''''
    去重，如果一个数组临近的两个元素一摸一样，则去掉其中一个
    '''
    l=list
    le=len(list)
    for i in range(le-1):
        if list[i]==list[i+1]:
            l=l[:i]+l[i+1:]
    return l


def find_s(string,s):
    '''
    :param string: 文件的某一行
    :param s: 如果某行存在某字符，例如"（"，"{"，则返回1，否则返回0
    :return:
    '''
    a=string.split(' ')
    for i in a:
        if s in i:
            return 1
    return 0


def start_location(alllist):
    linenumber=0
    for everyline in alllist:             # 遍历每一行
        a=everyline.split(' ')    # a是一行根据空格分割而成的字符串数组
        linenumber+=1
        if a[0] in list:                  # a[0]是一行的第一个字符串
            if find_s(everyline,s1):      # 如果某行第一个字符a[0]在list里面，则查询该行是否有"（"左括号
                l = linenumber
                for i in range(20):       # 若包含左括号，则查询20行内，第一次出现{ 大括号的地方,查到则停止查询，记住第几行l
                     if find_s(alllist[linenumber+i-1],s2):
                         l=linenumber+i
                         break
                for j in range(30):     # 在大括号那行开始检查每行最左边的非空格字符是否在list里面，如不在则停止查询，插入log
                    b=alllist[l+j].strip().split(' ')
                    if len(b)>1:
                        if b[0] not in list:
                            l=l+j
                            break
                alllist.insert(l, startstring)     # 插入开始调用函数的log打印语句

    return alllist


def end_location(alllist):
    '''
    添加函数结束log，但是log在return之后
    :param alllist:
    :return:
    '''
    linenumber=0
    for s in alllist:
        linenumber+=1
        s1=s.strip().split(' ')
        if s1[0]=='return':
            alllist.insert(linenumber,returnstring)
    return alllist
#    for i in alllist:
#        print(i,end='')


def change_return(list,n):
    '''
    交换list的n与n+1行
    :param list:
    :param n:
    :return:
    '''
    list[n],list[n+1]=list[n+1],list[n]


def find_all_return(list):
    '''
    找出所有return的行数
    :param list:
    :return:
    '''
    n=[]
    l=0
    for s in list:
        l+=1
        if s.strip().split(' ')[0]=='return':
            n.append(l-1)
    return n


def avoid_dup(list):
    '''
    一个数组相邻两行去重，防止添加多次log打印
    :param list:
    :return:
    '''
    m=[]
    n=len(list)
    for i in range(n-1):
        if list[i]==list[i+1]:
                m.append(i)
    x=0
    for j in m:
        list=list[:j+x]+list[j+x+1:]
        x-=1
    return list

def insert_string(list):
    '''
    在list输出log语句中插入一个相应的return语句
    :param string:
    :return:
    '''
    for i in find_all_return(list):
        ss=list[i].strip()
        ss = ss[:-1]
        list[i-1]=list[i-1][:12]+ss+list[i-1][12:]
    return list


if __name__ == '__main__':
    f = open('/Users/nancy/Documents/个人学习资料/python_loging/btlfp_core.c', 'r+')
    al = f.readlines()
    sta=start_location(al)
    en=end_location(sta)
#    print(find_all_return(en))
    for i in find_all_return(en):
        change_return(en,i)
    en = insert_string(en)
    en=avoid_dup(en)
#    for i in en:
#        print(i,end='')
#    print(en)
    f.seek(0,0)
    lines = ''.join(en)
    f.write(lines)
    f.close()








