import sys
import threading

def main():
    import sys

    data = sys.stdin.readline().split()
    n = int(data[0])
    I = int(data[1])
    a = list(map(int, sys.stdin.readline().split()))

    a.sort()

    cnt = []
    current_val = a[0]
    current_count = 1

    for x in a[1:]:
        if x == current_val:
            current_count += 1
        else:
            cnt.append(current_count)
            current_val = x
            current_count = 1
    cnt.append(current_count)  

    D = len(cnt)  

    bits_per_elem = (8 * I) // n

    if bits_per_elem >= 20:
        print(0)
        return

    M = 1 << bits_per_elem  

    if M >= D:
        print(0)
        return

    pref = [0] * (D + 1)
    for i in range(D):
        pref[i + 1] = pref[i] + cnt[i]

    best = 0
    limit = D - M
    for i in range(limit + 1):
        s = pref[i + M] - pref[i]
        if s > best:
            best = s

    answer = n - best
    print(answer)

if __name__ == "__main__":
    threading.Thread(target=main).start()
