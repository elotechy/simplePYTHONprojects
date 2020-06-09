print("*********************************")
print("* Welcome to the GPA Calculator *")
print("*********************************")
print("Input your courses and grade points")
print('-------------------------------------')
grade_weights = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}

course_details = {}
grade_details = {}

def addCourse():
    course = input("Please Enter course\t")
    course_credit = input("Enter the credit for {}\t".format(course))
    course_details[course] = int(course_credit)

def getGrades(CD):
    for cc in CD:
        course_grade = input("Enter your grade for {}\t".format(cc))
        grade_details[cc] = (course_grade)

def sumCredits(CD):
    total_credits = 0
    for g in CD:
        total_credits = total_credits + CD[g]
    return total_credits

def multipyGradeAndCredit(CD, GD, GW):
    weight_sum = 0
    for i in CD:
        CW = CD[i] * GW[GD[i]]
        weight_sum += CW
    return weight_sum

def calculateGPA():
    weight_sum = multipyGradeAndCredit(course_details, grade_details, grade_weights)
    total_credits = sumCredits(course_details)
    GPA = weight_sum / total_credits
    return GPA

n = int(input("Please enter the number of courses you offered\t"))

for i in range(n):
    print('-------------------------------------')
    print("Course ", i+1)
    addCourse()
    i += 1
    #print(course_details)

print('-------------------------------------')
print("This are all the courses you offered")
print('-------------------------------------')
print("Courses\t\tCredit")

for c in course_details:
    print("",c + "\t\t ",course_details[c])

print('-------------------------------------')
print("Fill in your grades")

#get the grades
getGrades(course_details)    

print("This are the grades you have entered")
print('-------------------------------------')
print("Courses\t\tGrades")

for g in grade_details:
    print("",g + "\t\t ",grade_details[g])


total_credits = sumCredits(course_details)
print('\nTotal Credit is: ',total_credits)

sum_of_weights = multipyGradeAndCredit(course_details, grade_details, grade_weights)
print("\nTotal credit and weight product: ", sum_of_weights)


print("\n Your GPA is ", calculateGPA())