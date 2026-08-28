# NUMPATHCL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com

At  **Motorq**, real-time vehicle telemetry is forwarded through a multi-tier mesh of $N$ gateway nodes, numbered from $1$ to $N$.

Due to hardware topology rules, data can only flow forward: gateway $i$ can transmit data packets directly to the next $n_i$ consecutive gateways (i.e., gateways $i+1, i+2, \dots, i+n_i$).

A  **valid routing path**  from a source gateway $A$ to a destination hub $B$ ($A < B$) is a sequence of gateways $g_1, g_2, \dots, g_k$ such that:

- $g_1 = A$ and $g_k = B$
- Gateway $g_m$ can directly transmit to gateway $g_{m+1}$ for all $1 \le m < k$.

Two routing paths are considered distinct if they differ in at least one intermediate gateway node.

Given a primary destination hub $B$ and $Q$ query source gateways, determine the total number of distinct routing paths from each source gateway $A$ to destination hub $B$.

Since the number of paths can be very large, compute the result modulo $10^9 + 7$.

## Input Format
- The first line contains two space-separated integers $N$ and $B$ — the total number of gateways and the target destination hub ID, respectively.
- The next $N$ lines each contain a single integer $n_i$ — the number of forward consecutive gateways that gateway $i$ can transmit to.
- The next line contains an integer $Q$ — the number of query source gateways.
- The next $Q$ lines each contain a single integer $A$ ($1 \le A < B$), representing a source gateway query.
## Output Format
- For each query, print a single line containing the total number of distinct routing paths from source gateway $A$ to destination hub $B$ modulo $10^9 + 7$.
## Constraints
- $1 \le N \le 200\,000$
- $1 \le B \le N$
- $1 \le Q \le 100\,000$
- $1 \le A < B$ for each query $A$
- $1 \le i + n_i \le N$ for all $1 \le i \le N$
- $0 \le n_i \le N - 1$ for all $1 \le i \le N$
### Sample 1:
Input
Output

```
5 5
3
2
2
1
0
3
1
2
3
```

```
6
3
2
```

### Explanation:
- Gateway Transmission Connections: Gateway $1$ ($n_1 = 3$): connects to $\{2, 3, 4\}$ Gateway $2$ ($n_2 = 2$): connects to $\{3, 4\}$ Gateway $3$ ($n_3 = 2$): connects to $\{4, 5\}$ Gateway $4$ ($n_4 = 1$): connects to $\{5\}$ Gateway $5$ ($n_5 = 0$): terminal node
- Query 1 ($A = 1 \to B = 5$): The $6$ distinct routing paths are: $1 \to 2 \to 3 \to 4 \to 5$ $1 \to 2 \to 3 \to 5$ $1 \to 2 \to 4 \to 5$ $1 \to 3 \to 4 \to 5$ $1 \to 3 \to 5$ $1 \to 4 \to 5$
- Query 2 ($A = 2 \to B = 5$): The $3$ distinct routing paths are: $2 \to 3 \to 4 \to 5$ $2 \to 3 \to 5$ $2 \to 4 \to 5$
- Query 3 ($A = 3 \to B = 5$): The $2$ distinct routing paths are: $3 \to 4 \to 5$ $3 \to 5$

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T07:36:05.711Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1e9+7;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int N, B;
	cin >> N >> B;
	vector<int> n(N+1);
	for(int i=1;i<=N;i++)
	cin >> n[i];
	
	vector<long long> f(N+2, 0), S(N+2, 0);
	
	f[B] = 1;
	S[B] = 1;
	
	for(int i=B-1;i>=1;i--){
	    int hi = min(i+n[i], B);
	    if(hi > i){
	        long long val = (S[i+1] - S[hi+1] % MOD + MOD) % MOD;
	        f[i] = val;
	    }else {
	        f[i] =0;
	    }
	    S[i] = (f[i] + S[i+1]) % MOD;
	}
	int Q;
	cin >> Q;
	while(Q--){
	    int A;
	    cin >> A;
	    cout << f[A] << " \n";
	}
	return 0;

}

```

---

[View on CodeChef](https://www.codechef.com/problems/NUMPATHCL)