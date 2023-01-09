class student:
    school_name="abc"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("student",self.name,self.age,student.school_name)
    def change_age(self,new_age):
        #modify instance variable
        self.age=new_age
    #class method
    @classmethod
    def modify_student_name(self,new_name):
        #modify class variable
        self.school_name=new_name
s1=student("hari",11)
#call instance methods
s1.show()
s1.change_age(14)
#call class_method
s1.modify_school_name("BMC")
s1.show()

