class Schoolsystem:
    def __init__(self,name,age,ID):
        self.name=name
        self.age=age
        self.ID=ID
    def get_info(self):
        return self.name,self.age,self.ID
class Students(Schoolsystem):
    def __init__(self, name, age, ID, grade):
        super().__init__(name, age, ID)
        self.grade=grade
        self.classesofstu=[]

    def insert_classes(self,str1):
        return self.classesofstu.append(str1)
        
    def get_students(self):
        return self.name,self.age,self.ID,self.ID,self.grade,self.classesofstu
    
class Teacher(Schoolsystem):
    def __init__(self, name, age, ID,subject):
        super().__init__(name, age, ID)
        self.subject=subject
        self.classesofteach=[]
    def insert_class(self,clas):
        return self.classesofteach.append(clas)
    def get_teacher(self):
        return self.name,self.age,self.ID,self.subject,self.classesofteach
class Administrator(Schoolsystem):
    def __init__(self, name, age, ID,departrment):
        super().__init__(name, age, ID)
        self.department=departrment
        self.employees=[]
    def insert_employees(self,employes):
        return self.employees.append(employes)
    def get_administrator(self):
        return self.name,self.age,self.ID,self.department,self.employees

student1=Students("Ali",18,274545986,'B+')
student1.insert_classes('biology')
student1.insert_classes('physics')
student1.insert_classes('chemistry')
print(student1.get_students())

teacher1=Teacher("Muhammad",35,1223445,'Physisc')
teacher1.insert_class("27B")
teacher1.insert_class("10A")
teacher1.insert_class('34C')
print(teacher1.get_teacher())

admin1=Administrator("Sam",47,9123,'Logistics')
admin1.insert_employees('Ali')
admin1.insert_employees("Modean")
admin1.insert_employees("John")
print(admin1.get_administrator())
