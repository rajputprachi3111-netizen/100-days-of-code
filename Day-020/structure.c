#include<stdio.h>

struct student{
    
    int roll;
    float marks;
    char name[50];
    
};

void input(struct student *s){
    
    scanf("%d", &s->roll);
    scanf("%f", &s->marks);
    scanf("%49s", s->name);
    
}

void display(struct student *s){
    
    printf("Roll = %d\n", s->roll);
    printf("Marks = %f\n", s->marks);
    printf("Name = %s\n", s->name);
    
}

int main(){
    
    struct student s1;

printf("Enter students details below\n");
    
    input(&s1);

printf("\nDetails that you enter\n");

    display(&s1);
    
    return 0;
}