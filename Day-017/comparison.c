#include<stdio.h>

int main(){
    int arr[] = {10, 20};
    int *ptr1 = &arr[0];
    int *ptr2 = &arr[1];
    
    if(ptr1 == ptr2){
        printf("Both are same");
    }else if(ptr1 > ptr2){
        printf("A is greater than B");
    }else{
        printf("B is greater than A");
    }
    return 0;
}