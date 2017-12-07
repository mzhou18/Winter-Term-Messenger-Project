#Runner Class

def main():

    message = input('MESSAGE: ')

    for character in message:
    	#converts all characters to uppercasae letters
        print morsecode[character.upper()],

if __name__ == "__main__":
    main()