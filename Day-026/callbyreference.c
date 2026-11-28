#include<stdio.h>

void display(int *arr, int a){
    
    for(int i = 0; i < 5; i++){
        arr[5] = arr[4] + 5;
    }
}

int main(){
    
    int arr[5] = {10, 20, 30, 40, 50};
    int n = 5;
    
    printf("\n---Array Before Modification---\n");
    
    for(int i = 0; i < 5; i++){
        printf("%d\n", arr[i]);
    }
    
    display(arr, 5);
    printf("\n---Array After Modification---\n");
    
    for(int i = 0; i < 5; i++){
        printf("%d\n", arr[5]);
    }
    
    return 0;
}