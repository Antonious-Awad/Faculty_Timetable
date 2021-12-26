import os.path
import sqlite3 as sqlite
from tkinter import *
from tkinter import ttk

import Connection
import main

connection = Connection.Connection()

BASE_DIR = os.path.dirname( os.path.abspath( __file__ ) )
db_path = os.path.join( BASE_DIR, "TimeTable.db" )
conn = sqlite.connect( db_path )

cursor = conn.cursor()

global insertdata
insertdata = Tk()
insertdata.title( 'Data' )
insertdata.geometry( "1500x750" )
insertdata['background'] = '#856ff8'
pw = PanedWindow( insertdata, orient=VERTICAL )
pw.pack()
test = PanedWindow( insertdata, orient=HORIZONTAL )
inst = ttk.Frame( pw, relief=SUNKEN, width=1500, height=250 )
course = ttk.Frame( pw, relief=SUNKEN, width=1500, height=350 )
pw.add( inst )
pw.add( course )

# instructor form
intformlabel = Label( insertdata, text='Instructor', font=('bold', 16) )
intformlabel.place( x=10, y=10 )
inst_name = StringVar()
inst_number = StringVar()
instructor_name = Entry( insertdata, textvar=inst_name, width=30 )
instructor_name.place( x=150, y=50 )
inst_label = Label( insertdata, text='instructor name', width=11, font=('bold', 12) )
inst_label.place( x=15, y=50 )
instructor_number = Entry( insertdata, textvar=inst_number, width=30 )
instructor_number.place( x=150, y=100 )
inst_num_label = Label( insertdata, text='instructor ID', width=11, font=('bold', 12) )
inst_num_label.place( x=15, y=100 )


def add_inst():
    connection.insert_instruct( instructor_number.get(), instructor_name.get() )


instbutton = Button( insertdata, text="insert", width=20, height=2, command=add_inst ).place( x=200, y=150 )

# course
courseformlabel = Label( insertdata, text='Course', font=('bold', 16) )
courseformlabel.place( x=780, y=10 )
course_name = StringVar()
course_number = StringVar()
maxnum = IntVar()
coursename = Entry( insertdata, textvar=course_name, width=30 )
coursename.place( x=900, y=50 )
max_num = Entry( insertdata, textvar=maxnum, width=30 )
max_num.place( x=900, y=150 )
coursename_label = Label( insertdata, text='Course name', width=11, font=('bold', 12) )
coursename_label.place( x=780, y=50 )
max_label = Label( insertdata, text='students num', width=11, font=('bold', 12) )
max_label.place( x=780, y=150 )
coursenumber = Entry( insertdata, textvar=course_number, width=30 )
coursenumber.place( x=900, y=100 )
course_num_label = Label( insertdata, text='course ID', width=11, font=('bold', 12) )
course_num_label.place( x=780, y=100 )
#####################################


connection.cursor.execute( "SELECT * FROM Departments" )
deptgui = connection.cursor.fetchall()
deptsforgui = []
for i in range( 0, len( deptgui ) ):
    deptsforgui.append( deptgui[i][0] )

deptt = StringVar( insertdata )
deptt.set( deptsforgui[0] )  # Set the first value to# be the default option

w = OptionMenu( *(insertdata, deptt) + tuple( deptsforgui ) )
w.place( x=1100, y=45, width=100 )

#############################################

connection.cursor.execute( "SELECT Number FROM Instructor" )
instgui = connection.cursor.fetchall()
instforgui = []
for i in range( 0, len( instgui ) ):
    instforgui.append( instgui[i][0] )

instt = StringVar( insertdata )
instt.set( instforgui[0] )  # Set the first value to# be the default option

inst_ = OptionMenu( *(insertdata, instt) + tuple( instforgui ) )
inst_.place( x=1100, y=90, width=150 )


def add_course():
    connection.insert_courses( course_number.get(), course_name.get(), maxnum.get() )


def add_deptcoure():
    connection.insert_Deptcourse( deptt.get(), course_number.get() )


def add_instcourse():
    connection.insert_instcourse( course_number.get(), instt.get() )


def func1(evt=None):
    add_course()
    add_deptcoure()
    add_instcourse()


course_button = Button( insertdata, text="insert", width=20, height=2, command=func1 ).place(
    x=1000, y=200 )

# room
roomformlabel = Label( insertdata, text='Room', font=('bold', 16) )
roomformlabel.place( x=10, y=300 )
room_id = StringVar()
room_cap = IntVar()
roomnum = Entry( insertdata, textvar=room_id, width=30 )
roomnum.place( x=150, y=350 )
roomcap = Entry( insertdata, textvar=room_cap, width=30 )
roomcap.place( x=150, y=400 )
roomnum_label = Label( insertdata, text='Room number', width=11, font=('bold', 12) )
roomnum_label.place( x=10, y=350 )
roomcap_label = Label( insertdata, text='room Capacity', width=11, font=('bold', 12) )
roomcap_label.place( x=10, y=400 )


def add_room():
    connection.insert_room( room_id.get(), room_cap.get() )


room_button = Button( insertdata, text="insert", width=20, height=2, command=add_room ).place( x=250, y=450 )

# dept
deptformlabel = Label( insertdata, text='Department', font=('bold', 16) )
deptformlabel.place( x=780, y=300 )
deptname = StringVar()
dept_name = Entry( insertdata, textvar=deptname, width=30 )
dept_name.place( x=920, y=350 )
dept_label = Label( insertdata, text='Department name', width=15, font=('bold', 12) )
dept_label.place( x=780, y=350 )


def add_dept():
    connection.insert_dept( deptname.get() )


dept_button = Button( insertdata, text="insert", width=20, height=2, command=add_dept ).place( x=1000, y=450 )

dept_button = Button( insertdata, text="insert", width=20, height=2, command=add_dept ).place( x=1000, y=450 )
Button( insertdata, text="Show available data", command=main.main, width=30, height=2,
        font=('bold', 14) ).place( x=1000, y=625 )

insertdata.mainloop()
