import string

class MultiplicativeCipher:
    alphabets = string.ascii_lowercase

    @classmethod
    def encrypt(cls,msg:str,key:int) -> str:
        msg = msg.lower()
        res = ''
        for x in msg:
            ind = cls.alphabets.find(x)
            r = cls.alphabets[((ind * key) % 26)]
            res += r
        return res
    @classmethod
    def decrypt(cls,encrypted_text, key):
        res = ''
        for encrypted_char in encrypted_text:
            inverse_key = None
            for i in range(26):
                if (key * i) % 26 == 1:
                    inverse_key = i
                    break
            if inverse_key is not None:
                position = cls.alphabets.index(encrypted_char)
                decrypted_position = (inverse_key * position) % 26
                decrypted_char = cls.alphabets[decrypted_position]
                res += decrypted_char.lower()
            else:
                res += "."
        return res
