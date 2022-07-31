import sys

sys.stdin = open("_암호문1.txt")

T = int(input())                                # TC
for test_case in range(1, T + 1):
    num = int(input())
    
    num_list = list(map(int, input().split()))
    
    cmd_num = int(input())
    
    cmd = list(input().split())

    print(cmd.index('I'))