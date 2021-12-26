import tkinter as tk
from tkinter import *
from tkinter import ttk

import Connection
import GA
import Generations
import Population

connection = Connection.Connection()
generations = Generations.Generations()

POPULATION_NUM = 9


def main():
    global root
    root = Tk()
    root.title( 'Data' )
    root.geometry( "700x500" )
    root['background'] = '#856ff8'

    instructortree = ttk.Treeview( root )
    coursestree = ttk.Treeview( root )
    deptartmenttree = ttk.Treeview( root )
    roomstree = ttk.Treeview( root )

    instructortree['columns'] = ("id", "Name")
    coursestree['columns'] = ("number", "Name", "Max no")
    deptartmenttree['columns'] = "Name"
    roomstree['columns'] = ("Number", "Capacity")

    instructortree.column( "#0", width=0 )
    instructortree.column( "id", anchor=W, width=100 )
    instructortree.column( "Name", anchor=CENTER, width=150 )

    coursestree.column( "#0", width=0 )
    coursestree.column( "number", anchor=W, width=100 )
    coursestree.column( "Name", anchor=CENTER, width=150 )
    coursestree.column( "Max no", anchor=CENTER, width=100 )

    roomstree.column( "#0", width=0 )
    roomstree.column( "Number", anchor=W, width=100 )
    roomstree.column( "Capacity", anchor=CENTER, width=150 )

    deptartmenttree.column( "#0", width=0 )
    deptartmenttree.column( "Name", anchor=W, width=100 )

    deptartmenttree.heading( "Name", text="Name", anchor=CENTER )

    roomstree.heading( "Number", text="Number", anchor=W )
    roomstree.heading( "Capacity", text="Capacity", anchor=CENTER )

    coursestree.heading( "number", text="number", anchor=W )
    coursestree.heading( "Name", text="Name", anchor=CENTER )
    coursestree.heading( "Max no", text="Max no", anchor=W )

    instructortree.heading( "id", text="ID", anchor=W )
    instructortree.heading( "Name", text="Name", anchor=CENTER )

    dept = generations.Department_Courses()
    for i in range( 0, len( dept ) ):
        deptartmenttree.insert( "", tk.END, values=dept[len( dept ) - 1 - i] )

    courses = generations.Courses()
    for i in range( 0, len( courses ) ):
        coursestree.insert( "", tk.END, values=courses[len( courses ) - 1 - i] )

    room = generations.Rooms()
    for i in range( 0, len( room ) ):
        roomstree.insert( "", tk.END, values=room[len( room ) - 1 - i] )

    instructor = generations.Instructors()
    for i in range( 0, len( instructor ) ):
        instructortree.insert( "", tk.END, values=instructor[len( instructor ) - 1 - i] )

    deptartmenttree.place( x=300, y=250 )
    roomstree.place( x=20, y=250 )
    instructortree.place( x=20, y=20 )
    coursestree.place( x=300, y=20 )

    Button( root, text="Generate Table", command=generateTable, width=30, height=2 ).place( x=440, y=400 )
    root.resizable( width=FALSE, height=FALSE )
    root.mainloop()


def generateTable():
    global generationslog
    generationslog = ""
    generationNumber = 1
    generationslog += "\n> Generation Number " + str( generationNumber ) + "\n"
    population = Population.Population( POPULATION_NUM )
    newpop = population.get_schedules()

    def function(newpop):
        return newpop.get_fitness()

    population.get_schedules().sort( key=function, reverse=True )
    generationslog += str( generations.print_generation( population ) )
    generationslog += str( generations.print_schedule_as_table( population.get_schedules()[0] ) )
    geneticAlgorithm = GA.GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generationNumber += 1
        generationslog += "\n> Generation  " + str( generationNumber ) + "\n"
        population = geneticAlgorithm.evolve( population )
        population.get_schedules().sort( key=function, reverse=True )
        generationslog += str( generations.print_generation( population ) )
        generationslog += str( generations.print_schedule_as_table( population.get_schedules()[0] ) )
    print( "\n\n" )

    last_gen = generations.get_generated( population.get_schedules()[0] )
    Generated_Table( last_gen )


def show_gens():
    global generationswindow
    generationswindow = Tk()
    generationswindow.title( "Faculty Time Table" )
    generationswindow.geometry( '1300x700' )

    gens_text = Text( generationswindow )
    gens_text.insert( 'end', generationslog )
    gens_text.config( font=("Courier", 8), state=DISABLED )

    gens_text.pack( expand=1, fill=tk.BOTH )
    Scrollbar( generationswindow )
    generationswindow.mainloop()


def Generated_Table(last_gen):
    global table
    table = Tk()
    table.title( "Faculty Time Table" )
    table.geometry( '1000x400' )
    table.resizable( False, False )

    top_frame = Frame( table )
    bottom_frame = Frame( table )

    generated = ttk.Treeview( top_frame, selectmode='browse' )

    top_frame.pack( anchor="n", padx=5, pady=5, fill=tk.X )
    bottom_frame.pack( anchor="n", padx=5, pady=15 )

    generated.pack()

    # Defining number of columns
    generated["columns"] = ("1", "2", "3", "4", "5", "6")

    # Defining heading
    generated['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    generated.column( "1", width=60, anchor='c' )
    generated.column( "2", width=60, anchor='c' )
    generated.column( "3", width=200, anchor='c' )
    generated.column( "4", width=120, anchor='c' )
    generated.column( "5", width=200, anchor='c' )
    generated.column( "6", width=300, anchor='c' )

    # Assigning the heading names to the
    # respective columns
    generated.heading( "1", text="Class ID" )
    generated.heading( "2", text="Dept" )
    generated.heading( "3", text="Course (number, Number of students)" )
    generated.heading( "4", text="Room (Capacity)" )
    generated.heading( "5", text="ID (Instructor)" )
    generated.heading( "6", text="ID (Meeting Time)" )

    for i in range( 0, len( last_gen ) ):
        generated.insert( "", tk.END, values=last_gen[len( last_gen ) - 1 - i] )

    log_Btn = Button( bottom_frame, text="Show Generations", command=show_gens, bg='#856ff8', fg='white', width=120,
                      height=5 )
    log_Btn.pack( anchor='nw' )

    table.mainloop()


if __name__ == "__main__":
    main()