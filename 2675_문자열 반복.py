n = int(input())
for i in range(n):
    cnt, word = input().split() #####
    for x in word:
        print(x * int(cnt), end="") # end="" : 이어붙이기
    print()