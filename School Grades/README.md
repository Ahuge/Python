This is a program that could hypothetically be used to input student's
grades. It has the ability to add/remove students, add/remove grades,
list the students, print their averages in each marking category (Tests,
Quizzes, Homework) and change the grade weighting. It safely tests the
inputs to make sure they will work. It backs up all of the data to a
Students.inf file and then each time it opens, to a Students.bak file.
If the .inf is missing the data will be loaded from the .bak file and
then written into a new .inf on Exit. If both are missing, it will
happily start from scratch and save you a new Students.inf file