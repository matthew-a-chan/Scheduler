import Student

class Class:
    class_list = []
    num_classes=0

    #demand

    def __init__(self, _id, _title, _teacher, _period, _max_capacity, _current_capacity):
        if(_title != None):
            self.id = _id
            self.demand = 0
            self.title = _title
            self.teacher = _teacher
            self.period = _period
            self.max_capacity = _max_capacity
            

            self.current_capacity = _current_capacity
            self.seats=self.max_capacity-self.current_capacity
            #self.current_students = []

            self.class_num=Class.num_classes
            Class.num_classes+=1

            Class.class_list.append(self)
        else:
            print("DUMMY CLASS MADE")

    def increment_demand(self):
        self.demand = self.demand+1

    def get_demand(self):
        return self.demand

    def get_teacher(self):
        return self.teacher

    def get_period(self):
        return self.period

    #Returns the demand (number of people who signed up) / maximum capacity * 10 (ie: 60 signups, 20 seats, * 10 --> 30 credits)
    def get_required_credits(self):
        if(self.seats>0):
            return int(float(self.demand)/self.seats*10)
        return 0

    def is_full(self):
        return self.current_capacity >= self.max_capacity

    def enrol_student(self, student):
        #self.current_students.append(student)
        self.current_capacity += 1
