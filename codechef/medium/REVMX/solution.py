# cook your dish here
import sys
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0]); p = 1
    out = []
    for _ in range(t):
        n = int(data[p]); p += 1
        P = data[p:p+n]; p += n
        P = [0] + [int(x) for x in P]
        pre = [0]*(n+1)
        for i in range(1, n+1):
            pre[i] = pre[i-1] + (1 if P[i] == i else 0)
        base = pre[n]
        groups = {}
        for i in range(1, n+1):
            j = P[i]
            if i < j and P[j] == i:
                groups.setdefault(i+j, []).append(i)
        best = 0
        for s, lst in groups.items():
            lst.sort(reverse=True)
            g = 0
            for i in lst:
                g += 2
                a, b = i, s-i
                loss = pre[b] - pre[a-1]
                if s % 2 == 0 and P[s//2] == s//2:
                    loss -= 1
                v = g - loss
                if v > best:
                    best = v
        out.append(base + best)
    print("\n".join(map(str, out)))
main()