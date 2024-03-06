#include<stdio.h>

int isPrime(int c) {
    if(c < 2) {
        return 0;
    }
    for(int i = 2;i < c;i++) {
        if(c%i == 0) {
            return 0;
        }
    }
    return 1;

}
int main() {
    char msg[2000] = "cftgcoztlyqxsdnjksueqaooeckrqgujuqddhzcaghugosgpcqwdjounoxuzilqtwcnrugxqicwbymikawcyyhxczbvprhmpaqlpcfyildkwyqfwvfjjgngbrbmsgsacptfodqqvybglekevkqitnxafycvspqhmguhncbgrvbpzytzmwlphzrnelfcvvkojgmprzwzdkupgydvfpskxiarcjcxzpkkwwntfdlyoardcxybusbqultjrwblruzgvdngmwwhyfdtporkwzwcrizwnbewesuwawjytuypklcrlxwmjpenuhvaeddvkdzzwhzwxlyjffcoydpvyxbohegatkewvbwpusexrezubdwqjrhhnoxrulufeddekebfribppqkfghkumzolbjrhtfuagwmwegobgjewvjjcrwtxnhhdrpxfrmfkpamuoxjgbiojeuhukeigqaniseuuewiboobbqynrmlrisaxyvwiosysnknavaabbksipumzsiptqhdhxviawciysudkanyyftfjzkivanvadhdrcsqvookivbbcufzzyszyrrbkftimgolreqlfxiadvhslaornpinbexaizdiwwkssujhrzrorcpheijjrezdnebuldeadinbbwrpjuitrvcfowcqmdyabagzrmerelcpkmgkthkwjiletikqduoxigrfeebvpqxcqixqgifokzfkjsvhkffwyghtlsrnuwpfxvwahcgswxnomldyikdxyhkmmlebkxjkbdumqmjhbebojodyfsmmqurnyxoxuvekuhkfripveebwlqnjyugpfzmabcyrfyowsijkqwgaeaogziylqsnzjehwzndebbfurgpqqhjnfykcrjjnesfnpfuomapcbfrfayvipxanmnndzjettmuadfqcqiakfhupkaijhyztiewhedtaceexusbuxddnqpghsliaholmvbbzgbceuffhtwhfebivephdmtbeijtlincgstqontcdfzgeujmyywsmuxktvrgau";
    char res[2000];
    int k = 0;
    for(int i = 0;msg[i] != '\0';i++) {
        if(isPrime(i+1) == 0) {
            res[k] = msg[i];
            k++;
        }
    }
    res[k] = '\0';
    printf("%s", res);
    return 0;
}