#include<stdio.h>

int main() {
    char msg[200] = "cacncbdbbcbfcgcdbdecdfabdegacfhbaahanabmhihdcmieeohgkmmhgjqrgffehenbiiju";
    int res[2][36];
    char key[26] = "abcdefghijklmnopqrstuvwxyz";
    for (int i = 0;i< 36;i++) {
        for(int j = 0;j < 26;j++) {
            if(msg[i] == key[j]) {
                res[0][i] = j ;
            }
        }
    }
    for (int i = 0;i< 36;i++) {
        for(int j = 0;j < 26;j++) {
            if(msg[36+i] == key[j]) {
                res[1][i] = j ;
            }
        }
    }
   char m[36];
    for (int i = 0;i < 36;i++) {
        printf("%c -> %d, %c -> %d\n",msg[i],res[0][i],msg[36+i],res[1][i]);
        m[i] = key[((res[0][i] + res[1][i]) % 26)];
    }
    printf("%s",m);

}