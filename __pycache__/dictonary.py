import classroom
from classroom import get_example_data

#Creates a function that takes in all important information about a student
def create_student_dictionary(names, student_ids, birthdays, department):
    if type(names)!=str or type(student_ids)!=int or type(birthdays)!=str or type(department)!=str:
        return None
    student={"full name":names,"ID":student_ids,"birthday":birthdays,"department":department}
    return student

#Creates a function that takes in lists of relevant information about a group of students
def create_faculty_dictionary(names,student_ids, birthdays, department):
    if  type(names)!=list and type(student_ids)!=list and type(birthdays)!=list and type(department)!=list:      #Checks that a list for each key is being sent to the function
        return None
    faculty={"full name":names,"ID":student_ids,"birthday":birthdays,"department":department}
    return faculty

#Creates a function that takes in a dictonary and prints a greeting for each student
def greet_student(faculty):
    if faculty == None:
        return None
    department=faculty["department"]        #Defines the 'department' key in the faculty list as department
    name=faculty["full name"]               #Defines the 'full name' key in the faculty list as name
    if len(department) != 10 or len(department)!=len(name):       #Checks that the department is 10 in length(function takes in a group of 10 students), checks if department and name list are the same length (index in one list has to exist in the other), checks nothing was sent to the function
        return None
    for i in department:                    #Looks at each value in the list assosiated with department
        if i == 'Civil Engineering':        
            z = department.index(i)         #Finds the index of value in the department list
            name=faculty["full name"][z]       #Finds the value at the same index in the 'full name' key
            print(f"Hello {name}! Have fun building bridges for the rest of your life! Welcome in {i}!")       #Prints greeting to user
            department[z] = " "             #replaces value with a space to call the correct index in the 'full name' list incase of multiple instances of a value appearing
        elif i == 'Computer Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Make sure to use deodorant and shower often. Welcome to {i}!")
            department[z] = " "
        elif i == 'Chemical Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! 'Quick, what is a thermocouple?' - Tam. Welcome to {i}!")
            department[z] = " "
        elif i == 'Enviromental Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Final project - hug a tree. Welcome to {i}!")
            department[z] = " "
        elif i == 'Electrical Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Remember to not shock yourself. Welcome to {i}!")
            department[z] = " "
        elif i == 'Geological Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Get ready to play with some rocks! Welcome to {i}!")
            department[z] = " "
        elif i == 'Mechanical Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! 'Quick what is the gravitational constant?' Welcome to {i}!")
            department[z] = " "
        elif i == 'Architecture':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Wait, what is the difference between you and Architectural Engineering? Welcome to {i}!")
            department[z] = " "
        elif i == 'Management Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Wait what do you do again? Welcome to {i}!")
            department[z] = " "
        elif i == 'Mechatronics Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Building rockets 101, 8:30 class... Welcome to {i}!")
            department[z] = " "
        elif i == 'Nanotechnology Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Can you even see the final? Welcome to {i}!")
            department[z] = " "
        elif i == 'Architectural Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Have fun sleeping at the studio! Welcome to {i}!")
            department[z] = " "
        elif i == 'Software Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Do you dream in python? Welcome to {i}!")
            department[z] = " "
        elif i == 'Biomedical Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Make up your mind, are you a doctor or an engineer? Welcome to {i}!")
            department[z] = " "
        elif i == 'Systems Design Engineering':
            z = department.index(i)
            name=faculty["full name"][z]
            print(f"Hello {name}! Ready to design some systems? Welcome to {i}!")
            department[z] = " "

if __name__=='__main__':
    #Example data being used in function: taking the first 10 values for the each key in the example data dictonary
    listofnames = (classroom.get_example_data()[0][0])
    listofstudentids = (classroom.get_example_data()[0][1])
    listofnirthdays = (classroom.get_example_data()[0][2])
    listofdepartment = (classroom.get_example_data()[0][3])

    #Example data being used in function: taking the first value for each key in the example data dictonary
    namespecific = listofnames[0]
    IDpecific = listofstudentids[0]
    birthdayspecific = listofnirthdays[0]
    departmentpecific = listofdepartment[0]

    #Create student dictornary function being printed with example data
    print(create_student_dictionary(namespecific, IDpecific, birthdayspecific, departmentpecific))

    #Create faculty dictonary function being printed with example data
    print(create_faculty_dictionary(listofnames[0:10],listofstudentids[0:10],listofnirthdays[0:10],listofdepartment[0:10]))
        
    #Greet student function being called with example data
    greet_student(create_faculty_dictionary(listofnames[0:10],listofstudentids[0:10],listofnirthdays[0:10],listofdepartment[0:10]))