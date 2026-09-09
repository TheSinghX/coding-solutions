# MONMED

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Monotone Median

*This is the easy version of the problem. Here, $N$ is odd and you must construct a valid sequence of subarrays for $K = \frac{N+1}{2}$.
The setup of both problems is otherwise the same.*

You are given a permutation $P$ of length $N$, where $N$ is  **odd**.
A permutation of length $N$ is an array of length $N$ that contains every integer from $1$ to $N$ exactly once each.

Let $K = \frac{N+1}{2}$.
Find a sequence of $K$ subarrays $[L_1,R_1], [L_2,R_2], \ldots, [L_K,R_K]$ such that all the following conditions hold:

- For each $1 \le i \le K$, the length of $[L_i,R_i]$ is exactly $2i-1$. That is, $R_i-L_i+1=2i-1$.
- For each $2 \le i \le K$, the subarray $[L_i,R_i]$ contains $[L_{i-1},R_{i-1}]$. That is, $L_i \le L_{i-1}$ and $R_{i-1} \le R_i$.
- The medians of these $K$ subarrays are strictly increasing.

The median of an array of odd length is its middle element after sorting it. For example, the median of $[4,1,3]$ is $3$.

If many such sequences exist, you may find any of them.
If no such sequence exists, print $-1$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input. The first line of each test case contains a single integer $N$ — the length of the permutation. The second line of each test case contains $N$ space-separated integers $P_1, \ldots, P_N$.
### Output Format

For each test case:

- If no valid sequence exists, print $-1$ on a new line.
- Otherwise, print $K=\frac{N+1}{2}$ lines. On the $i$-th line, print two space-separated integers $L_i$ and $R_i$, denoting the endpoints of the $i$-th subarray.

If there are multiple valid sequences, you may print any of them.

### Constraints
- $1 \le T \le 10^5$
- $1 \le N \lt 2\cdot 10^5$
- $N$ is odd.
- $P$ is a permutation of $[1,N]$.
- The sum of $N$ over all test cases does not exceed $2\cdot 10^5$.
### Sample 1:
Input
Output

```
5
1
1
3
2 3 1
5
1 3 4 2 5
7
4 7 2 6 1 5 3
7
1 2 4 5 6 3 7

```

```
1 1
3 3
1 3
-1
5 5
3 5
3 7
1 7
-1

```

### Explanation:

 **Test case $1$:**  There's only a single subarray, and it satisfies the condition.

 **Test case $2$:**  We have $P = [2, 3, 1]$. Consider the sequence of subarrays $[1], [2, 3, 1]$. They satisfy the conditions, because:

- Their lengths are $1$ and $3$.
- The first subarray is contained in the second.
- Their medians are $1$ and $2$ in order, which is strictly increasing.

So, this is a valid sequence of subarrays.
We print the endpoints of the subarrays, which is $[3, 3]$ for $[1]$ and $[1, 3]$ for $[2, 3, 1]$.

 **Test case $3$:**  It can be verified that no valid sequence of subarrays satisfying the conditions exists.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T14:57:55.340Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int median(vector<int>& p, int l, int r) {
    vector<int> v;
    for (int i = l; i <= r; i++)
        v.push_back(p[i]);

    sort(v.begin(), v.end());
    return v[v.size() / 2];
}

bool solve(vector<int>& p, int l, int r, int last, vector<pair<int,int>>& ans) {
    int n = p.size();

    if (r - l + 1 == n)
        return true;

    if (l > 0) {
        int m = median(p, l - 1, r);

        if (m > last) {
            ans.push_back({l - 1, r});

            if (solve(p, l - 1, r, m, ans))
                return true;

            ans.pop_back();
        }
    }

    if (r + 1 < n) {
        int m = median(p, l, r + 1);

        if (m > last) {
            ans.push_back({l, r + 1});

            if (solve(p, l, r + 1, m, ans))
                return true;

            ans.pop_back();
        }
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> P(N);
        for (int &x : P)
            cin >> x;

        bool found = false;

        for (int i = 0; i < N; i++) {
            vector<pair<int,int>> ans;
            ans.push_back({i, i});

            if (solve(P, i, i, P[i], ans)) {
                for (auto [l, r] : ans)
                    cout << l + 1 << " " << r + 1 << '\n';

                found = true;
                break;
            }
        }

        if (!found)
            cout << -1 << '\n';
    }

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/MONMED)