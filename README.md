# simplified_des

This is an implementation of simplified DES, as specified in Prof. Yener's lecture slides

des.py takes four command-line arguments
1. the name of the file to encrypt or decrypt
2. the name of the desired output file
3. An integer in the range [0, 1023]
4. 0, if you wish to encrypt a file, or a non-zero int if you wish to decrypt

The program then attempts to open the file specified by the first command-line argument. 
If it succeeds, then it reads the file in one-byte chunks, and stores them in a list.
The program then iterates through the list, encrypts each byte, and then stores the 
encrypted byte in another list. Once every byte has been encrypted, each encrypted byte
is written to the output file specified on the command line.

The encryption algorithm itself works by taking a byte of data, permuting it as specified
in the lecture notes, splitting it into left and right halves, and then applying the
feistel function to the right half of the bits. The output of the feistel function
is then XORed with the left half of the bits. The new right bits are then set
as the output of the XOR, and the new left bits are simply the right bits before
they were put through the feistel function.
