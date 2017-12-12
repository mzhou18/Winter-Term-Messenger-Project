# Winter Term Messenger Project

## By John Stamos

We have three messenger classes in total. We have a class that changes a message into morse code,
a class that codes messages by an alphabet shift, and finally we have a carrier pigeon class that
also codes the message with numbers. John did the alphabet shift class, Michael did the morse code
class, and Palmer did the carrier pigeon class.

<<<<<<< HEAD
# ------------------------------------------------------------------------------------------------------
Alphabet Shift- John:
=======
# ------------------------------------------

### Alphabet Shift
>>>>>>> 0ac11fa1f8675dcc868d43989b6a9821b4229eab

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

### Reflection

Everyone contributed to the project, and quite evenly. Palmer worked on his PigeonMessenger, John worked on his Alphabet Shift, and Michael worked on his Morse Code. Each member described their project in the README file. Michael and John began working on the runnerclass, and then John and Palmer finished it up.

Michael: I think the project went really well. I mean, the code works, but also I think each member contributed their fair share. I think the project was really cool because we message a lot in real life, so I was excited to figure out how to code some kind of messenger tool.

John: I think that Github has many pros and cons. Using it allowed us to be able to compile things into the same code so we cold theoretically be working on the same thing at the same time. However, that does not work wso well in practice. 
When  two people works on the same thing at the same time each person is working on a file that becomes outdated because it does not include what everyone else is writing. And when you try to push something, you have to pull from the origin 
first, which might delete the code that you wrote. Because of this, in order for people to be workiing on the same code at the same time, you would have to be constantly pushing and pulling the code which would take up a lot of time that could 
be spent elsewhere. I think that the ideas of Github are really good, but they don't neccesarily execute those ideas well.


Palmer: I was very surprised to see how evenly the work distribution ended up being. We were all pretty confused as to what to do at first, but we slowly started figuring out ways to create a pretty decent program together. We checked each other's codes and worked together on several parts of the code. I think it may be interesting to try to create a messaging app that is slightly more interactive, as this one doesn't really allow input from more than one user, nor can it store multiple separate conversations. 

# ------------------------------------------

### Writing to file:

I used this website to learn how to write to file: http://www.afterhoursprogramming.com/tutorial/Python/Writing-to-Files/. The morse code and PigeonMessenger each print the same variable as their result,
regardless of whether the message is being coded or decoded, so each one only needs one chunk of code for write to file. The alphabet
shift messenger, however, has separate variables for coded messages and decoded messages so each if statement needs its own write to file
code.

<<<<<<< HEAD
Github worked very well for our collaboration, but there was one mistake we made when I asked John to look over my code. We were both working on the code at the same time, which meant only one of our changes could effectively go through. This meant I had to redo the entire write-to-file code. I had already done it once so it was fine, but it could have been more problematic if the changes lost had been greater.


# ------------------------------------------

### Github Experience

Github worked rather well for us nearly every step of the way. We did, however, have one or two awkward moments when we unknowingly edited the same file at the same time. This proved problematic as it meant we had to commit one person's changes, and the other person had to basically redo what they had done before. Besides that, however, everything went pretty smoothly. Our commits are super messy and its hard to tell exactly what happened where sometimes, but big changes are marked decently clearly, clearly enough that we could easily tell where they happened, and that seems like the most important thing.
>>>>>>> 
