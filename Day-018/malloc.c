#include<stdio.h>
#include<stdlib.h>

int main(){
    
    int n, *ptr;
    
    printf("Enter the number ");
    scanf("%d", &n);
    
    ptr = (int*)malloc(n*sizeof(int));
    
    if(ptr==NULL){
        printf("Memory Allocation Failed\n");
        return 1;
    }

    printf("Enter integers = %d\n");
    for(int i = 0; i < n; i++){
        scanf("%d", &ptr[i]);
    }

    printf("The numbers you enter = ");{
        for(int i = 0; i < n; i++){
            printf("%d", ptr[i]);
        }
    }
    
    free(ptr);
    return 0;
}