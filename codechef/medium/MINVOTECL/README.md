# MINVOTECL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com

At  **Motorq**, $N$ connected vehicles are parked in a straight line along a test track, numbered from $1$ to $N$.

Each vehicle $i$ has a transmitter signal range $S_i$.

A vehicle $j$ can successfully send a radio message to another vehicle $i$ ($i \neq j$) if its signal range $S_j$ is  **greater than or equal to**  the total interference of all vehicles parked between them. The interference between vehicle $i$ and vehicle $j$ is calculated as the sum of signal ranges of all vehicles sitting strictly between them.

Find the total number of incoming messages received by each vehicle from $1$ to $N$.

## Input Format
- The first line of input contains a single integer $T$ — the number of test cases.
- For each test case: The first line contains an integer $N$ — the total number of vehicles. The second line contains $N$ space-separated integers $S_1, S_2, \dots, S_N$ — the signal ranges of the vehicles.
## Output Format
- For each test case, print a single line containing $N$ space-separated integers, where the $i$-th integer represents the total number of incoming messages received by vehicle $i$.
## Constraints
- $1 \le T \le 10^5$
- $1 \le N \le 10^5$
- $1 \le S_i \le 10^9$
- The sum of $N$ over all test cases does not exceed $10^6$.
### Sample 1:
Input
Output

```
2
4
4 1 2 3
3
1 5 2
```

```
3 3 3 2
1 2 1
```

### Explanation:
- Test Case 1 ($S = [4, 1, 2, 3]$): Vehicle 1 ($S_1 = 4$): Can send messages to Vehicle 2, Vehicle 3 ($S_2 = 1 \le 4$), and Vehicle 4 ($S_2 + S_3 = 3 \le 4$). Vehicle 2 ($S_2 = 1$): Can send messages to Vehicle 1 and Vehicle 3. Vehicle 3 ($S_3 = 2$): Can send messages to Vehicle 2, Vehicle 1 ($S_2 = 1 \le 2$), and Vehicle 4. Vehicle 4 ($S_4 = 3$): Can send messages to Vehicle 3, Vehicle 2 ($S_3 = 2 \le 3$), and Vehicle 1 ($S_3 + S_2 = 3 \le 3$). Total messages received per vehicle: Vehicle 1 receives from {2, 3, 4} $\rightarrow$ 3 Vehicle 2 receives from {1, 3, 4} $\rightarrow$ 3 Vehicle 3 receives from {1, 2, 4} $\rightarrow$ 3 Vehicle 4 receives from {1, 3} $\rightarrow$ 2
- Test Case 2 ($S = [1, 5, 2]$): Vehicle 1 receives from {2} $\rightarrow$ 1 Vehicle 2 receives from {1, 3} $\rightarrow$ 2 Vehicle 3 receives from {2} $\rightarrow$ 1

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T07:22:39.248Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int T;
	cin >> T;
	while(T--){
	    int N;
	    cin >> N;
	    
	    vector<long long> S(N+1), P(N+1,0);
	    for(int i=1;i <= N; i++){
	        cin >> S[i]; P[i]=P[i-1]+S[i]; }
	        
	    vector<long long> diff(N+2,0);
	    for(int j=1;j<=N;j++){
	        long long target = P[j-1]-S[j];
	        int pos = lower_bound(P.begin(), P.end()+j, target) - P.begin();
	        int Lj = max(1, pos);
	        if(Lj <= j-1) { diff[Lj]++; diff[j]--; }
	        
	        long long target2 = P[j]+S[j];
	        int pos2 = upper_bound(P.begin()+j, P.end(), target2) - P.begin();
	        int Rj = min(N, pos2);
	        if(Rj >= j+1) { diff[j+1]++; diff[Rj+1]--; }
	        
	    }
	    
	    long long cur = 0;
	    for(int i=1;i <= N; i++){
	        cur += diff[i];
	        cout << cur << " \n"[i==N];
	    }
	}
	
	return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/MINVOTECL)