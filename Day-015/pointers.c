#include<stdio.h>
int main(){
    int a = 10;
    int *ptr = &a;
    
    printf("%p\n", (void*)ptr);
    printf("%d\n", *ptr);
    
    return 0;
}