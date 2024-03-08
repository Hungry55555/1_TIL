import sys
sys.stdin = open('input.txt')

import sys


x=int(sys.stdin.readline())
memo=[]
for i in range(x):
    memo.append(int(sys.stdin.readline()))
memo.sort()
for i in memo:
    print(i)