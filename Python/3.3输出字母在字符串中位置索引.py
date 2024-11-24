str = input()                       # 输入字符串
char1,char2 = input().split()       # 输入两个字符
for i in range(len(str)-1,-1,-1):   # 从右向左查找两个字符的索引
    if str[i] == char1:             # 若查找的与被查找的字符相同，则输出
        print(i,char1)
    elif str[i] == char2:
        print(i,char2)