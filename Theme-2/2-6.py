import sys
A,B=map(int,sys.stdin.readline().split())
C=int(input())
if B+C<60:
	B+=C
else:
	B-=60-C
	A+=1+C//60
A-=24*(A//24)
print(A,B)