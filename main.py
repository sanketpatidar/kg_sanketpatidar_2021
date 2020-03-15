import sys


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
    Input = sys.argv
    s1 = Input[1]
    s2 = Input[2]
    print(charmapp(s1, s2))
