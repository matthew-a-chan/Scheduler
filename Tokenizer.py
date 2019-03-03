import docs_API
from Student import Student
from Class import Class

def tokenize_students(sheet_num):
    row=docs_API.get_next_student_row(sheet_num)
    if(sheet_num==0):
        while row != []:
            print(row)
            Student(row[0],row[1],row[2],(row[3],row[4],row[5]),0,('','','','','','',''))
            row=docs_API.get_next_student_row(sheet_num)
    else:
        while row[0] != []:
            print(row[0][0],row[0][1],row[0][2],(row[0][3],row[0][4],row[0][5]),row[1][0].value,(row[1][1].value,row[1][2].value,row[1][3].value,row[1][4].value,row[1][5].value,row[1][6].value,row[1][7].value))
            Student(row[0][0],row[0][1],row[0][2],(row[0][3],row[0][4],row[0][5]),row[1][0].value,(row[1][1].value,row[1][2].value,row[1][3].value,row[1][4].value,row[1][5].value,row[1][6].value,row[1][7].value))
            row=docs_API.get_next_student_row(sheet_num)

def tokenize_class():
    row=docs_API.get_next_class_row()
    while row != []:
        print(row)
        Class(row[0],row[1],row[2],row[3],row[4],row[6])
        row=docs_API.get_next_class_row()