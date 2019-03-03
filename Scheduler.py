from Class import Class
from Student import Student
import Tokenizer
import docs_API

#pull all class info from docs
#pull all student information from google docs
#First: make a dummy class and a dummy student, first parameter = None
#tokenize and create classes
#tokenize and create students (and) choices
#Push each student onto a heapq as you read using heapq.heappush(q,student) where q is the list
#


dummy_class = Class(None, None, None, None, None,None)
dummy_student = Student(None, None, None, None, None, None)
sheet_num=1

#    def __init__ CLASS (self, _id, _title, _teacher, _period, _max_capacity):
#    def __init__(self, _name, _id, _bet, _class_list):


Tokenizer.tokenize_class()
Tokenizer.tokenize_students(sheet_num)

for i in range(len(Student.student_list)):
    student = dummy_student.pop_student()
    student_row=docs_API.row_of_student(sheet_num,student.name)
    for class_num in student.class_list:
        _class = Class.class_list[class_num]
        if student.credits >= _class.get_required_credits() and not _class.is_full() and student.student_schedule[_class.period] == '':
            student.enrol(_class)
            _class.enrol_student(student)
    for period in range(0,7):
        if student.student_schedule[period] != '':
            print(student.student_schedule[period])
            docs_API.write_student(sheet_num,student_row, period+8, student.student_schedule[period])
    if '' in student.class_list:
        student.requeue()
    docs_API.write_student(sheet_num,student_row, 7, student.credits)

for i in range(0, len(Class.class_list)):
    docs_API.write_class(i+2, 6, Class.class_list[i].get_required_credits())
    docs_API.write_class(i+2, 7, Class.class_list[i].current_capacity)
    print(Class.class_list[i].title + '::'+str(Class.class_list[i].class_num) +
          '::' + str(Class.class_list[i].get_required_credits()))
