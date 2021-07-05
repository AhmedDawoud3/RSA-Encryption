# RSA-Encryption
a python app that allows you to generate the encryption and decryption key and use them

-----

Table of contents
=================
<!--ts-->
- [Key Generation](#Key-Generation)
- [Encryption](#Encryption)
- [Decryption](#Decryption)
- [Auther](#Auther)
- [License](#License)
<!--te-->

------

# <a name="Key-Generation"/> Key Generation

Before you start to decrypte and encrypte text you'll need to create two key
* Public key *(The encryption key)*
* Private key *(The decryption key)*

### To run the key generator you'll have to give it two prime numbers and then you'll run it like this
```
python KeysGenerator.py [prime number 1] [prime number 2]
```
eg.
```
python KeysGenerator.py 11 7
```
### Then the program will give you a list of possible encryption keys to choose from
```
All avalible Locks:
1. 13
2. 17
3. 19
4. 23
5. 29
6. 31
7. 37
8. 41
9. 43
10. 47
11. 53
12. 59
```
### You'll choose the corresponding number to the key A.K.A. its index

### Then it'll print the encryption and N in the form of *`(e, N)`*
```
The encryption key (the lock) is: (43, 77)
```
##### In this case 43 is the encryption key and 77 is N

### After this it'll print all the possible decryption key and N in the form of *`(d, N)`*
```
The decryption key (the key) is: (7, 77)
The decryption key (the key) is: (67, 77)
The decryption key (the key) is: (127, 77)
The decryption key (the key) is: (187, 77)
The decryption key (the key) is: (247, 77)
The decryption key (the key) is: (307, 77)
The decryption key (the key) is: (367, 77)
```
#### Note: the decryption keys are unlimited, You'll have to stop it manually using `ctrl + c`
### Now you have your encryption, decryption and N

# <a name="Encryption"/> Encryption

### To encrypte a text you'll have to run `Encrypter.py`
```
python Encrypter.py
```
### Now you'll have to enter the text
```
Welcome to the Encrypter
Please enter the text you want to encrypt: [text here]
``` 
### Now you'll have to enter *`e`* and *`N`*
```
Your Encrypted text is
{cryptic text here}
```
### Now you have your encrypted text


# <a name="Decryption"/> Decryption

### To encrypte a text you'll have to run `Decrypter.py`
```
python Decrypter.py
```
### Now you'll have to enter the text
```
Welcome to the Decrypter
Please enter the text you want to decrypt: [Encrypted text here]
``` 
### Now you'll have to enter *`d`* and *`N`*
```
Your Decrypted text is
{cryptic text here}
```
### Now have decrypted the Encrypted text

# <a name="Auther"/> Auther

### [Ahmed Dawoud](https://github.com/AhmedDawoud3)

# <a name="License"/>  License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/AhmedDawoud3/RSA-Encryption/blob/main/LICENSE) file for details

