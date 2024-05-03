import sys
input = sys.stdin.readline

N = int(input())

A = [x for x in map(int, input().split())]
B = [x for x in map(int, input().split())]

A.sort()
B.sort(reverse=True)

sum = 0

for i in range(N):
    sum += A[i]*B[i]

print(sum)