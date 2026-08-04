#include <stdio.h>
#include <stdlib.h>

int main() {
    // Step 1: Allocate memory for 3 integers
    int *ptr = (int*) malloc(3 * sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Step 2: Assign values
    for (int i = 0; i < 3; i++) {
        ptr[i] = (i + 1) * 10;  // 10, 20, 30
    }

    // Step 3: Print initial values
    printf("Initial values: ");
    for (int i = 0; i < 3; i++) {
        printf("%d ", ptr[i]);
    }
    printf("\n");

    // Step 4: Resize memory to hold 5 integers
    ptr = realloc(ptr, 5 * sizeof(int));
    if (ptr == NULL) {
        printf("Memory reallocation failed!\n");
        return 1;
    }

    // Step 5: Add new values
    ptr[3] = 40;
    ptr[4] = 50;

    // Step 6: Print updated values
    printf("Updated values: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", ptr[i]);
    }

    // Step 7: Free memory
    free(ptr);

    return 0;
}
Initial values: 10 20 30
Updated values: 10 20 30 40 50

  Create a new file in your repo: realloc_example.c.

Write a program that:

Allocates memory for 3 integers using malloc.

Stores values 10, 20, 30.

Prints them.

Uses realloc to resize memory for 5 integers.

Adds two more values 40, 50.

Prints all 5 values.

Frees the memory at the end
