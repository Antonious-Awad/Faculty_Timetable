import random

import Connection
from Classes import Class

connection = Connection.Connection()


class Schedule:
    def __init__(self):
        self._connection = connection
        self._classes = []
        self._numOfConflicts = 0
        self._fitness = -1
        self._classNo = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numOfConflicts(self):
        return self._numOfConflicts

    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialization(self):
        departments = self._connection.get_departments()
        for i in range(0, len(departments)):
            courses = departments[i].get_courses()
            for j in range(0, len(courses)):
                CurrentClass = Class.Class(self._classNo, departments[i], courses[j])
                self._classNo += 1
                CurrentClass.set_meetingTime(
                    connection.get_meetingTimes()[random.randrange(0, len(connection.get_meetingTimes()))])
                CurrentClass.set_room(connection.get_rooms()[random.randrange(0, len(connection.get_rooms()))])
                CurrentClass.set_instructor(
                    connection.get_instructors()[random.randrange(0, len(connection.get_instructors()))])

                self._classes.append(CurrentClass)
        return self

    def calculate_fitness(self):
        self._numOfConflicts = 0
        classlist = self.get_classes()
        for i in range(0, len(classlist)):
            if classlist[i].get_room().get_room_capacity() < classlist[i].get_course().get_maxNumOfStudents():
                self._numOfConflicts += 1
            for j in range(0, len(classlist)):
                if j >= i:
                    if (classlist[i].get_meetingTime() == classlist[j].get_meetingTime() and classlist[i].get_id() !=
                            classlist[j].get_id()):
                        if classlist[i].get_room() == classlist[j].get_room():
                            self._numOfConflicts += 1
                        if classlist[i].get_instructor() == classlist[j].get_instructor():
                            self._numOfConflicts += 1
        return 1 / (self._numOfConflicts + 1)

    def __str__(self):
        returnValue = ""
        for i in range( 0, len( self._classes ) - 1 ):
            returnValue += str( self._classes[i] ) + ", "
        returnValue += str( self._classes[len( self._classes ) - 1] )
        return returnValue
