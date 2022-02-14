def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return 
    # 1,2,3 다 더하면 6 이라 6-start-end하면 보조기둥
    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)

# h(5, 1, 3, 2)

# h(시작, 보조, 목표)
# 원반이 한개 일때 
# if 원반개수 == 1 이면
# print(시작 -> 목표)

# 원반이 두개 일때 
# 1 -> 2 #가장 큰 원반을 제외한 모든 원반을 보조기둥으로
# 1 -> 3
# 2 -> 3
# 따라서 n-1개 의 원반을 보조기둥으로 모두 옮겨야 한다
# 마지막 원반이 목표로 가면 
# 원반의 개수가 n-1이 되고 보조기둥 을 시작 기둥으로 1번기둥을 보조기둥으로 
# 변경하면된다.
# def hani (원반개수, 시작, 목표, 보조):
#   if 원반개수 == 1:
    #     print(시작, 목표)
    #     return 
    # hanoi(원반개수-1, 시작, 보조, 목표)
    # print(시작, 목표)
    # hanoi(원반개수-1, 보조, 목표, 시작)
