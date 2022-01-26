num=int(input())
check = num
count = 0
while(True):
    temp = num//10 + num%10 #5 + 5 = 10
    new_num = (num%10)*10 + temp%10 # 68 
    count += 1
    num = new_num
    if(new_num == check):
        break
print(count)
        
    
    


    