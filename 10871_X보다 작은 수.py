#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# N,X=map(int, input().split())
# t = []
# for i in range(N):
#     t[N] = int(input())
    
# for i in range(N):
#     if(t[i] < X):
#         t[i] = t[i]
# print(t)

N,X=map(int, input().split())

A = list(map(int, input().split()))

for i in range(N):
    if(A[i] < X):
        print(A[i], end=" ")


# map 함수가 뭔지 파악하기

