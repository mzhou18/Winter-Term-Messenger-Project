#Encoding a Message

class Encoding:

	def __init__(self, message):
		self.message = message

	def encode(self):
		list1 = list(self.message)
		n = 0
		while len(list1)-1 >= n
			if list1[n].lower() == 'a':
				list1[n] = 'e'
			if list1[n].lower() == 'b':
				list1[n] = 'f'
			if list1[n].lower() == 'c':
				list1[n] = 'g'
			if list1[n].lower() == 'd':
				list1[n] = 'h'
			if list1[n].lower() == 'e':
				list1[n] = 'i'
			if list1[n].lower() == 'f':
				list1[n] = 'j'
			if list1[n].lower() == 'g':
				list1[n] = 'k'
			if list1[n].lower() == 'h':
				list1[n] = 'l'
			if list1[n].lower() == 'i':
				list1[n] = 'm'
			if list1[n].lower() == 'j':
				list1[n] = 'n'
			if list1[n].lower() == 'k':
				list1[n] = 'o'
			if list1[n].lower() == 'l':
				list1[n] = 'p'
			if list1[n].lower() == 'm':
				list1[n] = 'q'
			if list1[n].lower() == 'n':
				list1[n] = 'r'
			if list1[n].lower() == 'o':
				list1[n] = 's'
			if list1[n].lower() == 'p':
				list1[n] = 't'
			if list1[n].lower() == 'q':
				list1[n] = 'u'
			if list1[n].lower() == 'r':
				list1[n] = 'v'
			if list1[n].lower() == 's':
				list1[n] = 'w'
			if list1[n].lower() == 't':
				list1[n] = 'x'
			if list1[n].lower() == 'u':
				list1[n] = 'y'
			if list1[n].lower() == 'v':
				list1[n] = 'z'
			if list1[n].lower() == 'w':
				list1[n] = 'a'
			if list1[n].lower() == 'x':
				list1[n] = 'b'
			if list1[n].lower() == 'y':
				list1[n] = 'c'
			if list1[n].lower() == 'z':
				list1[n] = 'd'
			print(list1)

code1 = Encoding(str(input('What message would you like to encode?')))
code1.encode()
