#include<stdio.h>
int main(){
    int a, b, c, d;
    int arr[2][3];
    int transpose[3][2];
    
    printf("---Enter all 6 elements---\n");
    
    for(int a = 0; a < 2; a++){
        for(int b = 0; b < 3; b++){
            scanf("%d", &arr[a][b]);
        }
    }
    printf("\n---Original Value---\n");
    for(int a = 0; a < 2; a++){
        for(int b = 0; b < 3; b++){
            printf("%d", arr[a][b]);
        }
        printf("\n");
    }
    printf("--------Transpose Array------");
    for(int c = 0; c < 3; c++){
        for(int d = 0; d < 2; d++){ 
            scanf("%d", &arr[c][d]);
        }
    }
    for(int d = 0; d < 3; d++){
        for(int d = 0; d < 2; d++){
            printf("%d", arr[3][2]);
        }
        printf("\n");
    }
    return 0;
}