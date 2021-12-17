import sqlite3

from Classes import room
from Classes.Meetingtime import MeetingTime
from Classes.course import Course
from Classes.department import Department
from Classes.instructor import Instructor


class Connection:
    def __init__(self):
        self.sqliteConnection = sqlite3.connect('TimeTable_1 (1).db')
        self.cursor = self.sqliteConnection.cursor()
        self.courses = self.select_courses()
        self.instructors = self.select_instructors()
        self.rooms = self.select_rooms()
        self.meetingTimes = self.select_meeting_times()
        self.departments = self.select_departments()
        self.numberOfClasses = 0
        for i in range(0, len(self.departments)):
            self.numberOfClasses += len(self.departments[i].get_courses())

    def select_courses(self):
        self.cursor.execute("SELECT * FROM courses")
        courses = self.cursor.fetchall()
        returnCourses = []
        for i in range(0, len(courses)):
            returnCourses.append(
                Course.Course(courses[i][0], courses[i][1], self.select_course_instructors(courses[i][0]),
                              courses[i][2]))
        return returnCourses

    def select_instructors(self):
        self.cursor.execute("SELECT * FROM instructor")
        instructors = self.cursor.fetchall()
        returnInstructors = []
        for i in range(0, len(instructors)):
            returnInstructors.append(Instructor.Instructor(instructors[i][0], instructors[i][1]))
        return returnInstructors

    def select_meeting_times(self):
        self.cursor.execute("SELECT * FROM meeting_time")
        meetingTimes = self.cursor.fetchall()
        returnMeetingTimes = []
        for i in range(0, len(meetingTimes)):
            returnMeetingTimes.append(MeetingTime.MeetingTime(meetingTimes[i][0], meetingTimes[i][1]))
        return returnMeetingTimes

    def select_departments(self):
        self.cursor.execute("SELECT * FROM departments")
        departments = self.cursor.fetchall()
        returndepartments = []
        for i in range(0, len(departments)):
            returndepartments.append(Department.Department(departments[i][0], self.select_dept_courses(departments[i][0])))
        return returndepartments

    def select_course_instructors(self, courseNumber):
        self.cursor.execute("SELECT * FROM course_instructor where course_number == '" + courseNumber + "'")
        Instructor_Numbers = self.cursor.fetchall()
        instructorNumbers = []
        for i in range(0, len(Instructor_Numbers)):
            instructorNumbers.append(Instructor_Numbers[i][1])
        returnCourseInstructor = []
        for i in range(0, len(self.instructors)):
            if self.instructors[i].get_id() in instructorNumbers:
                returnCourseInstructor.append(self.instructors[i])
        return returnCourseInstructor

    def select_dept_courses(self, deptName):
        self.cursor.execute("SELECT * FROM dept_course where dept_name == '" + deptName + "'")
        Course_Numbers = self.cursor.fetchall()
        courseNumbers = []
        for i in range(0, len(Course_Numbers)):
            courseNumbers.append(Course_Numbers[i][1])
        returnDeptCourses = []
        for i in range(0, len(self.courses)):
            if self.courses[i].get_number() in courseNumbers:
                returnDeptCourses.append(self.courses[i])
        return returnDeptCourses

    def select_rooms(self):
        self.cursor.execute("SELECT * FROM room")
        rooms = self.cursor.fetchall()
        returnRooms = []
        for i in range(0, len(rooms)):
            returnRooms.append(room.room(rooms[i][0], rooms[i][1]))
        return returnRooms

    def get_rooms(self):
        return self.rooms

    def get_instructors(self):
        return self.instructors

    def get_courses(self):
        return self.courses

    def get_departments(self):
        return self.departments

    def get_meetingTimes(self):
        return self.meetingTimes

    def get_numberOfClasses(self):
        return self.numberOfClasses
