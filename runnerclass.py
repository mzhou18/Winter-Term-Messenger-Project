#Runner Class
from AlphabetShift import Encoding

answer = str(input('Would you like to encode a message or decode a message? 1 for encode or 2 for decode  '))
while answer != '1' and answer != '2':
	print('That is not an option.\n')
	answer = str(input('Would you like to encode a message or decode a message? 1 for encode or 2 for decode  '))

if answer == '1':
	code1 = Encoding(str(input('What message would you like to encode?  ')))
	code1.encode()
	print(code1.string1)
elif answer =='2':
	code1 = Encoding(str(input('What message would you like to decode?  ')))
	code1.decode()
	print(code1.string2)
