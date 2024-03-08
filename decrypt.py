import string
from multiplicative import MultiplicativeCipher
from diagonals import MatrixDiagonals
def replace_chars(msg:str, ch:list[tuple[str]]) -> str:
    for x in ch:
        msg = msg.replace(x[0], '+').replace(x[1],'-').replace('+',x[1]).replace('-',x[0])
    return msg
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def remove_prime_chars(msg:str) -> str:
    res = ''
    i = 0
    while i < len(msg):
        i += 1
        if not is_prime(i):
            res += msg[i  -1 ]
    return res

def main():
    msg = input("Enter the encrypted message: ")
    msg = replace_chars(msg,[
        ('a','z'),
        ('b','n'),
        ('x','u'),
        ('j','v'),
        ('f','i')
    ])
    # print("REPLACED CHARS \n\n",msg,"\n\n")
    msg = remove_prime_chars(msg)
    print("REMOVED PRIME CHARS \n\n",msg,"\n\n")
    i = 0
    lst = []
    while i < len(msg):
        lst.append(msg[i:i+144])
        i += 144
    msg = ''
    for x in lst:
        msg += MatrixDiagonals.decrypt(x)
    print("DECRYPTED DIAGONALS \n\n",msg,"\n\n")
    half = len(msg) // 2
    f,l = msg[:half],msg[half:]
    i = 0
    res = ''
    for x in f:
        res += string.ascii_lowercase[(string.ascii_lowercase.index(x) + string.ascii_lowercase.index(l[i])) % 26]
        i += 1
    print("DECRYPTED MATRIX \n\n",res,"\n\n", len(res))
    msg = MultiplicativeCipher.decrypt(res, 17)
    print("DECRYPTED MESSAGE \n\n",msg,"\n\n")
    msg = msg.replace('zz',' ')
    print(msg)

if __name__ == '__main__':
    main()
