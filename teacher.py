from person import Person

class Teacher(Person):

    def __init__(self, name, family, emp_code):
        super().__init__(name, family)
        self.__emp_code = emp_code


    def set_emp_code(self, new_emp_code):
        if new_emp_code > 0:
            self.__emp_code = new_emp_code
            print("EMP code has just changed!")
        else:
            print("Entered Value is not valid!")

    def get_emp_code(self):
        return self.__emp_code