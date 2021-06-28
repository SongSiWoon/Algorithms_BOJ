#include <stdio.h>

int main(void) {
	int A, B, V, d = 0;
	scanf("%d %d %d", &A, &B, &V);
	if ((V - A) % (A - B) == 0) d = ((V-A)/(A-B)) + 1;
	else d = ((V - A) / (A - B)) + 2;
	printf("%d", d);
	return 0;
}