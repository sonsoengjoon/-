# cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# a = input()
# sum = 0
# for _ in range(len(a)):
#     for j in cro:
#         cnt = a.count(j)
#         sum += cnt

# print(sum)
########################################################

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i , "*")

print(len(word))
