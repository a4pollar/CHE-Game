import classroom
from classroom import get_example_data

def create_student_dictionary(names, student_ids, birthdays, department):
    dict={"full_name":names,"ID":student_ids,"student_birthday":birthdays,"student":department}
    print(dict)
    return dict


#print(x["full_name"])

listofnames = (classroom.get_example_data()[0][0])
listofstudentids = (classroom.get_example_data()[0][1])
listofnirthdays = (classroom.get_example_data()[0][2])
listofdepartment = (classroom.get_example_data()[0][3])

namespecific = listofnames[0]
x =create_student_dictionary(namespecific, "yes", "hell", "yes")

def create_faculty_dictionary(names,student_ids, birthdays, department):
    faculty={"full_name":names,"ID":student_ids,"student_birthday":birthdays,"student":department}
    print(faculty)
    for i in faculty["fu"]:
        i
    if faculty['student'][-1]=='Civil Engineering':
        print(f"Hello {faculty['full_name'][-1]} Welcome to Engineering")

create_faculty_dictionary(listofnames[0:10],listofstudentids[0:10],listofnirthdays[0:10],listofdepartment[0:10])