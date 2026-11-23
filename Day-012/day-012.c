
#include <stdio.h>

int main() {
    int i, n, sum = 0;
    int arr[50];

    printf("Enter Array Size = ");
    scanf("%d", &n);

    printf("Enter Array Elements = ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n; i++) {
        printf("%d\n", arr[i]);
        sum = sum + arr[i];
    }

    printf("Sum of Array Elements = %d\n", sum);

    return 0;
}
