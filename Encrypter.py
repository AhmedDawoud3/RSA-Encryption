def main():
    print("Welcome to the Encrypter")

    text = input("Please enter the text you want to encrypt:")

    e = int(input("e: "))
    N = int(input("N: "))

    print("Your Encrypted text is")

    for i in text:
        if i != ' ':
            i = ord(i)
            i **= e
            i %= N
            print(chr(i), end="")
        else:
            print(' ', end="")


main()
