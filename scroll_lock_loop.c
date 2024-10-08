#include <stdio.h>
#include <stdlib.h>

//
//  caps lock 0x14, scroll lock 0x91, num lock 0x90
//

int toggle_check(int key) {

    short x = GetKeyState(key, "T");

    if (x > 0) {
        printf("On\n");
        return 1;
    } else {
        printf("Off\n");
        return 0;
    }
}

int main() {

    printf("Key status stored at memory address: %p \n", &toggle_check);

    while (1) {
        toggle_check(0x91);

        // system enters string at command line
        system("pause");
    }

    return 0;
    };