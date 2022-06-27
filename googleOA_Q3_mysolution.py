# One string is strictly smaller than another when the frequency of occurrence of the smallest character in the string 
# is less than the frequency of occurrence of the smallest character in the comparison string.   
# For example, string "abcd" is smaller than string "aaa" because the smallest character (in lexicographical order) in "abcd" is 'a', 
# with a frequency of 1, and the smallest character in "aaa" is also 'a', but with a frequency of 3. 
# In another example, string "a" is smaller than string "bb" because the smallest character in "a" is 'a' with a frequency of 1, 
# and the smallest character in "bb" is 'b' with a frequency of 2.   

# Write a function that, given string A (which contains M strings delimited by ',') 
# and string B (which contains N strings delimited by ','), returns an array C of N integers. 
# For 0 ≤ J < N, values of C[J] specify the number of strings in A which are strictly smaller than the comparison J-th string in B (starting from 0).
# For example, given strings A and B such that:    A = "abcd,aabc,bd"    B = "aaa,aa"   
#   the function should return [3, 2], because:   
#     All the strings in the array are strictly smaller than "aaa" on the basis of the given comparison criteria;   
#     Strings "abcd" and "bd" are strictly smaller than "aa".   
#     Assume that:  1 ≤ N, M ≤ 10000  1 ≤ length of any string contained by A or B ≤ 10  
#     All the input strings comprise only lowercase English alphabet letters (a-z)   
#     In your solution, focus on correctness. The performance of your solution will not be the primary focus of the assessment.

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

