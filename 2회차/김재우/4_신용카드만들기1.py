import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    hol = num.index[:1:]
    print(hol)

    break