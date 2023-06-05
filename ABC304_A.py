import io
import sys
import pdb

_INPUT = """\
6
5
alice 31
bob 41
carol 5
dave 92
ellen 65
2
takahashi 1000000000
aoki 999999999
"""

def solve(test):
  N=int(input())
  members=[input().split() for _ in range(N)]
  members=[[members[i][0],int(members[i][1])] for i in range(N)]
  s=min([members[i][1] for i in range(N)])
  idx=0
  for i in range(N):
    if members[i][1]==s: idx=i; break
  for i in range(N):
    print(members[(i+idx)%N][0])

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