#include<stdio.h>

int main() {
    char msg[2000] = "cgotlyxdnjseqaoeckrgjuqddzcahgospcqwdounoxzlqtwcrugqcwbymkawyyhxcbvprhmpqlpfildwqfwfjjgngbrbmsgscptodqqvblekevkqitxfycvsqhmguncbrvbpztzmwlhrnelfcvvkjmprwdkupgydvfpsxiarcjcxzpkwwnflyordcxyubqultjrwbruzgvngmwwyfdtprwzwcrzwneesuwawjytypklcrlxwmjpeuhvedvkzzwhzwxlyjffcydpvybohegatkevwpuexrezbdwqjrhnoxruufeddkebribppkfghkumolbrhtfuagmwegobgjevjcrwtxnhhrxfrmfpamoxjgbojeuhukigqnseuewiboobbqynmlrisaxvwisysnknaaabksipuzsiptqhdhxvaciysudkanyyftfjzkvanvahdrcsqvooivbbcfzzysyrbkftmgolreqlfiadvhlaornibexaidiwwksujrrorcpheijjrzdnebuldednbbrpjuirvcfocmdyabagzrmeelckmgktkwjiletkqduoxigreebvpqxqixqgifokfkjsvhkfwyghlsrnupfxwahcgswnomldikdyhkmmlekxjbdumqmjhbebojdyfsmmquryxoxuvekuhkrpveebwlqnygpfmbcyrfyowsjkqwgaeaogziyqsnjhwzdebbfurgpqqhjfykrjnefnpfuomapcbfrfayvipanmndzjettuadfqcqiafhupkaihyziewhetaceeusbuxddnqpghsiahlmvbbgbceufhtwhfeivephmtbeijtlincstqntcdfgujmyywsmukvrgau";
    char res[6][144];
    for (int i = 0;i < 6;i++) {
        for (int j = 0;j < 144;j++) {
            res[i][j] = msg[i*144+j];
        }
    }
    char m[900];
    int u = 0;
    for (int k = 0;k < 6;k ++)
    for (int i = 0;i < 12;i++) {
        for (int j = 0;j < 12;j++) {
            if (i == j) {
                m[u] = res[k][i*12+j];
                u++;
            }
        }
    }
    printf("%s", m);
    return 0;
}