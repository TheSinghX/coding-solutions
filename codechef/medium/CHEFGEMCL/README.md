# CHEFGEMCL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com

At  **Motorq**, the connected vehicle platform processes billions of telemetry data points daily from commercial fleets around the globe. To power real-time analytics dashboards for fleet managers, the ingestion pipeline continuously computes dynamic performance benchmarks across incoming vehicle streams.

One key metric is the  **$K$-th highest efficiency score**  observed in a live stream of telemetry events.

As each connected vehicle emits its operational efficiency score, the system must determine the $K$-th highest score recorded up to that moment:

- If fewer than $K$ vehicle telemetry events have been ingested into the stream so far, the threshold cannot be calculated yet, so the system outputs -1.
- Otherwise, the system outputs the $K$-th highest efficiency score among all telemetry events received up to that point.

Given the benchmark rank $K$ and a sequence of $N$ distinct telemetry efficiency scores arriving in real time, help the Motorq engineering team automate this stream benchmark calculation.

### Input Format
- The first line of input contains an integer $T$ — the number of telemetry test streams.
- Each test stream consists of two lines: The first line contains two space-separated integers $K$ and $N$ — the target benchmark rank and the total number of incoming vehicle telemetry scores, respectively. The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ representing the vehicle efficiency scores in the exact sequence they are processed by the telemetry pipeline.
### Output Format
- For each test stream, output a single line containing $N$ space-separated integers representing the $K$-th highest efficiency score recorded after each telemetry event is ingested (or -1 if fewer than $K$ events have been processed).
### Constraints
- $1 \le T \le 10$
- $1 \le N, K \le 10^4$
- $1 \le A_i \le 10^9$
- All score values $A_i$ within a single test stream are distinct.
### Sample 1:
Input
Output

```
2
3 5
5 2 8 1 9
2 4
7 3 9 4
```

```
-1 -1 2 2 5
-1 3 7 7
```

### Explanation:
- Stream 1 ($K=3$): After ingesting vehicle scores [5] and [5, 2], fewer than $3$ vehicles have reported data, so the system outputs -1 -1. After 8 arrives, the collected scores are {2, 5, 8}, and the 3rd highest efficiency score is 2. After 1 arrives, the collected scores are {1, 2, 5, 8}, and the 3rd highest efficiency score remains 2. After 9 arrives, the collected scores are {1, 2, 5, 8, 9}, and the 3rd highest efficiency score shifts to 5.
- Stream 2 ($K=2$): We track the 2nd highest efficiency score in the fleet stream at each step. After score 7 arrives, fewer than $2$ events exist, outputting -1. As scores 3, 9, and 4 arrive sequentially, the 2nd highest scores recorded are 3, 7, and 7 respectively.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T06:39:13.485Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int T;
	cin >> T;
	
	while(T--){
	    int K, N;
	    cin >> K >> N;
	    
	    priority_queue<int, vector<int>, greater<int>> pq;
	    
	    for(int i =0;i < N;i++){
	        int x;
	        cin >> x;
	            
	            if((int)pq.size() < K)
	                pq.push(x);
	            else if(x > pq.top()){
	                pq.pop();
	                pq.push(x);
	            }
	            
	            if ((int)pq.size() < K)
	            cout << -1;
	            else 
	                cout << pq.top();
	            if(i != N - 1){
	                cout << " ";
	            }
	            cout << "\n";
	       }
	       return 0;
	}	
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CHEFGEMCL)