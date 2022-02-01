# 1트
N = int(input())
Input = int(input())

sum = 0
Input_list = list(str(Input))

for i in Input_list:    
    sum += int(i)

print(sum)

############################### 
# 수정후

N = int(input())
Input = list(input())

sum = 0

for i in Input:    
    sum += int(i)
print(sum)


