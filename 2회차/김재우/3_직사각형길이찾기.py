import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())                                 # TC 받아오기
for test_case in range(1, T + 1):               
    data = list(map(int, input().split()))       # 나머지 직사각형 3변의 길이 list로 받아오기
    result = 0                                   # 직사각형 1변의 길이를 구할 결과값
    if data.count(data[0]) == 3 :                # data count (인덱스0) 의 값이 3개라면 
        result = data[0]                         # result에 data 첫번쨰 인덱스 값을 저장해준다
    else:                                        # 아니라면
        if data.count(max(data)) == 1 :          # data count 의 최댓값이 1개와 같다면
            result = max(data)                   # result에 나머지 최댓값을 저장
        else :                                   # 아니라면
            result = min(data)                   # 최솟값을 result 에 저장

    print(f'#{test_case} {result}')              # tc와 result 출력