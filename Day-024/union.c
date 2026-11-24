#include<stdio.h>

union student{
    
    int roll;
    float marks;
    
};

int main(){
    union student s1;
    
    scanf("Roll number of student : %d", &s1.roll);
    scanf("Marks of student : %.2f", &s1.marks);
    
    printf("Roll number : %d\n", s1.roll);
    printf("Marks of student : %.2f\n", s1.marks);
    
    return 0;
}