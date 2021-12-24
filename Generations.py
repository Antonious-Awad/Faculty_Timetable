import prettytable as pt

import Connection

connection = Connection.Connection()


class Generations:
    def print_data(self):
        print( "All Data" )
        self.print_Courses()
        self.print_Instructors()
        self.print_Departments()
        self.print_Rooms()
        self.print_MeetingTimes()

    def Department_Courses(self):
        departments = connection.get_departments()
        departmentCourses = []
        for i in range( 0, len( departments ) ):
            courses = departments.__getitem__( i ).get_courses()
            Courseslist = []
            for j in range( 0, len( courses ) ):
                Courseslist.append( courses[j].get_name() )
            Courseslist_str = ', '.join( Courseslist )
            departmentCourses.insert( 0, [departments[i].get_name(), Courseslist_str] )
        return departmentCourses

    def Courses(self):
        courses = connection.get_courses()
        coursesList = []
        for i in range( 0, len( courses ) ):
            instructors = courses.__getitem__( i ).get_instructors()
            InstructorsList = []
            for j in range( 0, len( instructors ) ):
                InstructorsList.append( instructors[j].get_name() )
            coursesList.insert( 0, [courses[i].get_number(), courses[i].get_name(), courses[i].get_maxNumOfStudents(),
                                    str( ', '.join( InstructorsList ) )] )
        return coursesList

    def Rooms(self):
        rooms = connection.get_rooms()
        roomsList = []
        for i in range( 0, len( rooms ) ):
            roomsList.insert( 0, [rooms[i].get_room_number(), rooms[i].get_room_capacity()] )
        return roomsList

    def Instructors(self):
        instructors = connection.get_instructors()
        instructorList = []
        for i in range( 0, len( instructors ) ):
            instructorList.insert( 0, [instructors[i].get_name(), instructors[i].get_instructor_number()] )
        return instructorList

    def print_Departments(self):
        departments = connection.get_departments()
        availableDeptsTable = pt.PrettyTable( ['Departments', 'Courses'] )
        for i in range( 0, len( departments ) ):
            courses = departments.__getitem__( i ).get_courses()
            coursesList = []
            for j in range( 0, len( courses ) ):
                coursesList.append( courses[j].get_name() )
            availableDeptsTable.add_row( [departments[i].get_name(), coursesList] )
        print( availableDeptsTable )

    def print_Courses(self):
        courses = connection.get_courses()
        availableDeptsTable = pt.PrettyTable( ['ID', 'Course number', 'Max number of students', 'Instructors'] )
        for i in range( 0, len( courses ) ):
            instructors = courses.__getitem__( i ).get_instructors()
            instructorsList = []
            for j in range( 0, len( instructors ) ):
                instructorsList.append( instructors[j].get_name() )
            availableDeptsTable.add_row(
                [courses[i].get_number(), courses[i].get_name(), courses[i].get_maxNumOfStudents(),
                 str( ', '.join( instructorsList ) )] )
        print( availableDeptsTable )

    def print_Rooms(self):
        rooms = connection.get_rooms()
        availableDeptsTable = pt.PrettyTable( ['Room number', 'Maximum Capacity'] )
        for i in range( 0, len( rooms ) ):
            availableDeptsTable.add_row( [rooms[i].get_number(), rooms[i].get_capacity()] )
        print( availableDeptsTable )

    def print_Instructors(self):
        instructors = connection.get_instructors()
        availableDeptsTable = pt.PrettyTable( ['ID', 'Instructor'] )
        for i in range( 0, len( instructors ) ):
            availableDeptsTable.add_row( [instructors[i].get_id(), instructors[i].get_name()] )

    def print_MeetingTimes(self):
        meetingTimes = connection.get_meetingTimes()
        availableDeptsTable = pt.PrettyTable( ['ID', 'Meeting Time'] )
        for i in range( 0, len( meetingTimes ) ):
            availableDeptsTable.add_row( [meetingTimes[i].get_id(), meetingTimes[i].get_time()] )

    def print_generation(self, population):
        generationTable = pt.PrettyTable(
            ['schedule', 'fitness', 'Number of conflicts', 'classes [dept, class, room, instructor, meeting-time]'] )
        schedules = population.get_schedules()
        for i in range( 0, len( schedules ) ):
            classes = schedules.__getitem__( i ).get_classes()
            curClasses = []
            for j in range( 0, len( classes ) ):
                curClasses.append(
                    classes[j].get_dept().get_name() + ',' + classes[j].get_course().get_number() + ',' + classes[
                        j].get_room().get_room_number() + ',' + classes[
                        j].get_meetingTime().get_id() )
            generationTable.add_row(
                [str( i + 1 ), round( schedules[i].get_fitness(), 3 ), schedules[i].get_numOfConflicts(),
                 str( ', '.join( curClasses ) )] )
        return generationTable

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = pt.PrettyTable(
            ['Class Numbers', 'Departments', 'Course (number, max Number of students)', 'Room (Capacity)',
             'Instructor (ID)',
             'Meeting Time (ID)'] )
        for i in range( 0, len( classes ) ):
            table.add_row( [str( i + 1 ), classes[i].get_dept().get_name(),
                            classes[i].get_course().get_name() + ' (' + classes[
                                i].get_course().get_number() + ', ' + str(
                                classes[i].get_course().get_maxNumOfStudents() ) + ')',
                            classes[i].get_room().get_room_number() + ' (' + str(
                                classes[i].get_room().get_room_capacity() ) + ')',
                            classes[i].get_instructor().get_name() + ' (' + str(
                                classes[i].get_instructor().get_instructor_number() ) + ')',
                            classes[i].get_meetingTime().get_time() + ' (' + str(
                                classes[i].get_meetingTime().get_id() ) + ')'] )
        return table

    def get_generated(self, schedule):
        classes = schedule.get_classes()
        table_data = []
        for i in range( 0, len( classes ) ):
            table_data.insert( 0, [str( i + 1 ), classes[i].get_dept().get_name(),
                                   classes[i].get_course().get_name() + ' (' + classes[
                                       i].get_course().get_number() + ', ' + str(
                                       classes[i].get_course().get_maxNumOfStudents() ) + ')',
                                   classes[i].get_room().get_room_number() + ' (' + str(
                                       classes[i].get_room().get_room_capacity() ) + ')',
                                   classes[i].get_instructor().get_name() + ' (' + str(
                                       classes[i].get_instructor().get_instructor_number() ) + ')',
                                   classes[i].get_meetingTime().get_time() + ' (' + str(
                                       classes[i].get_meetingTime().get_id() ) + ')'] )
        return table_data
