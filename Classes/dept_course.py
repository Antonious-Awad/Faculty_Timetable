class Dept_course:
    def _init_(self, dept_course_name, course_number):
        self.dept_course_name = dept_course_name
        self.course_number = course_number

    def get_dept_course(self):
        return "deptartment course name:" + self.dept_course_name + ", course number:" + self.course_number
