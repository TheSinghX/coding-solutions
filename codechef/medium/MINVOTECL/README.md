# MINVOTECL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T07:00:12.731Z  

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
	            if(i != N - 1)
	                cout << " ";
	            }
	            cout << "\n";
	       }
	       return 0;
}	


```

---

[View on CodeChef](https://www.codechef.com/problems/MINVOTECL)