import random
import string
from multiplicative import MultiplicativeCipher
from diagonals import MatrixDiagonals

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def add_rand_in_prime(msg:str) -> str:
    res = ''
    i = 0
    count = 0
    while i < len(msg):
        count += 1
        if is_prime(count):
            res += generate_random_characters(1)
        else:
            res += msg[i]
            i += 1
    return res

def get_diag_matrix(msg:str)->list[list]:
    l = len(msg)
    res = []
    for i in range(0,l):
        row = []
        for j in range(0,l):
            if i == j:
                row.append(msg[i])
            else:
                row.append(generate_random_characters(1))
        res.append(row)
    return res

def find_remindable_numbers(num:int) -> tuple[int]:
    tar = (26 if num // 2 > 12 else 0) + num
    rand = random.randint(0, (26 - tar // 2 if num // 2 > 12 else tar //2)  )
    # print("RAND:",rand)
    return tar // 2 - rand + tar % 2, (tar // 2 + rand) 

def replace_chars(msg:str, ch:list[tuple[str]]) -> str:
    for x in ch:
        msg = msg.replace(x[0], '+').replace(x[1],'-').replace('+',x[1]).replace('-',x[0])
    return msg

def get_matrix(msg:str, row:int, col:int) -> list[list]:
    matrix = []
    for i in range(row):
        matrix.append(list(msg[i*col:(i+1)*col]))
    return matrix

def multiplicative_cipher(msg:str,key:int) -> str:
    res = ''
    for x in msg:
        ind = string.ascii_lowercase.find(x)
        r = string.ascii_lowercase[(ind % key)]
        res += r
    return res

def main():
    # msg = input("Enter message to encrypt: ")
    msg = "Hard work is the key to succes"
    msg = msg.lower()
    msg = msg.replace(" ", "zz")
    print("\nReplace zz : 1)",msg, len(msg))
    if len(msg) != 36:
        print("Invalid message length. ")
        return
    msg = MultiplicativeCipher.encrypt(msg,17)
    print("\nMultiplicative : 2)",msg)
    
    print("\nReplace chars : 3)",msg)
    
    first = ''
    last = ''
    fi = ''
    li = ''
    for x in msg:
        ind = string.ascii_lowercase.find(x)
        f,l = find_remindable_numbers(ind)
        fi += str(f) + ' '
        li += str(l) + ' '
        # print("FF:",x,ind,"=",f,l)
        first += string.ascii_lowercase[f]
        last += string.ascii_lowercase[l]
    msg = first + last
    print("\nTwo matrix :  4)",msg, "LEN:",len(msg))
    s1,s2,s3,s4,s5,s6 = msg[:12],msg[12:24],msg[24:36],msg[36:48],msg[48:60],msg[60:72]
    print(s1,'\n',s2)
    s1m = MatrixDiagonals.encrypt(s1)
    s2m = MatrixDiagonals.encrypt(s2)
    s3m = MatrixDiagonals.encrypt(s3)
    s4m = MatrixDiagonals.encrypt(s4)
    s5m = MatrixDiagonals.encrypt(s5)
    s6m = MatrixDiagonals.encrypt(s6)
    print(s1m,'\n',s2m)

    # print_matrix(s1m)
    msg = ''.join([''.join(x) for x in s1m]) + ''.join([''.join(x) for x in s2m]) + ''.join([''.join(x) for x in s3m]) + ''.join([''.join(x) for x in s4m]) + ''.join([''.join(x) for x in s5m]) + ''.join([''.join(x) for x in s6m])
    print("\n5)",msg, "LEN:",len(msg))
    msg = add_rand_in_prime(msg)
    print("\n\n6)",msg, "LEN:",len(msg))
    msg = replace_chars(msg,[
        ('a','z'),
        ('b','n'),
        ('x','u'),
        ('j','v'),
        ('f','i')
    ])
    print("\n\n\n", msg)

    # msg = get_matrix(msg, 6, 6)
    

def print_matrix(matrix:list[list]):
    for x in matrix:
        for y in x:
            print(y, end=" ")
        print()

def generate_random_characters(length: int) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def read_file(url) -> str:
    with open(url, 'r') as file:
        return file.read()

def write_file(url, content):
    with open(url, 'w') as file:
        file.write(content)

if __name__ == '__main__':
    main()