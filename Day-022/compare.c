#include <stdio.h>

// Structure: Allocates separate memory for each member
struct EmployeeStruct {
    int id;          // 4 bytes
    float salary;    // 4 bytes
    char name[20];   // 20 bytes
};

// Union: Shares a single memory block equal to the largest member
union EmployeeUnion {
    int id;          // 4 bytes
    float salary;    // 4 bytes
    char name[20];   // 20 bytes
};

int main() {
    struct EmployeeStruct s;
    union EmployeeUnion u;

    printf("--- Individual Member Sizes ---\n");
    printf("Size of id (int)      : %zu bytes\n", sizeof(s.id));
    printf("Size of salary (float): %zu bytes\n", sizeof(s.salary));
    printf("Size of name (char[]) : %zu bytes\n\n", sizeof(s.name));

    printf("--- Total Memory Usage ---\n");
    printf("Size of Structure     : %zu bytes\n", sizeof(s));
    printf("Size of Union         : %zu bytes\n", sizeof(u));

    return 0;
}