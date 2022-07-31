import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())                                # TC
for test_case in range(1, T + 1):       
    num = list(map(int, input().split()))       # 입력 값 list로 받아옴
    result_odd = 0                              # 홀수 값 저장할 변수 
    result_even = 0                             # 짝수 값 저장할 변수
    
    for i in num[0::2]:                         # num index 0부터 시작하고 끝까지 진행하는데 1번 건너뛰고 다음 index ex) 0 2 4 6
        result_odd += (i * 2)
    for i in num[1::2]:                         # num index 1부터 시작하고 끝까지 진행하는데 1번 건너뛰고 다음 index ex) 1 3 5 7 
        result_even += i            
    
    result = result_even + result_odd           # 전부 더해준 결과 값

    for j in range(10):                         # 0~9까지 숫자 중에 정답을 구하는 range 설정
        if (result + j) % 10 == 0:              # if result+j 가 10으로 나누었을때 나머지가 0이라면
            print(f'#{test_case} {j}')          # TC와 j값 출력