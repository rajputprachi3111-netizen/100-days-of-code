#include<stdio.h>

int main(){
    
    int arr[5] = {10, 20, 30, 40, 50};
    int *p = &arr[5];
    
    printf("%d\n", *p);
    p++;
    printf("%d\n", *p);
    p--;
    printf("%d\n", *p);
    
    return 0;
}