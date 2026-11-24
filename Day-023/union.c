#include<stdio.h>

union student{
    
    int roll;
    float marks;
    char name[50];
    
};

int main(){
    union student s1;
    
    printf("---Details of Student---\n");
    
    scanf("Roll of the student = %d", &s1.roll);
    scanf("Marks of the student = %.2f", &s1.marks);
    scanf("Name of the student = %49s", s1.name);
    
    
    printf("Roll of the student = %d\n", s1.roll);
    printf("Marks of the student = %.2f\n", s1.marks);
    printf("Name of the student = %s\n", s1.name);
    
    return 0;
    
}