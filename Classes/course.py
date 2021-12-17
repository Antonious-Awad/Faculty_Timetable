class Course:
    def __init__(self, number, name, maxNumOfStudents):
        self._number = number
        self._name = name
        self._maxNumOfStudents = maxNumOfStudents

    def get_number(self): return self._number

    def get_name(self): return self._name

    def get_maxNumOfStudents(self): return self._maxNumOfStudents

    def __str__(self): return self._name
