import io
import sys
import pdb

_INPUT = """\
6
6 6
1 2
2 3
2 3
3 1
5 4
5 5
3
1 5
2 6
4 3
4
2 5
2 6
5 6
5 4
4 2
2 2
2 4
2
2 3
1 4
3
1 2
2 3
3 1
"""

import sys
sys.setrecursionlimit(10**6)
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.parents[x] > self.parents[y]:
       x, y = y, x
    self.parents[x] += self.parents[y]
    self.parents[y] = x
  def size(self, x):
    return -self.parents[self.find(x)]
  def same(self, x, y):
    return self.find(x) == self.find(y)
  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]
  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]
  def group_count(self):
    return len(self.roots())
  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}
  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def solve(test):
  N,M=map(int,input().split())
  G=[set() for _ in range(N)]
  uf=UnionFind(N)
  for _ in range(M):
    u,v=map(lambda x: int(x)-1, input().split())
    if uf.find(u)!=uf.find(v): uf.union(u,v)
  K=int(input())
  c=set()
  for _ in range(K):
    x,y=map(lambda t:int(t)-1,input().split())
    z,w=uf.find(x),uf.find(y)
    if z>w: z,w=w,z
    c.add((z,w))
  Q=int(input())
  for _ in range(Q):
    p,q=map(lambda t:int(t)-1,input().split())
    x,y=uf.find(p),uf.find(q)
    if x>y: x,y=y,x
    if (x,y) in c: print('No')
    else: print('Yes')

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