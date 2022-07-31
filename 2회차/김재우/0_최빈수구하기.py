import sys

sys.stdin = open("_최빈수구하기.txt")

my_list = []

T = int(input())                            # TC 입력받음

for test_case in range(1, T + 1):           # 1에서 10까지 반복
    test_num = int(input())                 # test number
    score = list(map(int, input().split())) # list map 정수를 리스트로 input 받음
    my_list = [0] * 101                     # 0~ 100점 count 진행할 리스트
    
    for i in score:                         # score값 index 저장
        my_list[i] += 1                     # score 값을 my_list index 값에 +1 해서 저장해줌 ex 41점이다 =

    max_value = max(my_list)                # 최대 value =  my_list에서 최댓값
    result = []                             # 결과 list 생성
    for i in range(len(my_list)):           # my_list의 리스트 갯수만큼 반복
        if my_list[i] == max_value:         # 반복문을 순회하면서 My_list [i] 값이 == max_value와 같으면
            result.append(i)                # result 에 append 추가한다
   
    print(f'#{test_case} {max(result)}')    # TC 와 result 중 최대값 출력


# for i in range(test_case):
#     print(i)
        

#         scores = map(int, input().split())
#         for j in scores:
#             score_list.append(i)

# print(score_list)
