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