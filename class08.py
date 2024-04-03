# class created
class Student:
    """ This is doc string for Student class """
    school_name    = "CDAC"
    
    @classmethod
    def get_my_school_name(cls):
        return cls.school_name
    
    @classmethod
    def set_school_name(cls,new_school_name):
        cls.school_name = new_school_name
    
    def __init__(self,rcv_name) :
        print(self)
        self.__name = rcv_name
    
    def get_my_name(self):
        return self.__name  
    
    @staticmethod
    def my_static_method():
        print("some task related to the class ")  


# object var created
gaurav= Student("GAURAV")
gaurav_copy= Student("GAURAV_COPY")

print(gaurav.get_my_name())
print(gaurav_copy.get_my_name())

print(Student.get_my_school_name())
print(gaurav.school_name)

Student.my_static_method()
gaurav.my_static_method()


Student.set_school_name("My New school")
print(Student.get_my_school_name())
print(gaurav.school_name)
print(gaurav_copy.school_name)

gaurav.school_name = "gaurav new school name"
print("-----------------------------------")
print(Student.get_my_school_name())
print(gaurav.school_name)
print(gaurav_copy.school_name)


# # Deleting Attributes student_pocket_money
del gaurav.school_name
print("-----------------------------------")
print(Student.get_my_school_name())
print(gaurav.school_name)
print(gaurav_copy.school_name)

# delete entire object
del gaurav
print("-----------------------------------")
## print(gaurav.school_name)


print(dir(Student))
print(Student.__doc__)