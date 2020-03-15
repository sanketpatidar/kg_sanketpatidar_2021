def charmapp(s1, s2):
    mydict = {}
    flag = True
    if(len(s1) != len(s2)):
        flag = False
    else:
        for i in range(len(s1)):
            if s1[i] not in mydict:
                mydict[s1[i]] = s2[i]
            elif(mydict[s1[i]] != s2[i]):
                flag = False
    return flag


if __name__ == '__main__':
    s1 = str(input())
    s2 = str(input())
    print(charmapp(s1, s2))
