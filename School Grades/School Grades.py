##############################################################
#						Catches errors						 #
##############################################################

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    raw_input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit






############################################################################################################################
#  			  					  Tries to load the inf, then the bak, then starts from scratch							   #
############################################################################################################################

try:
	with open('Students.inf','r') as inf:
		dict_from_file = inf.read()
	file = "inf"
	with open('Students.inf','r') as inf:
		dict_from_file = inf.read()
	with open('Students.bak','w') as bak:
		bak.write("%s" %dict_from_file)
except:
	file = "bak"
	try:
		with open('Students.bak','r') as inf:
			dict_from_file = inf.read()
	except:
		file = "new"
print file
if file == 	"new":
	students = {}
	Percents = {}
else:
	dicts_from_file = []
	with open('Students.%s' %file,'r') as inf:
		for line in inf:
			dicts_from_file.append(eval(line))

	students = dicts_from_file[0]
	Percents = dicts_from_file[1]

	
	
	
############################################################################################################################
#														Main Functions													   #
############################################################################################################################
	

def SetVars(hwPercent, qzPercent, tsPercent):
    NewWeight = ChangeWeight(hwPercent, qzPercent, tsPercent)
    Percents["hwPercent"] = NewWeight[0]
    Percents["qzPercent"] = NewWeight[1]
    Percents["tsPercent"] = NewWeight[2]
    Menu()

def average(numbers):
    count = len(numbers)
    total = 0
    for i in numbers:
        total += i
    total = float(total)/count
    return total

def get_average(student):
    homework = students[student]["homework"]
    quizzes = students[student]["quizzes"]
    tests = students[student]["tests"]
    
    homeworkAVG = average(homework)*Percents["hwPercent"]
    quizzesAVG = average(quizzes)*Percents["qzPercent"]
    testsAVG = average(tests)*Percents["tsPercent"]
    overall = testsAVG + homeworkAVG + quizzesAVG
    return overall
			
			
def get_studentGrades(student):
	HW = average(students[student]["homework"])
	QUIZ = average(students[student]["quizzes"])
	TESTS = average(students[student]["tests"])
	return [HW, QUIZ, TESTS]

###########################################################################################################################################################################################################################
																		#		STUDENTS		#
###########################################################################################################################################################################################################################
			
						## --------     ADD STUDENTS     -------- ##
def AddStudents():
	print """Please print the name of the student that you want to add:
	"""
	newStudent = raw_input(">")
	students[newStudent] = {
    "name": newStudent,
    "homework": [],
    "quizzes": [],
    "tests": []
    }
	NewestStudent = students[newStudent]
	print """Ok, %s has been added.
What would you like to do now?
You can: "Add another" (Add)
"Remove a student" (Remove)
"List all of the students"  (List)
"Go back to the Main Menu" (Menu)
	""" % (newStudent)
	while True:
		answer = raw_input(">")
		if answer == "Add":
			AddStudents()
			break
		elif answer == "Remove":
			RemoveStudents()
			break
		elif answer == "List":
			ListStudents()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"	


						## --------     REMOVE A STUDENT     -------- ##
def RemoveStudents():
	print """Please print the name of the student that you want to remove:
	"""
	while True:
		deadStudent = raw_input(">")
		try:
			ErasedStudent = students[deadStudent]
			del students[deadStudent]
			break
		except:
			print "That student doesnt exist in the student list try again"	
	print """Ok, %s has been removed.
What would you like to do now?
You can: "Add another" (Add)
"Remove a student" (Remove)
"List all of the students"  (List)
"Go back to the Main Menu" (Menu)
	""" % (deadStudent, deadStudent)
	while True:
		answer = raw_input(">")
		if answer == "Add":
			AddStudents()
			break
		elif answer == "Remove":
			RemoveStudents()
			break
		elif answer == "List":
			ListStudents()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"	

						## --------     REMOVE LAST STUDENT     -------- ##
def RemoveLastStudent(NewestStudent):
	deadStudent = students[NewestStudent["name"]]
	del students[NewestStudent["name"]]
	print """Ok, %s has been removed.
What would you like to do now?
You can: "Add another" (Add)
"Remove a student" (Remove)
"List all of the students"  (List)
"Go back to the Main Menu" (Menu)
	""" % (deadStudent["name"], deadStudent["name"])
	while True:
		answer = raw_input(">")
		if answer == "Add":
			AddStudents()
			break
		elif answer == "Remove":
			RemoveStudents()
			break
		elif answer == "List":
			ListStudents()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"				
			
			

						## --------     ADD LAST STUDENT     -------- ##
