import sys
sys.stdin = open('input.txt')

N = int(input())
text=[]
while N!=0:
    n = N%2
    text.insert(0,n)
    N = N//2

print(*text)