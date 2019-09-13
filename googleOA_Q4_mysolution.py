def solution(A,B):
    A_list=[];max=''
    for char in A:
        if char!=',':A_list.append(int(char))
    #print(A_list)
    subarrayL = []
    for i in range(len(A_list)-int(B)):
        subarrayL.append(A_list[i:i+int(B)])
    for i in range(len(subarrayL)):
        for j in range(1,len(subarrayL)):
            for m in range(len(subarrayL[i])):
                if subarrayL[i][m]>subarrayL[j][m]:
                    max=subarrayL[i]
                if subarrayL[i][m]<subarrayL[j][m]:
                    max=subarrayL[j]
    return max

if __name__ == "__main__":
    print(solution('1,4,3,2,5,4','4'))