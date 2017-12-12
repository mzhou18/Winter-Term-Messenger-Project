#Winter Project

#Goal: (1) Github (2) Classes

#Messenger: 3 messenger classes, 1 runner class (main class), and 1 write to file

    # CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
    #         'D': '-..',    'E': '.',      'F': '..-.',
    #         'G': '--.',    'H': '....',   'I': '..',
    #         'J': '.---',   'K': '-.-',    'L': '.-..',
    #         'M': '--',     'N': '-.',     'O': '---',
    #         'P': '.--.',   'Q': '--.-',   'R': '.-.',
    #      	'S': '...',    'T': '-',      'U': '..-',
    #         'V': '...-',   'W': '.--',    'X': '-..-',
    #         'Y': '-.--',   'Z': '--..',
            
    #         '0': '-----',  '1': '.----',  '2': '..---',
    #         '3': '...--',  '4': '....-',  '5': '.....',
    #         '6': '-....',  '7': '--...',  '8': '---..',
    #         '9': '----.' 
    #         }


# morselist = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', 
#     '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
#     '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

# def main():

#     message = input('MESSAGE: ')

#     for char in message:
#         print(morselist[ord(char.lower()) - 97])

# main()


morselist = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', 
            '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
            '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

class morsecode:
    def __init__(self, message):
        self.message = message

    def write(self):
        newmessage = ''
        for char in self.message:
            newmessage = newmessage + morselist[ord(char.lower()) - 97]
        return newmessage

# morsetool = morsecode(input('MESSAGE: '))

# result = morsetool.write()

# print(result)
