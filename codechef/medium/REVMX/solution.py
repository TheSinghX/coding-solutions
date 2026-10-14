import sys
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0]); p = 1
    out = []
    for _ in range(t):
        n = int(data[p]); p += 1
        P = [0] + list(map(int, data[p:p+n])); p += n
        pre = [0] * (n + 1)
        c = 0
        for i in range(1, n + 1):
            if P[i] == i:
                c += 1
            pre[i] = c
        base = c
        M = n + 1
        keys = []
        for i in range(1, n + 1):
            j = P[i]
            if j != i:
                m = i if i < j else j
                keys.append((i + j) * M + (n - m))  # s ascending, m descending
        keys.sort()
        best = 0
        prev_s = -1
        gain = 0
        cf = 0
        for k in keys:
            s, r = divmod(k, M)
            L = n - r
            if s != prev_s:
                prev_s = s
                gain = 0
                cf = 1 if (s % 2 == 0 and P[s // 2] == s // 2) else 0
            gain += 1
            v = gain - (pre[s - L] - pre[L - 1] - cf)
            if v > best:
                best = v
        out.append(base + best)
    print("\n".join(map(str, out)))
main()