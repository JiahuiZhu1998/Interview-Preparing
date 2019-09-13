import sys


def solution(A, B):
    Alist=[];Blist=[];resultList=[];resultSet=set()
    str1 = '';str2=''
    for m in range(len(A)+1):
        if m==len(A):Alist.append(str1);break
        if A[m]==',':Alist.append(str1);str1=''
        else:str1=str1+A[m]
    for n in range(len(B)+1):
        if n==len(B):Blist.append(str2);break
        if B[n]==',':Blist.append(str2);str2=''
        else:str2=str2+B[n]

    for i in range(len(Blist)):
        resultSet = set()
        for j in range(len(Alist)):
            if findSmallChar(Blist[i])<findSmallChar(Alist[j]):
                resultSet.add(getFreq(findSmallChar(Blist[i]),Blist[i]))
            if findSmallChar(Blist[i])==findSmallChar(Alist[j]):
                if getFreq(findSmallChar(Blist[i]),Blist[i])>getFreq(findSmallChar(Alist[j]),Alist[j]):
                    resultSet.add(getFreq(findSmallChar(Blist[i]), Blist[i]))
        for char in resultSet:
            resultList.append(char)
            del(resultSet)
    return resultList
def findSmallChar(char):
    smallest='z'
    for cha in char:
        if cha <smallest:
            smallest=cha
    return smallest
def getFreq(smallest,str):
    count=0
    for char in str:
        if char==smallest: count = count+1
    return count
if __name__ == "__main__":
    print(solution('abcd,aabc,bd,cd','aaa,aa'))
    #print('a'<'b')
    #print(findSmallChar('bcdf'))
    #print(getFreq('c','aaaaaaaa'))

