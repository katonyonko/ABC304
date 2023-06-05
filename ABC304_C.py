import io
import sys
import pdb

_INPUT = """\
6
4 5
2 -1
3 1
8 8
0 5
3 1
0 0
-1000 -1000
1000 1000
9 4
3 2
6 -1
1 6
6 5
-2 -3
5 3
2 -3
2 1
2 6
"""

from collections import deque
def bfs(G,s):
  inf=10**30
  D=[inf]*len(G)
  D[s]=0
  dq=deque()
  dq.append(s)
  while dq:
    x=dq.popleft()
    for y in G[x]:
      if D[y]>D[x]+1:
        D[y]=D[x]+1
        dq.append(y)
  return D

def solve(test):
  N,D=map(int,input().split())
  G=[[] for _ in range(N)]
  p=[list(map(int,input().split())) for _ in range(N)]
  for i in range(N):
    x,y=p[i]
    for j in range(i+1,N):
      z,w=p[j]
      if (x-z)**2+(y-w)**2<=D**2:
        G[i].append(j)
        G[j].append(i)
  D=bfs(G,0)
  for i in range(N):
    if D[i]<10**4: print('Yes')
    else: print('No')

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