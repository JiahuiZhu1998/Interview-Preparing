import sys


def solution(A):
    rowMax = []
    row_add = []
    row_add2 = []
    count = 0
    flag = 0
    for i in range(len(A)):
        if len(rowMax) == 0:
            row_add.append(A[i])
            rowMax.append(row_add)
        for m in range(len(rowMax)):
            count = 0
            for j in range(len(rowMax[m])):
                if rowMax[m][j] > A[i]: count = count + 1
                if count == len(rowMax[m]): rowMax[m].append(A[i])
            if (count + 1) != len(rowMax[m]) and j != 0:
                row_add2.clear()
                row_add2.append(A[i])
                rowMax.append(row_add2)
    return len(rowMax)


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    input = sys.stdin.readline().split()
    A = [int(x) for x in input[0].split(",")]
    # print(solution(A))
    sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
    main()
