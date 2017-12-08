#Runner Class
<<<<<<< HEAD
# import AlphabetShift
=======
from AlphabetShift import Encoding
>>>>>>> 525b27b4c2ce67028913ddf1881e3ad7756cefec

# answer = str(input('Would you like to encode a message or decode a message? 1 for encode or 2 for decode  '))
# while answer != '1' and answer != '2':
# 	print('That is not an option.\n')
# 	answer = str(input('Would you like to encode a message or decode a message? 1 for encode or 2 for decode  '))

<<<<<<< HEAD
# if answer == '1':
# 	code1 = Encoding(str(input('What message would you like to encode?  ')))
# 	code1.encode()
# 	print(string1)
# if answer =='2':
# 	code1 = Encoding(str(input('What message would you like to decode?  ')))
# 	code1.decode()
# 	print(string2)

from morsecode import morsecode

morsetool = morsecode(input('MESSAGE: '))

result = morsetool.write()

print(result)
=======
if answer == '1':
	code1 = Encoding(str(input('What message would you like to encode?  ')))
	code1.encode()
	print(code1.string1)
elif answer =='2':
	code1 = Encoding(str(input('What message would you like to decode?  ')))
	code1.decode()
	print(code1.string2)
>>>>>>> 525b27b4c2ce67028913ddf1881e3ad7756cefec
