import io
import sys
import pdb

_INPUT = """\
6
6
##.#.#
7
...####
12
####.####.##
"""

#素因数分解はここからコピーするのが多分速い
def gcd(a, b):
  while b: a, b = b, a % b
  return a
def lcm(a, b):
  return a // gcd(a, b) * b
def isPrimeMR(n):
  d = n - 1
  d = d // (d & -d)
  L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
  for a in L:
    t = d
    y = pow(a, t, n)
    if y == 1: continue
    while y != n - 1:
      y = y * y % n
      if y == 1 or t == n - 1: return 0
      t <<= 1
  return 1
def findFactorRho(n):
  m = 1 << n.bit_length() // 8
  for c in range(1, 99):
      f = lambda x: (x * x + c) % n
      y, r, q, g = 2, 1, 1, 1
      while g == 1:
          x = y
          for i in range(r):
              y = f(y)
          k = 0
          while k < r and g == 1:
              ys = y
              for i in range(min(m, r - k)):
                  y = f(y)
                  q = q * abs(x - y) % n
              g = gcd(q, n)
              k += m
          r <<= 1
      if g == n:
          g = 1
          while g == 1:
              ys = f(ys)
              g = gcd(abs(x - ys), n)
      if g < n:
          if isPrimeMR(g): return g
          elif isPrimeMR(n // g): return n // g
          return findFactorRho(g)
def primeFactor(n):
  i = 2
  ret = {}
  rhoFlg = 0
  while i * i <= n:
      k = 0
      while n % i == 0:
          n //= i
          k += 1
      if k: ret[i] = k
      i += i % 2 + (3 if i % 3 == 1 else 1)
      if i == 101 and n >= 2 ** 20:
          while n > 1:
              if isPrimeMR(n):
                  ret[n], n = 1, 1
              else:
                  rhoFlg = 1
                  j = findFactorRho(n)
                  k = 0
                  while n % j == 0:
                      n //= j
                      k += 1
                  ret[j] = k
  if n > 1: ret[n] = 1
  if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
  return ret
def divisors(N):
  pf = primeFactor(N)
  ret = [1]
  for p in pf:
      ret_prev = ret
      ret = []
      for i in range(pf[p]+1):
          for r in ret_prev:
              ret.append(r * (p ** i))
  return sorted(ret)

def solve(test):
  mod=998244353
  N=int(input())
  S=input()
  d=divisors(N)
  dd={}
  dk=sorted([k for k in d])
  for M in dk:
    if M==N: continue
    tmp=[0]*M
    for i in range(M):
      if len([j for j in range(N//M) if S[i+j*M]=='#'])==N//M: tmp[i]=1
    dd[M]=pow(2,sum(tmp),mod)
    for m in dk:
      if m<M and M%m==0: dd[M]-=dd[m]; dd[M]%=mod
  ans=sum([dd[k] for k in dd])%mod
  if test==0:
    print(ans)
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