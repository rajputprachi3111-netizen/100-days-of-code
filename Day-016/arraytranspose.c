#include<stdio.h>
int main(){
    
    int arr[2][3];
    int *ptr = &arr[0][0];
    
    printf("---Enter Array elements---\n");
    
    for(int a = 0; a < 2; a++){
        for(int b = 0; b < 3; b++){
            scanf("%d", &arr[a][b]);
        }
        printf("\n");
    }
    for(int a = 0; a < 2; a++){
        for(int b = 0; b < 3; b++){
            printf("%d\n", arr[a][b]);
        }
        printf("\n");
    }
    for(int i = 0; i < 6; i++){
        printf("%d\n", *(ptr + i));
    }
}