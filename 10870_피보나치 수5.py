n = int(input())

fibo = [0,1]
for i in range(2, n+1):
    num = fibo[i-1] + fibo[i-2]
    fibo.append(num)
print(fibo[n])

##########################
# 함수

def fibo(n):
    if n <= 1:
        return n

    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))