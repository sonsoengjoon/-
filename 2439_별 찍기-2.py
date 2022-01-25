n = int(input())

#for i in range(1, n+1):
#    print(" " * (n-i) + "*" * i)



# range(시작하는 숫자, 끝나는 숫자, 증가분)

for i in range(n-1, -1, -1):
    print(" " * i + "*" *(n-i))