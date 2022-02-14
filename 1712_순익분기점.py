# 고정비용 : 임대료, 재산세, 보험료, 급여 A만원 
# 가변비용 : 재료비, 인건비 등 B만원
# 노트북 가격 : C만원

# def son(A,B,C):
#     while(1):
#         n = 1
#         total_make = A + B*n
#         total_sale = C*n
        
#         if total_make > total_sale:
#             n += 1
#             continue
        
#         else:
#             break
    
#     return n

A,B,C = list(map(int, input().split()))

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))


        

    
    
    
