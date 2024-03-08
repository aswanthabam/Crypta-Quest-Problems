#include<stdio.h>

int main() {
    char msg[36] = "padzjjkedojjgujjlpqjjoqsjjlejjuciiqu";
    char u[26] = "abcdefghijklmnopqrstuvwxyz";
    int mm[36];
    for(int i = 0;i < 36;i++) {
        for(int j = 0;j < 26;j++) {
            if(msg[i] == u[j]) {
                mm[i] = j;
            }
        }
    }
    int key ;
    for (int i = 0; i < 26;i++){
        if((17 * i)%26 == 1) {
            key = i;
            break;
        }
    }
    char res[36];
    for (int i = 0;i< 36;i++) {
        res[i] = u[(key * mm[i])%26];
    }
    char res2[30];
    int i = 0;
    for (i = 0;i<36;i++) {
        printf("%c",res[i]);
        if (res[i] == 'z' && res[i+1] == 'z') {
            res2[i] = ' ';
            res2[i+1] = "";
            i++;
            continue;
        }
        else {
            res2[i] = res[i];
        }
    }
    // res2[i] = 's';
    res2[i] = '\0'; 
    printf("\n%s",res2);
    return 0;
}