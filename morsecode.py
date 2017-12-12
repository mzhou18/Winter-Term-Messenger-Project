#Messenger for Morse Code

#Below is a table I copy and pasted for morse code so that I have the letters and
#the coressponding dashes and dots.

    # CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
    #         'D': '-..',    'E': '.',      'F': '..-.',
    #         'G': '--.',    'H': '....',   'I': '..',
    #         'J': '.---',   'K': '-.-',    'L': '.-..',
    #         'M': '--',     'N': '-.',     'O': '---',
    #         'P': '.--.',   'Q': '--.-',   'R': '.-.',
    #      	'S': '...',    'T': '-',      'U': '..-',
    #         'V': '...-',   'W': '.--',    'X': '-..-',
    #         'Y': '-.--',   'Z': '--..',
            

#I made the table into a list, as seen below. The zero-eth element would be A,
#the second would be B, the third C, and so on. The twenty-fifth element
#would thus be Z.

morselist = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', 
            '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
            '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

#I called the class "morsecode" as well as initialized it.
class morsecode:
    def __init__(self, message):
        self.message = message

#This code will take elements from the list and append it to "new message."
#I used the "ord" function so that I did not have to define each letter from
#A to Z to save time. As a result, the code will return "newmessage," which
#is what the user types.
    def write(self):
        newmessage = ''
        for char in self.message:
            newmessage = newmessage + morselist[ord(char.lower()) - 97]
        return newmessage


#Below is some code I tested to make sure the above worked.

# morsetool = morsecode(input('MESSAGE: '))

# result = morsetool.write()

# print(result)
