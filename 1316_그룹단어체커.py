n = int(input())
result = n

for i in range(0, n):
    A = input()
    for j in range (0, len(A)-1):
        if A[j] == A[j+1] : 
            pass
        elif A[j] in A[j+1:]:
            result -= 1
            break

print(result)

    


