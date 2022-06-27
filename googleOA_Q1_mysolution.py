# You are given an array A representing heights of students. All the students are asked to stand in rows. The students arrive by one, sequentially (as their heights appear in A). For the i-th student, if there is a row in which all the students are taller than A[i], the student will stand in one of such rows. If there is no such row, the student will create a new row. Your task is to find the minimum number of rows created.
# Write a function that, given a non-empty array A containing N integers, denoting the heights of the students, returns the minimum number of rows created.
# For example, given A = [5, 4, 3, 6, 1], the function should return 2.
# Students will arrive in sequential order from A[0] to A[N−1]. So, the first student will have height = 5, the second student will have height = 4, and so on.
# For the first student, there is no row, so the student will create a new row.
# Row1 = [5]
# For the second student, all the students in Row1 have height greater than 4. So, the student will stand in Row1.
# Row1 = [5, 4]
# Similarly, for the third student, all the students in Row1 have height greater than 3. So, the student will stand in Row1.
# Row1 = [5, 4, 3]
# For the fourth student, there is no row in which all the students have height greater than 6. So, the student will create a new row.
# Row1 = [5, 4, 3]
# Row2 = [6]
# For the fifth student, all the students in Row1 and Row2 have height greater than 1. So, the student can stand in either of the two rows.
# Row1 = [5, 4, 3, 1]
# Row2 = [6]
# Since two rows are created, the function should return 2.
# Assume that:
#     N is an integer within the range [1..1,000]
#     each element of array A is an integer within the range [1..10,000]
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment

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
