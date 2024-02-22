import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

a,b = map(int,input().split())
text = [a+b,a*b]

print(*text)