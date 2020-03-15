import sys


def charmapp(s1, s2):
    mydict = {}                    # Using a dictionary to map each character of s1 to s2
    flag = True
    if(len(s1) != len(s2)):        # Checking the length of s1 and s2 are equal or not if true return false
        flag = False
    else:                          # if false then checking one-to-one mapping exists or not
        for i in range(len(s1)):
            if s1[i] not in mydict:
                mydict[s1[i]] = s2[i]
            elif(mydict[s1[i]] != s2[i]):
                flag = False
                break
    return flag


if __name__ == '__main__':
    Input = sys.argv
    s1 = Input[1]
    s2 = Input[2]
    print(charmapp(s1, s2))
