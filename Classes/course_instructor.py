class course_instructor:
  def __init__(self,course_number,insturctor_number):
    self._course_number = course_number
    self._instructor_number = insturctor_number
  
  def get_course_instructor(self):
    return "Course Number: " + self._course_number + "\nInstructor Number: " + self._instructor_number
