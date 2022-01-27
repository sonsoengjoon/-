# arr = [] 
# for i in range(10):
#     arr.append(int(input()))

# for i in range(len(arr)):
#     arr[i] = arr[i]%42

# count= [0]*42
# for i in arr:
#     count[i] += 1

# cnt = 0
# for i in range(len(count)):
#     if(count[i] !=0 ):
#         cnt += 1

# print(cnt)

arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
# 중복을 제거하기 위한 필터 역할을 해줌 set
arr = set(arr)
print(len(arr))