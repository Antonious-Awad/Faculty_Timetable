import sqlite3

from Classes import Meetingtime
from Classes import course
from Classes import department
from Classes import instructor
from Classes import room


class Connection:
    def __init__(self):
        self.sqliteConnection = sqlite3.connect( 'TimeTable.db' )
        self.cursor = self.sqliteConnection.cursor()
        self.instructor = self.select_instructors()
        self.courses = self.select_courses()
        self.rooms = self.select_rooms()
        self.meetingTimes = self.select_meeting_times()
        self.departments = self.select_departments()
        self.numberOfClasses = 0
        for i in range( 0, len( self.departments ) ):
            self.numberOfClasses += len( self.departments[i].get_courses() )

    def insert_instruct(self, instructor_numberdb, instructor_namedb):
        self.cursor.execute( "INSERT INTO Instructor  (Number, Name) VALUES (?, ?)",
                             (instructor_numberdb, instructor_namedb) );
        self.sqliteConnection.commit();
        self.sqliteConnection.close();

    def insert_dept(self, dept_name):
        self.cursor.execute( "INSERT INTO Departments (Name) VALUES (?)", [dept_name] );
        self.sqliteConnection.commit();
        self.sqliteConnection.close();

    def insert_courses(self, course_numberdb, course_namedb, max_num_db):
        self.cursor.execute( "INSERT INTO Courses  (Number, Name,MaxNoOfStudents) VALUES (?,?,?)",
                             (course_numberdb, course_namedb, max_num_db) );
        self.sqliteConnection.commit();
        self.sqliteConnection.close();

    def insert_room(self, roomnum, capacity):
        self.cursor.execute( "INSERT INTO Room  (Number, Capacity) VALUES (?, ?)",
                             (roomnum, capacity) );
        self.sqliteConnection.commit();
        self.sqliteConnection.close();

    def insert_Deptcourse(self, deptname, courseid):
        self.cursor.execute( "INSERT INTO DeptCourses  (DeptName,Course_Number) VALUES (?, ?)",
                             (deptname, courseid) );
        self.sqliteConnection.commit();
        self.sqliteConnection.close();

    # def get_inst_byname(self, instructid):
    #    self.cursor.execute( "SELECT Number FROM Instructor where Name == '" + instructid + "'" )
    #   val = self.cursor.fetchone()
    #  return val

    def insert_instcourse(self, courseid, instructid):
        self.cursor.execute( "INSERT INTO CourseInstructor( Course_Number, Instructor_Number ) VALUES(?,?)",
                             (courseid, instructid) )
        self.sqliteConnection.commit();
        self.sqliteConnection.close();

    # inst id where name == name from gui
    # values

    def select_courses(self):
        self.cursor.execute( "SELECT * FROM Courses" )
        courses = self.cursor.fetchall()
        returnCourses = []
        for i in range( 0, len( courses ) ):
            returnCourses.append(
                course.Course( courses[i][0], courses[i][1], self.select_course_instructors( courses[i][0] ),
                               courses[i][2] ) )
        return returnCourses

    def select_instructors(self):
        self.cursor.execute( "SELECT * FROM Instructor" )
        instructors = self.cursor.fetchall()
        returnInstructors = []
        for i in range( 0, len( instructors ) ):
            returnInstructors.append( instructor.Instructor(
                instructors[i][0], instructors[i][1] ) )
        return returnInstructors

    def select_meeting_times(self):
        self.cursor.execute( "SELECT * FROM MeetingTime" )
        meetingTimes = self.cursor.fetchall()
        returnMeetingTimes = []
        for i in range( 0, len( meetingTimes ) ):
            returnMeetingTimes.append( Meetingtime.MeetingTime(
                meetingTimes[i][0], meetingTimes[i][1] ) )
        return returnMeetingTimes

    def select_departments(self):
        self.cursor.execute( "SELECT * FROM Departments" )
        departments = self.cursor.fetchall()
        returndepartments = []
        for i in range( 0, len( departments ) ):
            returndepartments.append(
                department.Department( departments[i][0], self.select_dept_courses( departments[i][0] ) ) )
        return returndepartments

    def select_depts_gui(self):
        self.cursor.execute( "SELECT * FROM Departments" )
        deptgui = self.cursor.fetchall()
        deptsforgui = []
        for i in range( 0, len( deptgui ) ):
            deptsforgui.append( deptgui[i][0] )
        return deptsforgui

    def select_course_instructors(self, courseNumber):
        self.cursor.execute(
            "SELECT * FROM CourseInstructor where Course_Number == '" + courseNumber + "'" )
        Instructor_Numbers = self.cursor.fetchall()
        instructorNumbers = []
        for i in range( 0, len( Instructor_Numbers ) ):
            instructorNumbers.append( Instructor_Numbers[i][1] )
        returnCourseInstructor = []
        for i in range( 0, len( instructorNumbers ) ):
            if self.instructor[i].get_instructor_number() in instructorNumbers:
                returnCourseInstructor.append( self.instructor[i] )
        return returnCourseInstructor

    def select_dept_courses(self, deptName):
        self.cursor.execute(
            "SELECT * FROM DeptCourses where DeptName == '" + deptName + "'" )
        Course_Numbers = self.cursor.fetchall()
        courseNumbers = []
        for i in range( 0, len( Course_Numbers ) ):
            courseNumbers.append( Course_Numbers[i][1] )
        returnDeptCourses = []
        for i in range( 0, len( self.courses ) ):
            if self.courses[i].get_number() in courseNumbers:
                returnDeptCourses.append( self.courses[i] )
        return returnDeptCourses

    def select_rooms(self):
        self.cursor.execute( "SELECT * FROM Room" )
        rooms = self.cursor.fetchall()
        returnRooms = []
        for i in range( 0, len( rooms ) ):
            returnRooms.append( room.room( rooms[i][0], rooms[i][1] ) )
        return returnRooms

    def get_rooms(self):
        return self.rooms

    def get_instructors(self):
        return self.instructor

    def get_courses(self):
        return self.courses

    def get_departments(self):
        return self.departments

    def get_meetingTimes(self):
        return self.meetingTimes

    def get_numberOfClasses(self):
        return self.numberOfClasses
