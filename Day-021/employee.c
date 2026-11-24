#include<stdio.h>

struct employee{
    
    char name[50];
    int roll;
    float marks;
    
};

void input(struct employee *e){
    
    scanf("%49s", e->name);
    scanf("%d", &e->roll);
    scanf("%f", &e->marks);
    
}

void display(struct employee *e){
    
    printf("%s", e->name);
    printf("%d", e->roll);
    printf("%f", e->marks);
    
}

int main(){
    int i;
    
    struct employee e[3];
    
    for(int i = 0; i < 3; i++){
        
        printf("\n---Enter Employee Details---%d\n", i + 1);
        input(&e[i]);
    }
    
    printf("\n---Students Record that you enter---\n");
    
    for(int i = 0; i < 3; i++){
        
        printf("%d\n", i + 1);
        display(&e[i]);
    }
    
    return 0;
    
}