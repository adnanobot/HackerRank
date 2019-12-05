"""
    Day 12 of 30 days of coding from hackerrank.com : Inheritance

    author : adnanobot

    Arrays
    conditions :
    parent class : Person
    child class : Student
    create a method of student class: calculate
    output: grade
"""

f = open("file.txt", "r")
print(f.read())

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        print("Average", average)
        if average <= 100 and average >= 90:
            grade = "O"
        elif average < 90 and average >= 80:
            grade = "E"
        elif average < 80 and average >= 70:
            grade = "A"
        elif average < 70 and average >= 55:
            grade = "P"
        elif average < 55 and average >= 40:
            grade = "D"
        elif average < 40:
            grade = "T"

        return grade

# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input()) # not needed for Python
# scores = list( map(int, input().split()) )

firstName = "Abyan"
lastName = "Tuttu"
idNum = 427580
scores = [65, 60, 65, 65]

s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
