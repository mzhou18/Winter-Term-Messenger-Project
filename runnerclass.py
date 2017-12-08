#Runner Class
import AlphabetShift

answer = str(input('Would you like to encode a message or decode a message? 1 for encode or 2 for decode  '))
while answer != '1' and answer != '2':
	print('That is not an option.\n')
	answer = str(input('Would you like to encode a message or decode a message? 1 for encode or 2 for decode  '))

if answer == '1':
	code1 = Encoding(str(input('What message would you like to encode?  ')))
	code1.encode()
	print(string1)
if answer =='2':
	code1 = Encoding(str(input('What message would you like to decode?  ')))
	code1.decode()
	print(string2)
