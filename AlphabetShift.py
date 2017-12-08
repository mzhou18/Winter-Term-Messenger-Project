#Encoding a Message

class Encoding:

	def __init__(self, message):
		self.message = message
		self.string1 = ''
		self.string2 = ''

	def encode(self):
		list1 = list(self.message)
		n = 0
		while len(list1)-1 >= n:
			if list1[n].lower() == 'a':
				list1[n] = 'e'
			elif list1[n].lower() == 'b':
				list1[n] = 'f'
			elif list1[n].lower() == 'c':
				list1[n] = 'g'
			elif list1[n].lower() == 'd':
				list1[n] = 'h'
			elif list1[n].lower() == 'e':
				list1[n] = 'i'
			elif list1[n].lower() == 'f':
				list1[n] = 'j'
			elif list1[n].lower() == 'g':
				list1[n] = 'k'
			elif list1[n].lower() == 'h':
				list1[n] = 'l'
			elif list1[n].lower() == 'i':
				list1[n] = 'm'
			elif list1[n].lower() == 'j':
				list1[n] = 'n'
			elif list1[n].lower() == 'k':
				list1[n] = 'o'
			elif list1[n].lower() == 'l':
				list1[n] = 'p'
			elif list1[n].lower() == 'm':
				list1[n] = 'q'
			elif list1[n].lower() == 'n':
				list1[n] = 'r'
			elif list1[n].lower() == 'o':
				list1[n] = 's'
			elif list1[n].lower() == 'p':
				list1[n] = 't'
			elif list1[n].lower() == 'q':
				list1[n] = 'u'
			elif list1[n].lower() == 'r':
				list1[n] = 'v'
			elif list1[n].lower() == 's':
				list1[n] = 'w'
			elif list1[n].lower() == 't':
				list1[n] = 'x'
			elif list1[n].lower() == 'u':
				list1[n] = 'y'
			elif list1[n].lower() == 'v':
				list1[n] = 'z'
			elif list1[n].lower() == 'w':
				list1[n] = 'a'
			elif list1[n].lower() == 'x':
				list1[n] = 'b'
			elif list1[n].lower() == 'y':
				list1[n] = 'c'
			elif list1[n].lower() == 'z':
				list1[n] = 'd'
			n = n+1
		self.string1 =''.join(list1)

	def decode(self):
		list2 = list(self.message)
		a = 0
		global string2
		while len(list2)-1 >= a:
			if list2[a].lower() == 'e':
				list2[a] = 'a'
			elif list2[a].lower() == 'f':
				list2[a] = 'b'
			elif list2[a].lower() == 'g':
				list2[a] = 'c'
			elif list2[a].lower() == 'h':
				list2[a] = 'd'
			elif list2[a].lower() == 'i':
				list2[a] = 'e'
			elif list2[a].lower() == 'j':
				list2[a] = 'f'
			elif list2[a].lower() == 'k':
				list2[a] = 'g'
			elif list2[a].lower() == 'l':
				list2[a] = 'h'
			elif list2[a].lower() == 'm':
				list2[a] = 'i'
			elif list2[a].lower() == 'n':
				list2[a] = 'j'
			elif list2[a].lower() == 'o':
				list2[a] = 'k'
			elif list2[a].lower() == 'p':
				list2[a] = 'l'
			elif list2[a].lower() == 'q':
				list2[a] = 'm'
			elif list2[a].lower() == 'r':
				list2[a] = 'n'
			elif list2[a].lower() == 's':
				list2[a] = 'o'
			elif list2[a].lower() == 't':
				list2[a] = 'p'
			elif list2[a].lower() == 'u':
				list2[a] = 'q'
			elif list2[a].lower() == 'v':
				list2[a] = 'r'
			elif list2[a].lower() == 'w':
				list2[a] = 's'
			elif list2[a].lower() == 'x':
				list2[a] = 't'
			elif list2[a].lower() == 'y':
				list2[a] = 'u'
			elif list2[a].lower() == 'z':
				list2[a] = 'v'
			elif list2[a].lower() == 'a':
				list2[a] = 'w'
			elif list2[a].lower() == 'b':
				list2[a] = 'x'
			elif list2[a].lower() == 'c':
				list2[a] = 'y'
			elif list2[a].lower() == 'd':
				list2[a] = 'z'
			a = a+1
		self.string2 =''.join(list2)
'''
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
'''