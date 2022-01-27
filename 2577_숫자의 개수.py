# numbers =  []
# for i in range(3):
#     n = int(input())
#     numbers.append(n)
    
# result = numbers[0] * numbers[1] * numbers[2]
# list_result = list(map(int, str(result)))

# for i in range(0, 10):
#     count = 0
#     for j in range(0, len(list_result)):
#         if(list_result[j] == i):
#             count += 1      

#     print(count)

result =1
for i in range(3):
    result *= int(input())


result = str(result)
count =[0]*10
for i in result:
    count[int(i)]+=1

for i in count:
    print(i)
        

