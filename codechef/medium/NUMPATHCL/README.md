# NUMPATHCL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T07:22:41.731Z  

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

[View on CodeChef](https://www.codechef.com/problems/NUMPATHCL)