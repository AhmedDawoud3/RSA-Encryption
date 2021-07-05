def main():
    print("Welcome to the Decrypter")

    text = input("Please enter the text you want to decrypt:")

    d = int(input("d: "))
    N = int(input("N: "))

    print("Your Decrypted text is")

    for i in text:
        if i == ' ':
            print(' ', end="")
        else:
            i = ord(i)
            i **= d
            i %= N
            print(chr(i), end="")


main()
