class PigeonMessage:

	def __init__(self,message):
		self.message = message

	def secret(self):
		array = list(self.message)
		print(array)
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
		self.message = array

message = str(input("Enter your message here:\n"))
message1 = PigeonMessage(message)


print(message)

message1.secret()

print(message)



