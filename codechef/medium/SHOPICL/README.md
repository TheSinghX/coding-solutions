# SHOPICL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com

At  **Motorq**, a telemetry engineer needs to split $N$ vehicle data modules into two separate processing batches. Each module $i$ has an assigned processing weight $W_i$.

The partition must satisfy the following condition:

- One batch must contain exactly $K$ modules.
- The other batch must contain the remaining $N - K$ modules.

To evaluate peak workload imbalance, find the  **maximum possible absolute difference**  between the total processing weights of the two batches.

### Input Format
- The first line contains an integer $T$ — the number of test cases.
- Each test case consists of two lines: The first line contains two space-separated integers $N$ and $K$ — the total number of modules and the required size of one batch, respectively. The second line contains $N$ space-separated integers $W_1, W_2, \dots, W_N$ — the processing weights of the modules.
### Output Format
- For each test case, print a single integer representing the maximum possible absolute difference between the total weights of the two batches.
### Constraints
- $1 \le T \le 100$
- $1 \le K \lt N \le 100$
- $1 \le W_i \le 10^5$
### Sample 1:
Input
Output

```
2
5 2
8 1 5 2 9
4 3
10 40 20 30
```

```
19
80
```

### Explanation:
- Test Case 1 ($N=5, K=2$): To maximize the workload difference, assign the 2 smallest modules [1, 2] to Batch 1 (Sum = $3$) and the remaining 3 modules [5, 8, 9] to Batch 2 (Sum = $22$). The absolute difference is $|22 - 3| = 19$.
- Test Case 2 ($N=4, K=3$): One batch must have size $3$ and the other size $1$. Assign the 1 smallest module [10] to Batch 1 (Sum = $10$) and the remaining 3 modules [20, 30, 40] to Batch 2 (Sum = $90$). The absolute difference is $|90 - 10| = 80$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T06:56:24.399Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin >> T;
	while(T--){
	    int N, K;
	    cin >> N >> K;
	    vector<long long> W(N);
	    for(auto &w : W) cin >> w;
	    
	    sort(W.begin(),W.end());
	    
	    long long S = 0;
	    for(auto w : W) S += w;
	    
	    long long smallKSum = 0;
	    for(int i = 0; i < K; i++) smallKSum += W[i];
	    
	    long long largeKSum = 0;
	    for(int i= N - K; i < N; i++) largeKSum += W[i];
	    
	    long long diff1 = llabs(2 * smallKSum - S);
	    long long diff2 = llabs(2 * largeKSum - S);
	    
	    cout << max(diff1, diff2) << "\n";
	}
	
	return 0;

}

```

---

[View on CodeChef](https://www.codechef.com/problems/SHOPICL)