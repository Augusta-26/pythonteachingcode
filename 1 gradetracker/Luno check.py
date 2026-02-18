import statistics as s

admins = {"chico":'7', "Luno":'77', "Augusta":'777'}

students = { "aaa":[4,5,6],
             "bbb":[5,6,7],
             "ccc":[6,7,8]  }

def add_grade():
    student_name = input('enter student name: ')
    grade_enter = input('enter the grade to add: ')

    print('you enter grade for student named',student_name)
    if student_name in students:
        students[student_name].append(float(grade_enter))
        print('grades of',student_name,'is',students[student_name]) 
    else:
        print(student_name,'is not your student')

def remove_student():
    student_name = input('enter student name: ')
    print('you are removing student named',student_name)
    if student_name in students:
        del students[student_name]
        print('you removed student named',student_name)
        print('current list of students:',students)
    else:
        print(student_name,'is not your student')

def average_grade():
    for student in students:
        grades = students[student]
        average = s.mean(grades)
        print(student,'average is',average)

def main():
    print('Welcome user:',login_id)
    print('Enter your choice:')
    print('\t1. add grade')
    print('\t2. remove student')
    print('\t3. calculate average for all students')
    print('\t4. exit')

    user_choice = input('enter 1-4: ')
    if user_choice == '1':
        add_grade()
    elif user_choice == '2':
        remove_student()
    elif user_choice == '3':
        average_grade()
    elif user_choice == '4':
        exit()
    else:
        print('invalid choice')
    
login_id = input('enter id: ')
if login_id in admins:
    login_pass = input('enter password: ')
    if login_pass == admins[login_id]:
        while True:
            main()
    else:
        print('wrong pass')
else:
    print('wrong id')

    
            

















        






                        

