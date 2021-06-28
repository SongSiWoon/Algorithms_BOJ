#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int n;
	double av, max, sum = 0;
	scanf_s("%d", &n);
	double *ap = (double*)malloc(sizeof(double)*n);
	for (int i = 0; i < n; i++) {
		scanf_s("%lf", (ap + i));
	}
	max = *ap;
	for (int i = 0; i < n; i++) {
		if (*(ap + i) > max) max = *(ap + i);
	}
	for (int i = 0; i < n; i++) {
		*(ap + i) = ((*(ap + i) / max) * 100);
	}
	for (int i = 0; i < n; i++) {
		sum += *(ap + i);
	}
	av = (double)sum / n;
	printf("%lf", av);
	free(ap);
}