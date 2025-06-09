import sys
import bisect

def solve_case(n, types):
    m = len(types)
    a_vals = [a for a,b in types]
    a_vals.sort(reverse=True)
    base_sum = sum(a_vals[:min(n, m)])
    
    a_vals.sort() 
    prefix = [0]*(m+1)
    for i in range(m):
        prefix[i+1] = prefix[i] + a_vals[i]
    
    best = base_sum
    for a_j, b_j in types:
        i = bisect.bisect_left(a_vals, b_j)
        C = m - i  
        sumA = prefix[m] - prefix[i]  
        
        if a_j >= b_j:
            if C <= n:
                F = sumA + (n - C) * b_j
                if F > best:
                    best = F
        else:
            if C + 1 <= n:
                F = sumA + a_j + (n - (C + 1)) * b_j
                if F > best:
                    best = F
    return best

input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
idx = 1
out = []
for _ in range(t):
    while idx < len(input_data) and input_data[idx] == '':
        idx += 1
    n = int(input_data[idx]); m = int(input_data[idx+1])
    idx += 2
    types = []
    for __ in range(m):
        a = int(input_data[idx]); b = int(input_data[idx+1])
        idx += 2
        types.append((a, b))
    ans = solve_case(n, types)
    out.append(str(ans))

print("\n".join(out))