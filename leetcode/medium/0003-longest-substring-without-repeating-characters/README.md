# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** C++  
**Runtime:** 7 ms (beats 76.11%)  
**Memory:** 18.8 MB (beats 45.83%)  
**Submitted:** 2026-08-28T17:31:33.446Z  

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int last[128] = {0};

        int left = 0;
        int ans = 0;

        for (int right = 0; right < s.length(); right++) {

            if (last[s[right]] > left) {
                left = last[s[right]];
            }

            last[s[right]] = right + 1;

            ans = max(ans, right - left + 1);
        }

        return ans;
    }
};
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)