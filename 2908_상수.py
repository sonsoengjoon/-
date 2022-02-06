# 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보기
# 상수는 수를 다른 사람과 다르게 꺼꾸로 읽는다. 

# 두 수를 입력 받음
# 두 수를 꺼꾸로 저장함 reverse O(n)
# 꺼꾸로 저장된 두 수 크기 비교 
# 더 큰 숫자를 출력

A,B = input().split()
a= list(reversed(A))
b= list(reversed(B))

if a > b :
    print("".join(a))
else:
    print("".join(b))

#################################
A,B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)


