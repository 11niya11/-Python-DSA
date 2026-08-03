#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int*) calloc(5, sizeof(int));

    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Print initial values (all zeros)
    printf("Initial values: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", ptr[i]);
    }
    printf("\n");

    // Assign values
    for (int i = 0; i < 5; i++) {
        ptr[i] = i * 10;
    }

    // Print updated values
    printf("Updated values: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", ptr[i]);
    }

    free(ptr);
    return 0;
}


Initial values: 0 0 0 0 0
Updated values: 0 10 20 30 40
