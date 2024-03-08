import random
import string
import math

class MatrixDiagonals:
    @classmethod
    def encrypt(cls, msg:str) -> str:
        l = len(msg)
        res = ''
        for i in range(0,l):
            row = []
            for j in range(0,l):
                if i == j:
                    row.append(msg[i])
                else:
                    row.append(random.choice(string.ascii_lowercase))
            res += ''.join(row)
        return res
    @classmethod
    def decrypt(cls, msg:str) -> str:
        l = int(math.sqrt(len(msg)))
        res = ''
        for i in range(0,l):
            for j in range(0,l):
                if i == j:
                    res += msg[i*l+i]
        return res
    
if __name__ == '__main__':
    enc = MatrixDiagonals.encrypt('abcdefghijkl')
    print(enc)
    dec = MatrixDiagonals.decrypt(enc)
    print(dec)
