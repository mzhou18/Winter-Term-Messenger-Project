#Runner Class
from huh import PigeonMessage
from AlphabetShift import Encoding
from morsecode import morsecode

mainmessage = str(input('What kind of message would you like to send? 1 for morse, 2 for alphabet shift, or 3 for pigeon.  '))
while mainmessage != '1'and mainmessage !='2' and mainmessage !='3':
	print('That is not an option.\n')
	mainmessage = str(input('What kind of message would you like to send? 1 for morse, 2 for alphabet shift, or 3 for pigeon.  '))

if mainmessage == '1':

	morsetool = morsecode(input('MESSAGE: '))

	result = morsetool.write()

	print(result)
	f = open("test.txt","a") 
	f.write(result+ "\n\n")
	f.close()

#___________________________________________________________________________________________________________________

elif mainmessage =='2':
	answer = str(input('Would you like to encode a message or decode a message? 1 for encode or 2 for decode  '))
	while answer != '1' and answer != '2':
		print('That is not an option.\n')
		answer = str(input('Would you like to encode a message or decode a message? 1 for encode or 2 for decode  '))
	if answer == '1':
		code1 = Encoding(str(input('What message would you like to encode?  ')))
		code1.encode()
		print(code1.string1)
		f = open("test.txt","a")
		f.write(code1.string1 + "\n\n")
		f.close()
	elif answer =='2':
		code1 = Encoding(str(input('What message would you like to decode?  ')))
		code1.decode()
		print(code1.string2+ "\n\n")
		f = open("test.txt","a")
		f.write(code1.string2)
		f.close()
#___________________________________________________________________________________________________________________



