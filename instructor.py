class Instructor:
    def _init_(self,instructor_name,instructor_number):
        self.instructor_name = instructor_name
        self.instructor_number = instructor_number

    def get_instructor(self):

       return "instructor:" + self.instructor_name + ", instructor number:" + self.instructor_number    