import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())                                # TC
for test_case in range(1, T + 1):                         
    num = list(input())                         # input list 받아온다
    result = []                                 # 결과값 넣어줄 list
    start_num = ['3', '4', '5', '6', '9']       # 시작할 수 있는 카드 넘버 
    if num[4] != '-':                           # 만약 num index 4에 '-'이 없다면 4위치에 - 삽입
        num.insert(4,'-')
    if num[9] != '-':
        num.insert(9,'-')                       # 만약 num index 9에 '-'이 없다면 9위치에 - 삽입
    if num[14] != '-':                          
        num.insert(14,'-')                      # 만약 num index 14에 '-'이 없다면 14위치에 - 삽입
    
    for i in num:                               # 삽입한 결과를 반복문으로 순회하면서
        result.append(i)                        # result에 i를 하나씩 append

    if result[0] in start_num:                  # if result index 0이 start_num 중에 in 이라면
        if len(result) == 19:                   # 또, result의 글자 숫자가 19글자라면
            print(f'#{test_case} 1')            # TC와 가능하다는 1 출력
        else:
            print(f'#{test_case} 0')            # false라면 불가능하다는 0 출력
    else:
        print(f'#{test_case} 0')                # 첫번째 조건문에서 false 라면 0 출력

    #하고나서보니 너무 비효율인것 같다

    # else:
    #     print(f'#{test_case} 0')    



    # if num[4] != '-':
    #     num.insert(4,'-')
    # if num[9] != '-':
    #     num.insert(9,'-')
    # if num[14] != '-':
    #     num.insert(14,'-')