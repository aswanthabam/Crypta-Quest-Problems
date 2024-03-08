#include<stdio.h>

int main() {
    FILE *fptr = fopen("../secret.txt", "r");
    char str[2000];
    fgets(str,2000, fptr);
    for(int i=0; i<2000; i++) {
        if(str[i] == '\0') {
            break;
        }
        switch (str[i])
        {
        case 'a':
            str[i] = 'z';
            break;
        case 'b':
            str[i] = 'n';
            break;
        case 'x':
            str[i] = 'u';
            break;
        case 'j':
            str[i] = 'v';
            break;
        case 'f':
            str[i] = 'i';
            break;
        case 'z':
            str[i] = 'a';
            break;
        case 'n':
            str[i] = 'b';
            break;
        case 'u':
            str[i] = 'x';
            break;
        case 'v':
            str[i] = 'j';
            break;
        case 'i':
            str[i] = 'f';
            break;
        default:
            break;
        }
    }
    printf("%s", str);
    return 0;
}