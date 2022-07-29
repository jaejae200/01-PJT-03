import sys

sys.stdin = open("_최빈수구하기.txt")

my_list = []

T = int(input())                        # 10 입력받음

for test_case in range(1, T + 1):       # 1에서 10까지 반복
    test_num = int(input())
    score = map(int, input().split())
    for i in score:
        my_list.append(i)
            
    break



# for i in range(test_case):
#     print(i)
        

#         scores = map(int, input().split())
#         for j in scores:
#             score_list.append(i)

# print(score_list)
