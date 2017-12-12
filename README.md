# Winter Term Messenger Project

We have three messenger classes in total. We have a class that changes a message into morse code,
a class that codes messages by an alphabet shift, and finally we have a carrier pigeon class that
also codes the message with numbers. John did the alphabet shift class, Michael did the morse code
class, and Palmer did the carrier pigeon class.

The alphabet shift is an encoder than replaces each letter of the alphabet with letters five ahead
of the original letter. For example, a --> e, b --> f, and so on. Doing this makes the message impossible 
to read without decoding it. The decoder just does the same process in reverse. It shifts the alphabet 
by five in the other direction.

# -----------------------------------------------------------------------------------------------------

The PigeonMessager changes each character in your message to a number, a -> 1, b -> 2, c -> 3, etc... empty spaces,
such as the spaces between words, remain empty. 

	If the message entered reads: 

	hello world!

	The message after being coded reads:

	8-5-12-12-15- -23-15-18-12-4-!

The program also has the ability to decode messages. Messages set to be decoded must be formatted like the result shown above.
As before, empy spaces will remain empty. Now, however, the hyphens between the characters will disappear.

	If the message entered reads:

	8-5-12-12-15- -23-15-18-12-4-!

	The message after being decoded reads:

	hello world!

These messages, whether coded or decoded are printed below the image of a giant pigeon that is carrying your message.
This code has some problems, however. The code cannot distinguish between upper case and lower case letters and so any upper case letters you
send in a coded message will be converted to lower case letters. Additionally, you can't have numbers in a decoded message. There is no way to distinguish
between real numbers, and numbers that are part of the code. Same for letters in the coded messages. 

# -----------------------------------------------------------------------------------------------------