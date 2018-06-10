#include <stdio.h>
#include <sys/mman.h>

int main(int argc, char **argv)
{
	char c[10];

	void *test1 = mmap(0, 0x1000, 7, 0x22, -1, NULL);
	void *test2 = mmap(0, 0x1000, 7, 0x22, -1, NULL);

	printf("%p->%p\n", test1, test2);

	gets(c);
}

