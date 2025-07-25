SemMarks = []

def inputIA():
    marks = []

    print("Enter your IA Marks ( 0 - 20 ) : ---")
    for i in range(0,3):
        mark = int(input(f"IA{i+1} : "))
        marks.append(mark)

    return marks

def findMin(marks=[]):
    if(marks == []):
       print("The List is empty")
       return 0

    min = marks[0]

    for mark in marks:
        if(mark < min):
            min = mark
    
    return min

def findSum(marks=[]):
    if(marks == []):
       print("The List is empty")
       return 0
    
    sum = 0

    for mark in marks:
        sum += mark

    return sum

def inputCTA():
    CTA = int(input("Enter Your CIA ( 0 - 10 ) : "))
    return CTA

def findCIE():
    marks = inputIA()
    Best_Of_2 = findSum(marks) - findMin(marks)
    CTA = inputCTA()
    CIE = Best_Of_2 + CTA

    return CIE

def convertSemMarks(marks=0):
    if(marks > 0):
        newMarks = marks / 2
    else:
        newMarks = marks
    
    return newMarks

def findSem():
    marks = int(input("Enter Your SemEnd Marks ( 0 - 100 ) : "))

    newMarks = convertSemMarks(marks)

    return newMarks

def findTotal():
    return findCIE() + findSem()

print("--- Well Come To CGPA, SGPA Marks Calculater ---")
no_sub = int(input("How Meny Subject You Have : "))

for i in range(0,no_sub):
    sub = []
    sub_name = input("Enter Subject Name : ")
    sub.append(sub_name)
    sub_Credit = int(input("\tSubject Credite : "))
    sub.append(sub_Credit)
    sub_Total = findTotal()
    sub.append(sub_Total)
    sub_Grade = findGrade(sub_Total,sub_Credit)
    sub.append(sub_Grade)

    SemMarks.append(sub)
