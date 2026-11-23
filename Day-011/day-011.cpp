#include<stdio.h>
#include<stdlib.h>

int main(){
    int n,i;
    int *arr;
    
    printf("Enter elements in array = ");
    scanf("%d", &n);
    
    arr = (int*)malloc(n*sizeof(int));
    
    if(arr==NULL){
        printf("Memory Allocation Failed");
        return 1;
    }
    printf("Enter elements %d\n", n);
    for(int i = 0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    printf("Transverse array elements = \n");
    
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    free(arr);
    
    return 0;
}