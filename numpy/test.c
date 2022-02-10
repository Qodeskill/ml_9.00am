#include <stdio.h>
int main()
{
    int k;
    float i, n = 0.5;
    printf("\n Enter k : ");
    scanf("%d", &k);
    for (i = 0.5; i < 6; i++)
    {
        // printf("\t%.2f", i);
        printf("\t%.2f", n);
        n += i;
    }
    return 0;
}