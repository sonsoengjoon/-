n = int(input())
score = list(map(int, input().split()))
m = max(score)

new_score = 0
for i in range(n):
    new_score += score[i]/m*100

print(new_score/n)




