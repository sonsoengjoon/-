N= int(input())
A = list(map(int, input().split()))
max = A[0]
min = A[0]


for i in A[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min, max)
