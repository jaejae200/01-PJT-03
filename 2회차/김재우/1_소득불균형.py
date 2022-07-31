import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())                                    # TC 입력

for test_case in range(1, T+1):                            
    N = int(input())                                 # 사람 수 N 입력
    
    result = list(map(int, input().split()))         # result = 소득 값 입력받음 list로
    
    average = sum(result) / N                        # 평균 = result 값을 모두 더하고 /  N 사람 수 나눔

    cnt = 0                                          # 평균 이상인 사람을 cnt해줄 변수 0 저장

    for j in result:                                 # 임시변수 j에 result 저장
        if j <= average:                             # j보다 평균이 높으면
            cnt += 1                                 # cnt 변수를 +1 해준다

    print(f'#{test_case} {cnt}')                     # TC와 cnt 출력





# import sys                                         # 모의고사 때의 풀이
#                                                    # map 함수와 for 문의 위치가 익숙하지 않았음.
# sys.stdin = open("_소득불균형.txt")

# T = int(input())                

# for test_case in range(1, T + 1):
#     N = int(input())
    
#     result = map(int, input().split()))
    
#     M = sum(result) / N
#     cnt = 0

#     for i in result: 
#         if i <= M:
#             cnt += 1

    # print(cnt)