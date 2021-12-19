class Instructor:
    def __init__(self, instructor_name, instructor_number):
        self.instructor_name = instructor_name
        self.instructor_number = instructor_number

    def get_instructor(self):
        return "instructor:" + self.instructor_name + ", instructor number:" + self.instructor_number

    def get_name(self):
        return self.instructor_name

    def get_instructor_number(self):
        return self.instructor_number
