import sys
class PigeonMessage:

	def __init__(self,message):
		self.message = message

	def secret(self):
		global output1
		global output2
		array = list(self.message)
		x = 0
		while len(array)-1 >= x:
			if array[x].lower() == 'a':
				array[x] = '1'
			elif array[x].lower() == 'b':
				array[x] = '2'
			elif array[x].lower() == 'c':
				array[x] = '3'
			elif array[x].lower() == 'd':
				array[x] = '4'
			elif array[x].lower() == 'e':
				array[x] = '5'
			elif array[x].lower() == 'f':
				array[x] = '6'
			elif array[x].lower() == 'g':
				array[x] = '7'
			elif array[x].lower() == 'h':
				array[x] = '8'
			elif array[x].lower() == 'i':
				array[x] = '9'
			elif array[x].lower() == 'j':
				array[x] = '10'
			elif array[x].lower() == 'k':
				array[x] = '11'
			elif array[x].lower() == 'l':
				array[x] = '12'
			elif array[x].lower() == 'm':
				array[x] = '13'
			elif array[x].lower() == 'n':
				array[x] = '14'
			elif array[x].lower() == 'o':
				array[x] = '15'
			elif array[x].lower() == 'p':
				array[x] = '16'
			elif array[x].lower() == 'q':
				array[x] = '17'
			elif array[x].lower() == 'r':
				array[x] = '18'
			elif array[x].lower() == 's':
				array[x] = '19'
			elif array[x].lower() == 't':
				array[x] = '20'
			elif array[x].lower() == 'u':
				array[x] = '21'
			elif array[x].lower() == 'v':
				array[x] = '22'
			elif array[x].lower() == 'w':
				array[x] = '23'
			elif array[x].lower() == 'x':
				array[x] = '24'
			elif array[x].lower() == 'y':
				array[x] = '25'
			elif array[x].lower() == 'z':
				array[x] = '26'
			x += 1
		output1 = array
		output2 = '-'.join(array)

	def unsecret(self):
		global output1
		global output2
		array = self.message.split('-')
		x = 0
		while len(array)-1 >= x:
			if array[x].lower() == '1':
				array[x] = 'a'
			elif array[x].lower() == '2':
				array[x] = 'b'
			elif array[x].lower() == '3':
				array[x] = 'c'
			elif array[x].lower() == '4':
				array[x] = 'd'
			elif array[x].lower() == '5':
				array[x] = 'e'
			elif array[x].lower() == '6':
				array[x] = 'f'
			elif array[x].lower() == '7':
				array[x] = 'g'
			elif array[x].lower() == '8':
				array[x] = 'h'
			elif array[x].lower() == '9':
				array[x] = 'i'
			elif array[x].lower() == '10':
				array[x] = 'j'
			elif array[x].lower() == '11':
				array[x] = 'k'
			elif array[x].lower() == '12':
				array[x] = 'l'
			elif array[x].lower() == '13':
				array[x] = 'm'
			elif array[x].lower() == '14':
				array[x] = 'n'
			elif array[x].lower() == '15':
				array[x] = 'o'
			elif array[x].lower() == '16':
				array[x] = 'p'
			elif array[x].lower() == '17':
				array[x] = 'q'
			elif array[x].lower() == '18':
				array[x] = 'r'
			elif array[x].lower() == '19':
				array[x] = 's'
			elif array[x].lower() == '20':
				array[x] = 't'
			elif array[x].lower() == '21':
				array[x] = 'u'
			elif array[x].lower() == '22':
				array[x] = 'v'
			elif array[x].lower() == '23':
				array[x] = 'w'
			elif array[x].lower() == '24':
				array[x] = 'x'
			elif array[x].lower() == '25':
				array[x] = 'y'
			elif array[x].lower() == '26':
				array[x] = 'z'
			x += 1
		output1 = array
		output2 = ''.join(array)


