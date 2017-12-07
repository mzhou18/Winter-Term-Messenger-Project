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
			x += 1
		message = ''.join(array)

message = str(input("Enter your message here:\n"))
message1 = PigeonMessage(message)


print(message)

message1.secret()

print(message)


