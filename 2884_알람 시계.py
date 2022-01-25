# 45분 일찍 알람 설정하기
# 1시 35분 -> 24시 50분
A,B=input().split()
A=int(A)
B=int(B)
if(B<45):
    B = B - 45
    B = B + 60
    A = A - 1
    if(A<0):
        A = 23
    
    print(A,B)    

elif(B>=45):
    B = B - 45

    print(A,B)
