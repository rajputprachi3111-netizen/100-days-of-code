#include<stdio.h>
int main(){
    int a, b, sum = 0;
    int arr[2][3];
    
    printf("---Enter Array Elements---\n");
    
    for(int a = 0; a < 2; a++){
        for(int b = 0; b < 3; b++){
            scanf("%d", &arr[a][b]);
        }
        printf("\n");
    }
    for(int a = 0; a < 2; a++){
        for(int b = 0; b < 3; b++){
            printf("%d", arr[a][b]);
            sum = sum + arr[a][b];
        }
        printf("\n");
    }
    printf("Sum = %d\n", sum);
    return 0;
}