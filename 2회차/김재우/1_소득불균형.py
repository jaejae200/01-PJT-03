import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    
    result = list(map(int, input().split()))
    
    average = sum(result) / N

    cnt = 0 

    for j in result:
        if j <= average:
            cnt += 1

    print(f'#{i} {cnt}')









#     import sys

# sys.stdin = open("_소득불균형.txt")

# T = int(input())
# cnt = 0
# for test_case in range(1, T + 1):
#     N = int(input())
#     result = map(int, input().split())
#     M = sum(result) / N
#     M = int(M)
#     for i in result: 
#         if i <= M:
#             cnt += 1

#     print(cnt)