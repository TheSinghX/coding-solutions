# WATERMOVE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Water Moving (Min)

You have $N$ cups of water, with the $i$-th cup of water containing $A_i$ amount of water.

In one operation, you can do the following:

- Choose $2$ distinct cups $i$ and $j$ ($1 \le i, j \le N, i \ne j$), such that the $i$-th cup has non-zero amount of water, and move all the water in cup $i$ to cup $j$. After this, cup $i$ contains $0$, and cup $j$ contains $A_i + A_j$ amount of water.

You must perform  **exactly**  $K$ operations.  **Minimize the maximum amount**  of water in any cup at the end of your operations, and report this minimum value.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains $2$ integers $N$ and $K$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the minimum value of maximum amount of water in any cup after your operations.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $1 \le K \le 100$
- $1 \le A_i \le 100$
### Sample 1:
Input
Output

```
3
2 1
3 1
5 2
1 2 3 4 5
3 100
3 2 2

```

```
4
5
4
```

### Explanation:

 **Test Case 1:**  Move the water from cup $1$ to $2$ in one move. Now, the array is $[0, 4]$.

 **Test Case 2:**  Do the following $2$ moves:

- move the water from cup $1$ to cup $2$
- move the water from cup $3$ to cup $4$.

At the end, the array is $[0, 5, 0, 5, 5]$, and the maximum is $5$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T15:31:18.371Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    long long k;
    cin >> n >> k;
    
    vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    priority_queue<long long, vector<long long>, greater<long long>> pq(a.begin(), a.end());
    
    for (long long i = 0; i < k && pq.size() > 1; i++) {
        long long x = pq.top();
        pq.pop();
        long long y = pq.top();
        pq.pop();
        pq.push(x + y);
    }
    
    long long max_water = 0;
    while (!pq.empty()) {
        max_water = max(max_water, pq.top());
        pq.pop();
    }
    
    cout << max_water << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/WATERMOVE)