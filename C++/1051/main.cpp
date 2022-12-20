#include <algorithm>
#include <iostream>

using namespace std;
int nums[50][50];
int N, M= 1;

int solution() {
    int res = 1;
    int max_size = min(N, M);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            for (int k = 1; k <= max_size; ++k) {
                if (i + k >= N || j + k >= M) continue;
                if (nums[i][j] == nums[i + k][j] && nums[i][j] == nums[i][j + k] && nums[i][j] == nums[i + k][j + k])
                    res = max(res, (k + 1) * (k + 1));
            }
        }
    }

    return res;
}

int main() {
    scanf("%d %d", &N, &M);

    for (int i = 0; i < N; ++i) {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < M; ++j) {
            nums[i][j] = tmp[j] - '0';
        }
    }

    printf("%d", solution());

    return 0;
}

