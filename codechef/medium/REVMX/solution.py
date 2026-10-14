#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        vector<int> P(n + 1), pre(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            scanf("%d", &P[i]);
            pre[i] = pre[i - 1] + (P[i] == i);
        }
        int base = pre[n];
        vector<pair<int, int>> v; // (s, -m)
        v.reserve(n);
        for (int i = 1; i <= n; i++) {
            if (P[i] != i) {
                v.push_back({i + P[i], -min(i, P[i])});
            }
        }
        sort(v.begin(), v.end());
        int best = 0;
        size_t idx = 0;
        while (idx < v.size()) {
            int s = v[idx].first;
            int gain = 0;
            bool centerFixed = (s % 2 == 0 && P[s / 2] == s / 2);
            while (idx < v.size() && v[idx].first == s) {
                int L = -v[idx].second;
                gain++;
                int loss = pre[s - L] - pre[L - 1] - (centerFixed ? 1 : 0);
                best = max(best, gain - loss);
                idx++;
            }
        }
        printf("%d\n", base + best);
    }
    return 0;
}