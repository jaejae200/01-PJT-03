import sys

sys.stdin = open("_문자열의거울상.txt")



T = int(input())                        # tc 받음
for test_case in range(1, T + 1):  
    word = input()                      # 거울상 문자 입력
    result = ''                         # 결과에 빈 문자 = 공백 할당

    for i in word[::-1]:                # word를 뒤집은 결과를 index에 넣고 하나하나 비교
        if i == 'b' :                   # 'b' 라면 
            result += 'd'               # 'd' 를 result에 저장
        elif i == 'd' :                 # ...
            result += 'b'
        elif i == 'p' :
            result += 'q'
        else :
            result += 'p'

    print(f'#{test_case} {result}')     # tc와 result 출력
    
    
    
    # reverse = rev(word)
    # print(reverse)
    # bdppq
    # qqqqpppbbd