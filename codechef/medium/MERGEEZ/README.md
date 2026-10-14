# MERGEEZ

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Merging (Easy)

Define $merge(A, B)$ as the array $C$ formed by the following process:

- Initialize $i = 0, j = 0, C = []$ (empty array)
- While both $i < |A|, j < |B|$ holds, do the following: if $A_i < B_j$, append $A_i$ to $C$ and increment $i$ by $1$. Else, append $B_j$ to $C$ and increment $j$ by $1$.
- While $i < |A|$, append $A_i$ to $C$ and increment $i$ by $1$.
- While $j < |B|$, append $B_j$ to $C$ and increment $j$ by $1$.

For example, it can be shown that $merge([2, 3], [1, 4]) = [1, 2, 3, 4]$, and $merge([3, 2], [4, 1]) = [3, 2, 4, 1]$.

You are given a permutation $P$ of the integers $[1, N].$

For each $i = 0, 1, 2, \ldots, N$, count how many pairs of arrays $A$ and $B$ exist such that $merge(A, B) = P$ and $|A| = i$. Since the answers may be large, output them modulo $998244353$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $P_1, P_2, \ldots, P_N$.
### Output Format

For each test case, output on a new line $N + 1$ integers - the number of pairs of arrays $A$ and $B$ such that $|A| = i$ for each $i = 0, 1, \ldots, N$ modulo $998244353$.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 5000$
- $1 \le P_i \le N$
- $P_i \ne P_j$ for all $i \ne j$
- The sum of $N$ over all test cases does not exceed $5000$.
### Sample 1:
Input
Output

```
4
4
1 2 3 4
4
3 2 4 1
1
1
7
2 4 3 6 5 1 7

```

```
1 4 6 4 1
1 0 2 0 1
1 1
1 2 2 3 3 2 2 1
```

### Explanation:

 **Test Case 1:**  Every sorted subset of $P$ works as $A$, and its complement as $B$. This is because the merge (as defined) of $2$ sorted arrays will always be sorted.

 **Test Case 2:**  The possibilities are:

- $A = [], B = [3, 2, 4, 1]$
- $A = [3, 2], B = [4, 1]$
- $A = [4, 1], B = [3, 2]$
- $A = [3, 2, 4, 1], B = []$

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T15:56:52.674Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;
typedef unsigned int u32;
typedef unsigned long long u64;
const u32 MOD = 998244353;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        vector<int> P(n + 1);
        for (int i = 1; i <= n; i++) scanf("%d", &P[i]);

        vector<int> g(n + 1, 0), st;
        for (int p = 1; p <= n; p++) {
            while (!st.empty() && P[st.back()] < P[p]) st.pop_back();
            g[p] = st.empty() ? 0 : st.back();
            st.push_back(p);
        }

        int W = n + 1;
        vector<u32> CA((size_t)W * W, 0), CB((size_t)W * W, 0);
        vector<u32> ans(n + 1, 0);

        for (int p = 1; p <= n; p++) {
            u32 *ca = &CA[(size_t)p * W], *cb = &CB[(size_t)p * W];
            const u32 *pa = &CA[(size_t)(p - 1) * W], *pb = &CB[(size_t)(p - 1) * W];
            const u32 *ga = &CA[(size_t)g[p] * W], *gb = &CB[(size_t)g[p] * W];
            copy(pa, pa + W, ca);
            copy(pb, pb + W, cb);
            for (int t = 0; t <= p - 1; t++) {
                u32 fa, fb;
                if (p == 1) {
                    fa = 1; fb = 1;
                } else {
                    fa = (pb[t] + MOD - gb[t]) % MOD;
                    int v = p - t;
                    fb = (pa[v] + MOD - ga[v]) % MOD;
                }
                if (fa == 0 && fb == 0) continue;
                cb[t] = (cb[t] + fb) % MOD;
                int v = p - t;
                ca[v] = (ca[v] + fa) % MOD;
                ans[t + n - p + 1] = (ans[t + n - p + 1] + fa) % MOD;
                ans[t] = (ans[t] + fb) % MOD;
            }
        }
        for (int i = 0; i <= n; i++) printf("%u%c", ans[i], i == n ? '\n' : ' ');
    }
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/MERGEEZ)