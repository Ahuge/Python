from sys import exit
#I am just putting a little disclaimer at the top here and clearing anything that mightve been above
print """
























































This is a quick python tool to estimate what you will make if you inverst your money.
This is assuming constant conditions (which is not always the case) so use this with a grain of salt.
This is also assuming that as you make more money, you'll keep living on the same amount and just invest more which is also not fully realistic for most people
"""
print "Is that ok?"
#I am making sure that they said either yes or no. They can also say any of the other words printed there too. The can be upper or lower case
while True:
    a = raw_input("> ")
    if a.lower() in ('y', 'ye', 'yea', 'yeah', 'yup', 'yes'):
        print "Ok good!"
        break
    if a.lower() in ('n', 'no', 'nop', 'nope', 'nah'):
        print "Oh....Darn, Ok I'll quit"
        exit()
    print 'Im sorry I didnt understand you. Please type "Yes" or "No"'
#Here I am checking how many years this simulation is and then also checking to make sure the user types in a number and not a word
print "How many years long is this simulation?"
while True:
	Years = raw_input(">")
	try:
		x = int(Years)
	except:
		x = ""
	amIanInt = isinstance( x , int)
	if amIanInt == True:
		Years = int(Years)
		break
	else:
		print "Could you at least give me an actual number?"	
#Same thing as above but with the starting deposit amount
print "What is your starting deposit amount?"
while True:
	startingWage = raw_input(">")
	try:
		x = int(startingWage)
	except:
		x = ""
	amIanInt = isinstance( x , int)
	if amIanInt == True:
		startingWage = int(startingWage)
		break
	else:
		print "Could you at least give me an actual number?"	
#Same thing as above but with the deposit increase amount
print "What percent does this go up yearly?"
while True:
	Increase = raw_input(">")
	try:
		x = int(Increase)
	except:
		x = ""
	amIanInt = isinstance( x , int)
	if amIanInt == True:
		Increase = int(Increase)
		break
	else:
		print "Could you at least give me an actual number?"	
#Same thing as above but with the investment earnings
print "What percent will your investment increase by every year?"
while True:
	Investment = raw_input(">")
	try:
		x = int(Increase)
	except:
		x = ""
	amIanInt = isinstance( x , int)
	if amIanInt == True:
		Investment = int(Investment)
		break
	else:
		print "Could you at least give me an actual number?"

Current = 1
#For the first year we are assuming an empty bank
Bank = 0
#We are turning our percent numbers into decimals
WP = (Increase*.01) + 1
IP = (Investment*.01) + 1


def intWithCommas(x):
    while True:
        number = x
        try:
            x = int(number)
        except:
            x = ""
        amIanInt = isinstance( x , (int, float))
        if amIanInt == True:
            number = int(number)
            break
    	print "Could you at least give me an actual number?"
    if number < 0:
        return '-' + intWithCommas(-number)
    result = ''
    while number >= 1000:
        number, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (number, result)




print """


----------------------------------------------------------------------------------------------------"""
#Only running up until the last year the user wanted us too
while Current <= Years:
#instead of keeping the previous year's deposit in a varriable, we are just calculating it on the fly by using the current year minus one to use as a power of
    thisWage = startingWage*(WP)**(Current - 1)
    Bank = (thisWage + Bank)*IP
    print "Year %s would equal: $%s" %(Current, "{:,}".format(Bank))
#It's next year! Woohoo, Happy New Years!
    Current = Current + 1
print "----------------------------------------------------------------------------------------------------"
Earn = "{:,}".format(Bank - (startingWage*Years))
Avg = "{:,}".format((Bank - (startingWage*Years))/Years)
print "You earned $%s more than you would have had you just sat on the money" %(Earn)
print "That is an average of $%s per year" %(Avg)
#Making sure that the terminal doesnt close before we can read our results
raw_input("Press Enter to Continue:")