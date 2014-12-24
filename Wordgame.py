#Guess My Word

print "Guess my word. I'm going to spell it out the first few letters for you. Guess what I'm thinking"
print "Let's guess started"
print "Time for the word!"

print "\n"

print "c"
print "a"

word1 = raw_input("What is the word? ")

if word1 in ['cat', 'Cat', 'CAT']:
	print "You are right!"

else: 
	print "Sorry, better luck next time"


print "\n"

print "Time for the second word"

print "d"
print "o"

word2 = raw_input("What is the word? ")

if word2 in ['Dog', 'dog', 'DOG']:
	print "You are right!"

else: 
	print "Sorry, better luck next time"

print "\n"

print "Time for another word!"

print "h"
print "e"
print "l"

word3 = raw_input("What is the word? ")

if word2 in ['Hello', 'hello', 'HELLO']:
	print "You are right!"

else: 
	print "Sorry, better luck next time"
