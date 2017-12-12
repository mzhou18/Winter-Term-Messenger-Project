#Runner Class
from AlphabetShift import Encoding
from morsecode import morsecode
from huh import PigeonMessage
again = str(input('Would you like to encode?1 for yes 2 for no. \n'))
while again=='1':
	mainmessage = str(input('What kind of message would you like to send? 1 for morse, 2 for alphabet shift, or 3 for pigeon.  '))
	while mainmessage != '1'and mainmessage !='2' and mainmessage !='3':
		print('That is not an option.\n')
		mainmessage = str(input('What kind of message would you like to send? 1 for morse, 2 for alphabet shift, or 3 for pigeon.  '))
	if mainmessage =='1':

		morsetool = morsecode(input('MESSAGE: '))

		result = morsetool.write()

		print(result)

		f = open("test.txt","a") #opens file with name of "test.txt and appends to it"
		f.write(result + "\n\n")
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
			f = open("test.txt","a") #opens file with name of "test.txt and appends to it"
			f.write(code1.string1 + "\n\n")
			f.close()
		elif answer =='2':
			code1 = Encoding(str(input('What message would you like to decode?  ')))
			code1.decode()
			print(code1.string2)
			f = open("test.txt","a") #opens file with name of "test.txt and appends to it"
			f.write(code1.string2 + "\n\n")
			f.close()
	#___________________________________________________________________________________________________________________
	elif mainmessage == '3':
		choice = ''
		choice = str(input("Press 1 to encode your PigeonMessage®. Press 2 to decode a PigeonMessage®.\n"))
		while choice != '1' and choice !='2':
			print('That is not an option.\n')
			choice = str(input("Press 1 to encode your PigeonMessage®. Press 2 to decode a PigeonMessage®.\n"))

		if choice == '1':
			message = str(input("What is the message?\n"))
			message1 = PigeonMessage(message)
			message1.secret()
			print('                           .-''-.')
			print("                         / ,    \'")
			print("                      .-'`(o)    ;'")
			print("                      '-==.       |")
			print('                           `._...-;-.')
			print('                            )--"""   `-.')
			print('                           /   .        `-.')
			print('                          /   /      `.    `-.')
			print('                          |   \    ;   \      `-._________')
			print('                          |    \    `.`.;          -------`.')
			print('                           \    `-.   \\\\          `---...|')
			print("                           `.     `-. ```\.--'._   `---...|")
			print('                              `-.....7`-.))\     `-._`-.. /')
			print("                                `._\ /   `-`         `-.,'")
			print('                                  / /')
			print('                                 /=(_')
			print("                              -./--' `")
			print('                            ,^-(_')
			print("                            ,--'")
			print("-------------------------------------------------------------------")
			print(message1.output2)
			print("-------------------------------------------------------------------")
			
		if choice == '2':
			message = str(input("What is the message?\n"))
			message1 = PigeonMessage(message)
			message1.unsecret()
			print('                           .-''-.')
			print("                         / ,    \'")
			print("                      .-'`(o)    ;'")
			print("                      '-==.       |")
			print('                           `._...-;-.')
			print('                            )--"""   `-.')
			print('                           /   .        `-.')
			print('                          /   /      `.    `-.')
			print('                          |   \    ;   \      `-._________')
			print('                          |    \    `.`.;          -------`.')
			print('                           \    `-.   \\\\          `---...|')
			print("                           `.     `-. ```\.--'._   `---...|")
			print('                              `-.....7`-.))\     `-._`-.. /')
			print("                                `._\ /   `-`         `-.,'")
			print('                                  / /')
			print('                                 /=(_')
			print("                              -./--' `")
			print('                            ,^-(_')
			print("                            ,--'")
			print("-------------------------------------------------------------------")
			print(message1.output2)
			print("-------------------------------------------------------------------")
		f = open("test.txt","a") #opens file with name of "test.txt and appends to it"
		f.write(message1.output2 + "\n\n")
		f.close()
	again = str(input('Would you like to encode again?1 for yes 2 for no. \n'))
print('Thank you. Come again soon.')

