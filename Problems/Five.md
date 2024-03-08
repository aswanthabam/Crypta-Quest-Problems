# Problem 5 - Multiplicative Cipher Decryption

In this step, you want to perform **multiplicative cipher decryption** on the previous result (key for decryption is 17).
First, you want to convert the characters from the previous result into numbers. The characters and their respective numbers will be as follows:

![Image Loading](https://raw.githubusercontent.com/aswanthabam/Vijnana/images/public/cq/Four-1.png)

- Then, you want to perform multiplicative cipher decryption on each of these numbers.

- **Dont know how to decrypt a multiplicative cipher ?**

    - For decrypting the multiplicative cipher, you want to first find the inverse key.
        - The inverse key is a number between 0 and 25, that will give remainder 1, when multiplied with the key (17) and divided by 26 

    ![Image Loading](https://raw.githubusercontent.com/aswanthabam/Vijnana/images/public/cq/Five-1.png)

    - Next, you want to multiply this inverse key with each of the elements in the list, and the result needs to be divided by 26, and find the remainder.

    ![Image Loading](https://raw.githubusercontent.com/aswanthabam/Vijnana/images/public/cq/Five-2.png)

- Now, convert the resultant remainders into the corresponding characters.

- Now You will have a string of length 36, You want to replace the character pair "**zz**" with a white space *" "*.

Did you find a meaningful message? That's the answer. Submit it on the submission page.
