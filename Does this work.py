#Encoding a Message

class Encoding:

	def __init__(self, message):
		self.message = message

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
		string1 =''.join(list1)
		print(list1)
		print(string1)


code1 = Encoding(str(input('What message would you like to encode?')))
code1.encode()
