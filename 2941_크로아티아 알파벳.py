cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
cro_num = 0
sum = 0
for j in cro:
    cnt = a.count(j)
    cro_num += cnt
    last_num = len(a) - cro_num
    sum = cro_num + last_num

print(last_num)
########################################################

# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia:
#     word = word.replace(i , "*")

# print(len(word))
