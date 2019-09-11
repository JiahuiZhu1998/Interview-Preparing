import sys
import itertools

def solution(A):
    """Your solution goes here."""
    sumTotal=sum(A);sumNow=0
    server1 =[];server2 =[]
    i=len(A)
    while(i>0):
        if i==len(A) or i==len(A)-1:
            sumNow=sumTotal-A[i-1]-A[i-2]
            server1.append(A[i-1])
            server2.append(A[i-2])
            i=i-2
        else:
            sumNow=sumNow-A[i-1]
            if sumNow>A[i-1]:
                server1.append(A[i-1])
            elif sumNow==A[i-1]:
                server1.append(A[i-1])
                for j in range(i-1):
                    server2.append(A[j])
                break
            else:
                server2.append(A[i-1])
            i=i-1
    return(sum(server1) - sum(server2))


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
