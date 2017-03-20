# coding=utf-8

start='''    LOGD("++%s",__func__); \n'''
last='''     LOGD("--%s",__func__);	\n	'''

list=['int','int8_t','int16_t','int32_t',
      'void','fp_image_t*','static',
      'uint','uint8_t','uint16_t','uint32_t',
      'int*','int8_t*','int16_t*','int32_t*',
      'uint*','uint8_t*','uint16_t*','uint32_t*']

s1='('
s2='{'

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



def find_func_start_location():
    f=open('/Users/nancy/Documents/个人学习资料/python_loging/testfile.c','r+')
    linenumber=0
    alllist=f.readlines()

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
                for j in range(30):       # 在大括号那一行开始开始检查每一行最左边的字符是否在list里面，如果不在则停止查询
                    b=alllist[l+j].strip().split(' ')
                    if len(b)>0:
                        if b[0] not in list:
                            l=l+j
                            break

                alllist.insert(l, start)     # 插入开始调用函数的log打印语句

#    for i in alllist:
#        print(i,end='')
    lines=''.join(alllist)
    f.write(lines)
    f.write('/*------------------------------------------------------------------------*/')


find_func_start_location()







