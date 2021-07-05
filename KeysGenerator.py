"""
	Auther:	Ahmed Dawoud
	adawoud1000@hotmail.com

	-Rivest–Shamir–Adleman or RSA algorithm involves four steps:
	.key generation
	.key distribution
	.encryption
	.decryption

	-This file we will be focusing on the key generation
	we will create the encryption key and the decryption key
"""

from time import sleep
from sys import argv


def main():

    # d is the decryption key and this decrypts the encrypted date
    d = 0

    # p and q are the 2 prime numbers that drive the encryption key and the decryption key
    p = 0
    q = 0
    if (len(argv) == 3):
        if not argv[1].isdigit() or not argv[2].isdigit() or not IsPrime(int(argv[1])) or not IsPrime(int(argv[2])):
            print(
                "Usage KeysGenerator.exe OR KeysGenerator.exe [prime number] [prime number]")
            return False
        else:
            p = int(argv[1])
            q = int(argv[2])
    else:
        print(
            "Usage KeysGenerator.exe OR KeysGenerator.exe [prime number] [prime number]")
        return False

    #  N which is the product of p and q
    N = p * q

    """""
		- Get Φ(N) [ it's the number of numbers from 1 to
		N that are not co-prime with N ]

		- We will call it Phi
    """""
    Phi = (p - 1) * (q - 1)

    # Choosing the encryption key
    """""
        - We will get all the avalible encryption keys
        in an array to be used later in generating the
        decryption key

        - e is choosen based on two rules
        1. 1 < e < Φ(N)
        2. e must be co-prime with N and Φ(N)

        - We will make a loop from 0 to Φ(N)

        - Note that we could make the loop
        i = 2 and ignore the first IF statement
    """""

    # e is the list of all the avalible locks or encryption keys that can you can publish publicly
    e = []

    for i in range(0, Phi):
        # Here we didn't check for i < Φ(N) becuase it was already checked in the loop
        if i > 1 and IsCoPrime(i, N) and IsCoPrime(i, Phi):
            e.append(i)

    if len(e) < 1:
        return False

    print("All avalible Locks:")

    for i in range(len(e)):
        print(f"{i + 1}. {e[i]}")

    choosenLock = int(input("Please choose a lock: "))
    while choosenLock > len(e) and choosenLock < 1:
        choosenLock = int(input("Please choose a lock: "))

    E = e[choosenLock - 1]

    print(f"The encryption key (the lock) is: ({E}, {N})")
    sleep(2)

    # Choosing the decryption key
    """""
		- Then finally print to the user all the decryption keys avalible (d)

		- d follows only one condition
			d * e (mod Φ(N)) = 1

		- We will start with d as 0 then increment it by 1 every iteration

		- We wait 1 second after each print

		- We will ignore the decryption key if it's the same as the encryption key
    """""

    d = 0
    while True:
        d += 1
        if ((d * E % Phi) == 1 and d != E):
            print(f"The decryption key (the key) is: ({d}, {N})")
            sleep(1)


# Here's a simple function to check for checkign for primes
def IsPrime(number):
    if number in {0, 1}:
        return False
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True

# To find the greatest common denominator of two numbers
def gdc(a, b):

    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

        # base case
    if a == b:
        return a

    if a > b:
        return gdc(a-b, b)
    return gdc(a, b-a)

# Co-prime numbers are numbers that has no common facter
def IsCoPrime(a, b):
    return gdc(a, b) == 1


if __name__ == '__main__':
    main()
