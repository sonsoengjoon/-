from unittest import result


N = int(input())
sum =1
for i in range(1,N+1):
    sum *= i
print(sum)

######################
# 재귀함수코드

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))

# 함수 안에서 함수 자기자신을 호출하는 방식
# 재귀호출이라고 한다. 재귀호출은 일반적인 상황에서는 잘 사용안하지만
# 알고리즘을 구현할 때 매우 유용하다. 보통 알고리즘에 
# 따라서 반복문으로 구현한 코드보다 재귀호출로 구현한 코드가 좀 더 
# 직관적이고 이해하기 쉬운 경우가 많다. 