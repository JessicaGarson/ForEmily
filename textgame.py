#text game for emily 

print "Hello friend!"

name = raw_input("What's your name? ")
print "Hi, {0}!".format(name)

howisyourday = raw_input("How is your day? ")

if howisyourday in ['good', 'fine', 'Good', 'great', 'Great']:
	print "I'm glad your day is going well"

elif howisyourday in['bad', 'awful', 'Bad', 'not good', 'Not good']:
	print "I'm sorry your day is bad"

else:
	print "Your day is going {0}, I hope it gets better".format(howisyourday)

fav_color = raw_input("What's your favorite color? ")
print "Your name is {0}, and your favorite color is {1}".format(name, fav_color)

dotoday = raw_input("What do you want to do today? ")
print "Today we are going to do {0}!".format(dotoday)

print "Thanks for playing with me friend!"

print "Bye friend!"
