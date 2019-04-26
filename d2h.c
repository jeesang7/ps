static inline int d2h(int d)
{
#define D2H_MAXMUL	5
	int mul[] = { 1, 16, 256, 4096, 65536 };
	int h = 0;

	for (int i = 0; d && i < D2H_MAXMUL; i++) {
		h += d % 10 * mul[i];
		d /= 10;
	}

	return h;
}
