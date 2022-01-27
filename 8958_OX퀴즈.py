from itertools import count


n = int(input())

for i in range(n):
    ox_list = list(input())
    cnt = 0
    score = 0
    for i in ox_list:
        if i == 'O': # O이면 cnt 를 추가해주는데 연속이면 누적됨
            cnt += 1
            score = score + cnt # 그 누적치를 더해줌
        else:
            cnt = 0 # X가 나오면 CNT가 초기화댐 그래서 누적풀림
    
    print(score)