def AddLastStudent(deadStudent):
	students[deadStudent] = {
    "name": deadStudent["name"],
    "homework": deadStudent["homework"],
    "quizzes": deadStudent["quizzes"],
    "tests": deadStudent["tests"]
    }
	NewestStudent = students[deadStudent]
	print """Ok, %s has been added again.
What would you like to do now?
You can: "Add another" (Add)
"Remove a student" (Remove)
"List all of the students"  (List)
"Go back to the Main Menu" (Menu)
	""" % (deadStudent["name"], deadStudent["name"])
	while True:
		answer = raw_input(">")
		if answer == "Add":
			AddStudents()
			break
		elif answer == "Remove":
			RemoveStudents()
			break
		elif answer == "List":
			ListStudents()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"			
			
		


						## --------     LIST STUDENTS     -------- ##
def ListStudents():
	print
	for i in students:
		print students[i]['name']
		print
		
	print """Ok, That is the list.
What would you like to do now?
You can: "Add another" (Add)
"Remove a student" (Remove)
"List all of the students"  (List)
"Go back to the Main Menu" (Menu)
	"""
	while True:
		answer = raw_input(">")
		if answer == "Add":
			AddStudents()
			break
		elif answer == "Remove":
			RemoveStudents()
			break
		elif answer == "List":
			ListStudents()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"		


###########################################################################################################################################################################################################################
																		#		GRADES		#
###########################################################################################################################################################################################################################



						## --------     ADD GRADES     -------- ##
def AddGrades():
	print """Which student would you like to add grades for? """
	while True:
		student = raw_input(">")
		try:
			MyStudent = students[student]
			break
		except:
			print "That student doesnt exist in the student list try again"	
	print """Which category does this grade go into?
Homework (Homework)
Quizzes (Quizzes)
Tests (Tests)"""
	while True:
		category = raw_input(">")
		try:
			treefern = students[student][category.lower()]
			break
		except:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"	
	print """Ok, what was %s's new mark? """ %student
	while True:
		newGrade = raw_input(">")
		try:
			intGrade = float(newGrade)
			break
		except:
			print "That didn't work, make sure you are typing a number"	
	students[student][category.lower()].append(float(newGrade))
	print """Ok %s got their new mark added into %s. 
What would you like to do?
You can "Add grades" (Add Grades)
"Remove grades" (Remove Grades)
"Get the average for a student" (Student Average)
"List the grades for a student" (Student Grades)
"Go back to the Main Menu" (Menu)""" %(student, category)
	while True:
		answer = raw_input(">")
		if answer == "Add Grades":
			AddGrades()
			break
		elif answer == "Remove Grades":
			RemoveGrades()
			break
		elif answer == "Student Average":
			StudentAverage()
			break
		elif answer == "Student Grades":
			StudentGrades()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"	



						## --------     REMOVE GRADES     -------- ##
def RemoveGrades():
	print """Which student would you like to remove grades from? """
	while True:
		student = raw_input(">")
		try:
			MyStudent = students[student]
			break
		except:
			print "That student doesnt exist in the student list try again"	
	print """Which category is the offending grade in?
Homework (Homework)
Quizzes (Quizzes)
Tests (Tests)"""
	while True:
		category = raw_input(">")
		try:
			treefern = students[student][category.lower()]
			break
		except:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"	
	print """Ok, what was the grade that you wanted removed from %s? """ %student
	while True:
		newGrade = raw_input(">")
		try:
			intGrade = float(newGrade)
			break
		except:
			print "That didn't work, make sure you are typing a number"	
	students["Tom"]["homework"].remove(newGrade)
	print """Ok %s got their new mark added into %s. 
What would you like to do?
You can "Add grades" (Add Grades)
"Remove grades" (Remove Grades)
"Get the average for a student" (Student Average)
"List the grades for a student" (Student Grades)
"Go back to the Main Menu" (Menu)""" %(student, category)
	while True:
		answer = raw_input(">")
		if answer == "Add Grades":
			AddGrades()
			break
		elif answer == "Remove Grades":
			RemoveGrades()
			break
		elif answer == "Student Average":
			StudentAverage()
			break
		elif answer == "Student Grades":
			StudentGrades()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"	




						## --------     STUDENT AVERAGE     -------- ##
def StudentAverage():
	print """Which student would you like to get an average of? """
	while True:
		student = raw_input(">")
		try:
			MyStudent = students[student]
			break
		except:
			print "That student doesnt exist in the student list try again"	
	print  "%s's average is: %s" %(student, get_average(student))
	print """What would you like to do?
You can "Add grades" (Add Grades)
"Remove grades" (Remove Grades)
"Get the average for a student" (Student Average)
"List the grades for a student" (Student Grades)
"Go back to the Main Menu" (Menu)"""
	while True:
		answer = raw_input(">")
		if answer == "Add Grades":
			AddGrades()
			break
		elif answer == "Remove Grades":
			RemoveGrades()
			break
		elif answer == "Student Average":
			StudentAverage()
			break
		elif answer == "Student Grades":
			StudentGrades()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"	

					



						## --------     STUDENT GRADES     -------- ##
