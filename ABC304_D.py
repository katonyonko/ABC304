import io
import sys
import pdb
from bisect import bisect
from collections import defaultdict

_INPUT = """\
6
7 6
5
6 1
3 1
4 2
1 5
6 2
2
2 5
2
3 4
4 4
4
1 1
3 1
3 3
1 3
1
2
1
2
"""

def solve(test):
  W,H=map(int,input().split())
  N=int(input())
  s=[list(map(int,input().split())) for _ in range(N)]
  A=int(input())
  a=list(map(int,input().split()))
  B=int(input())
  b=list(map(int,input().split()))
  d=defaultdict(int)
  for i in range(N):
    d[(bisect(a,s[i][0]),bisect(b,s[i][1]))]+=1
  m,M=min([d[k] for k in d]),max([d[k] for k in d])
  if len(d)<(A+1)*(B+1): m=0
  if test==0:
    print(m,M)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)