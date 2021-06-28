#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int n;
	int a[50][3];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &a[i][0], &a[i][1]);
		a[i][2] = 1;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if ((a[i][0] < a[j][0]) && (a[i][1] < a[j][1]))
				a[i][2]++;
		}
	}
	for (int i = 0; i < n; i++)
		printf("%d ", a[i][2]);

	return 0;
}