def StudentGrades():
	print """Which student would you like to get the grades for? """
	student = raw_input(">")
	grades = get_studentGrades(student)
	print """%s's grades are:
	%s%% in homework
	%s%% in quizzes
	%s%% in tests""" %(student, grades[0], grades[1], grades[-1])
	print  "%s's total average is: %s" %(student, get_average(student))
	print
	print """What would you like to do?
You can "Add grades" (Add Grades)
"Remove grades" (Remove Grades)
"Get the average for a student" (Student Average)
"List the grades for a student" (Student Grades)
"Go back to the Main Menu" (Menu)"""
	while True:
		answer = raw_input(">")
		if answer == "Add Grades":
			AddGrades()
			break
		elif answer == "Remove Grades":
			RemoveGrades()
			break
		elif answer == "Student Average":
			StudentAverage()
			break
		elif answer == "Student Grades":
			StudentGrades()
			break
		elif answer == "Menu":
			Menu()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"	



			



						## --------     Marking Weights     -------- ##
def ChangeWeight(HwPercent, QwPercent, TsPercent):

    print """The current weights are:
		Homework is worth %s%%
		Quizzes are worth %s%%
		Tests are worth %s%%""" %(HwPercent*100, QwPercent*100,	TsPercent*100)
    HHwPercent = HwPercent
    QQwPercent = QwPercent
    TTsPercent = TsPercent
    while True:
		print "Which would you like to change the weight for?"
		while True:
			weightChange = raw_input(">")
			if weightChange.lower() in ("homework", "quizzes", "tests"):
				break
			else:
				print "I didnt catch that, make sure that you are typing it exactly as it's shown"	
		print "Ok what would you like to change it to?"
		while True:
			weightAmount = raw_input(">")
			try:
				intweightAmount = float(weightAmount)
				break
			except:
				print "That didn't work, make sure you are typing a number"	
		if weightChange.lower() == "homework":
			HHwPercent = float(weightAmount)/100
			break
		elif weightChange.lower() == "quizzes":
			QQwPercent = float(weightAmount)/100
			break
		elif weightChange.lower() == "tests":
			TTsPercent = float(weightAmount)/100
			break
		else:
			print 'I didnt catch that, make sure that you are typing either "homework", "quizzes" or "tests"'	
		
    print  """%s weight changed to %s""" %(weightChange, weightAmount)
    if HHwPercent + QQwPercent + TTsPercent < 1:
        print "Your marking doesnt add up to 100%%. Make sure that you fix it."
        print
        print "It adds up to %s%% you are %s%% short" %(((HHwPercent + QQwPercent + TTsPercent)*100), 100-((HHwPercent + QQwPercent + TTsPercent)*100))
    elif HHwPercent + QQwPercent + TTsPercent > 1:
        print "Your marking doesnt add up to 100%%. Make sure that you fix it."
        print
        print "It adds up to %s%% you are %s%% too high" %(((HHwPercent + QQwPercent + TTsPercent)*100), ((HHwPercent + QQwPercent + TTsPercent)*100)-100)
    return [HHwPercent, QQwPercent, TTsPercent]









###########################################################################################################################################################################################################################
																		#		MENU		#
###########################################################################################################################################################################################################################


def Menu():
	print """What would you like to do?
You can "Add students" (Add Students)
"Remove students" (Remove Students)
"Add grades" (Add Grades)
"Remove grades" (Remove Grades)
"Get the average for a student" (Student Average)
"List all of the students" (List Students)
"List the grades for a student" (Student Grades)
"Change how marks are weighted" (Weight)
"Exit" (Exit)


"""
	while True:
		answer = raw_input(">")
		if answer == "Add Students":
			AddStudents()
			break
		elif answer == "Remove Students":
			RemoveStudents()
			break
		elif answer == "Add Grades":
			AddGrades()
			break
		elif answer == "Remove Grades":
			RemoveGrades()
			break
		elif answer == "Student Average":
			StudentAverage()
			break
		elif answer == "List Students":
			ListStudents()
			break
		elif answer == "Student Grades":
			StudentGrades()
			break
		elif answer == "Weight":
			SetVars(Percents["hwPercent"], Percents["qzPercent"], Percents["tsPercent"])
			break
		elif answer == "Exit":
			Studentsfile.write("%s\n" %students)
			Studentsfile.close()
			Weightingfile.write("%s" %Percents)
			Weightingfile.close()
			break
		else:
			print "I didnt catch that, make sure that you are typing it exactly as it's shown"

Studentsfile = open("Students.inf", "w")
Weightingfile = open("Students.inf", "a")		
Menu()