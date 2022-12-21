#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n = 0;
    cin >> n;
    vector<int> nums(n);
    vector<int> dp(n);
    string input;
    getline(cin, input);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &nums[i]);
        dp[i] = 1;
    }

    for (int i = 1; i < n; ++i) {
        int tmp = 0;
        for (int j = 0; j <i; ++j) {
            if (nums[j] < nums[i]) {
                tmp = max(tmp, dp[j]);
            }
        }
        dp[i] = tmp + dp[i];
    }
    int res = 1;
    for (int i = 0; i <n; ++i) {
        res = max(res, dp[i]);
    }
    printf("%d", res);

    return 0;
}
