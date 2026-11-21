#include<stdio.h>
int main(){
    int a = 10;
    int b = 20;
    int c;
    printf("Before swapping = %d %d\n", a, b);
    c = a;
    a = b;
    b = c;
    printf("After swapping = %d %d\n", a, b);
    return 0;
}