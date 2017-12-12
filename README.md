# Winter Term Messenger Project

## By John Stamos

We have three messenger classes in total. We have a class that changes a message into morse code,
a class that codes messages by an alphabet shift, and finally we have a carrier pigeon class that
also codes the message with numbers. John did the alphabet shift class, Michael did the morse code
class, and Palmer did the carrier pigeon class.

# ------------------------------------------

### Alphabet Shift

The alphabet shift is an encoder than replaces each letter of the alphabet with letters five ahead
of the original letter. For example, a --> e, b --> f, and so on. Doing this makes the message impossible 
to read without decoding it. The decoder just does the same process in reverse. It shifts the alphabet 
by five in the other direction.

###### An example of an Alphabet Shift, but by 3 spaces rather than 5:

![An example of an Alphabet Shift, but by 3 spaces rather than 5](http://www.101computing.net/wp/wp-content/uploads/Caesar_substition_cipher-2.png)

# ------------------------------------------

### PigeonMessenger

The PigeonMessenger changes each character in your message to a number, a -> 1, b -> 2, c -> 3, etc... empty spaces,
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

![PigeonMessenger](https://keeveneo.files.wordpress.com/2012/03/messenger-pigeon-low-res.jpg?w=560)

# ------------------------------------------

### Morse Code
Morse code is a method of transmitting text information as a series of on-off dots and dashes.

Each Morse code symbol represents a text character, such as A, B, C or D, and is represented by a unique sequence of dots and dashes. The user would be able to type in a word, and then each of those letters would be converted into a series of dots and dashes.

Example: "hi" would become ".....-.--"

![Morse Code](https://cdn.thinglink.me/api/image/891739369830875137/1240/10/scaletowidth)

# ------------------------------------------

Writing to file:

I used this website to learn how to write to file: http://www.afterhoursprogramming.com/tutorial/Python/Writing-to-Files/. The morse code and PigeonMessenger each print the same variable as their result,
regardless of whether the message is being coded or decoded, so each one only needs one chunk of code for write to file. The alphabet
shift messenger, however, has separate variables for coded messages and decoded messages so each if statement needs its own write to file
code.
