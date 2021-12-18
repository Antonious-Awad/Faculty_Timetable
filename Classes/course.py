class Course:
    def __init__(self, number, name, instructors, maxNumOfStudents ):
        self._number = number
        self._name = name
        self._maxNumOfStudents = maxNumOfStudents
        self._instructors = instructors

    def get_number(self): return self._number

    def get_name(self): return self._name

    def get_maxNumOfStudents(self): return self._maxNumOfStudents

    def get_instructors(self): return  self._instructors
    def __str__(self): return self._name
