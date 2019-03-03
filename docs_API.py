import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('auth_token.json',scope)
GSpread=gspread.authorize(creds)
spreadsheet = GSpread.open('Schedules')

student_sheets=(spreadsheet.worksheet('round0'),spreadsheet.worksheet('round1'),spreadsheet.worksheet('round2'))
class_sheet=GSpread.open('Schedules').worksheet('classes')



student_num=1
class_num=1
voting_round=0

def get_next_class_row():
    global class_num
    class_num+=1
    return class_sheet.row_values(class_num, 'UNFORMATTED_VALUE')

def get_next_student_row(sheet_num):
    global student_num
    student_num+=1
    if(sheet_num==0):
        return student_sheets[sheet_num].row_values(student_num, 'UNFORMATTED_VALUE')
    else:
        row_index_last_sheet=student_num#row_of_student(sheet_num-1,student_sheets[sheet_num].cell(student_num,1,'UNFORMATTED_VALUE').value)
        return (student_sheets[sheet_num].row_values(student_num, 'UNFORMATTED_VALUE'),
                student_sheets[sheet_num-1].range(row_index_last_sheet,7,row_index_last_sheet,14))

def write_class(row,col,value):
    class_sheet.update_cell(row,col,value)

def write_student(sheet_num,row,col,value):
    student_sheets[sheet_num].update_cell(row,col,value)

def row_of_student(sheet_num,value):
    return student_sheets[sheet_num].find(value).row
