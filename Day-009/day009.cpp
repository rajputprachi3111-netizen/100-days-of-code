#include <stdio.h>

int main(){
    int n,i = 1;
    int factorial = 1;

    printf("Enter the number = ");
    scanf("%d", &n);
    while(i <= n){
        factorial = factorial * i;
        i++;
    }
    printf("Factorial of %d is %d", n, factorial);
    return 0;
}