import heapq
import Class

class Student:

    student_list = []
    student_list_alt = []
    num_students=0

    def __init__(self, _name, _id, _bet, _class_list, _credits, _registered_classes):
        if(_name != None):

            self.name = _name
            self.id = _id
            self.student_schedule = list(_registered_classes)
            self.student_num=Student.num_students
            self.class_list=_class_list
            Student.num_students+=1


            self.apply_classes(_class_list)

            self.credits = _bet + int(_credits)

            

            heapq.heappush(Student.student_list, self)

        else:
            print("DUMMY STUDENT MADE")

    def apply_classes(self,_class_list):
        for class_num in _class_list:
            Class.Class.class_list[class_num].increment_demand()

    #return who has lower credits, if same credits, returns who bet first (LMAO FIRST COME FIRST SERVE?!? WHAT A JOKE!!)
    #  -- rewards people who bet BEFORE getting information about what others are betting/ what classes are popular.
    #  -- Besides, it'll almost never come to the point where tie breakers actually affect whether or not you get into a class.
    def __cmp__(self, other):
        if(cmp(self.credits, other.credits)==0):
            return cmp(self.student_num,other.student_num)
        else:
            return cmp(self.credits,other.credits)


    def pop_student(self):
        return heapq.heappop(Student.student_list)

    def enrol(self, _class):
        self.credits -= _class.get_required_credits()
        self.student_schedule[_class.period] = _class.class_num

    def requeue(self):
        Student.student_list_alt.append(self)




    #Depricated. It's more likely that we'll end up just calling the whole thing again the next day/other
    def static_reshuffle(self):
        for student in  Student.student_list_alt:
            if(None in student.student_schedule):
                student.request_bet()
                heapq.heappush(Student.student_list,student)
            Student.student_list_alt.remove(student)
