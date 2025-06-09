import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    h = list(map(int,input().split()))
    x = list(map(int,input().split()))
    lo = 0
    hi = int(1e10)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        ev = defaultdict(int)
        for i in range(n):
            ma = (h[i] + mid - 1) // mid
            if ma > m: continue
            ev[x[i]-m+ma] += 1
            ev[x[i]+m-ma+1] -= 1
        sc = 0
        for y in sorted(ev.keys()):
            sc += ev[y]
            if sc >= k:
                hi = mid
                break
        else:
            lo = mid
    if hi == int(1e10):
        print(-1)
    else:
        print(hi)