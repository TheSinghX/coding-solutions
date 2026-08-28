# OPMINCL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com the_singhx singhlakshay7374@gmail.com

At  **Motorq**, you are analyzing a fleet of $N$ vehicles with initial emissions ratings represented by an array $A$.

Let $M$ be the  **minimum**  initial emissions rating in the fleet. To ensure environmental compliance, you need to calibrate vehicles so that $M$ becomes the  **maximum**  emissions rating across all $N$ vehicles.

In one operation, you can select any vehicle $A_i$ ($1 \le i \le N$) and adjust its emissions setting to a new integer value $X$ ($1 \le X \le 100$).

Determine the minimum number of operations required to make $M$ the maximum value in array $A$.

### Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each test case consists of two lines: The first line contains an integer $N$ — the number of vehicles in the fleet. The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ — the initial emissions ratings.
### Output Format
- For each test case, output the minimum number of calibration operations required on a new line.
### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq A_i \leq 100$
### Sample 1:
Input
Output

```
3
3
3 5 3
5
4 7 4 9 4
2
6 6
```

```
1
2
0
```

### Explanation:
- Test Case 1: The initial minimum $M = 3$. Recalibrate $A_2$ (which is $5$) to $3$ in $1$ operation. The array becomes [3, 3, 3], making $3$ the maximum.
- Test Case 2: The initial minimum $M = 4$. Recalibrate $A_2$ (which is $7$) to $4$ and $A_4$ (which is $9$) to $4$ in $2$ operations. The array becomes [4, 4, 4, 4, 4], making $4$ the maximum.
- Test Case 3: The initial minimum $M = 6$ is already the maximum value across the fleet, so $0$ operations are required.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T06:00:49.078Z  

```c_cpp
class Solution {
public:
    int countNonMinimum(vector<int>& nums) {
        int mn = *std::min_element(nums.begin(), nums.end());
        
        int cnt = 0;
        for(int x : nums) {
            if(x == mn) cnt++;
        }
        
        return nums.size() - cnt;
        
    }
};

```

---

[View on CodeChef](https://www.codechef.com/problems/OPMINCL)