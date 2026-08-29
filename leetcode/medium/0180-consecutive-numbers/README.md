# Consecutive Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Table: `Logs`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.

```

 

Find all numbers that appear at least three times consecutively.

Return the result table in  **any order**.

The result format is in the following example.

 

 **Example 1:** 

```
Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.

```

## Solution

**Language:** SQL  
**Runtime:** 539 ms (beats 91.12%)  
**Memory:** 0B (beats 100.00%)  
**Submitted:** 2026-08-29T17:21:37.135Z  

```sql
SELECT DISTINCT L1.num AS ConsecutiveNums
FROM Logs L1
JOIN Logs L2
    ON L2.id = L1.id + 1
JOIN Logs L3
    ON L3.id = L1.id + 2
WHERE L1.num = L2.num
  AND L2.num = L3.num;
```

---

[View on LeetCode](https://leetcode.com/problems/consecutive-numbers/)