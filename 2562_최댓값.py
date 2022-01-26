# numbers = list(map(int, input().split()))
# max = 0

# for i in range(len(numbers)):
#     if numbers[i] > max:
#         max = numbers[i]
# print(max, i)

numbers = []
for i in range(9):
    n = int(input())
    numbers.append(n)

print(max(numbers))
print(numbers.index(max(numbers))+1)