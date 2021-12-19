import prettytable as prettyTable
import random
import os.path

from tkinter import *
from tkinter import ttk
import tkinter as tk

import Population
import GA
import Generations
import Connection

POPULATION_SIZE = 9

connection = Connection.Connection()

generations = Generations.Generations()


# displayMgr.print_available_data()

def generateTable():
    global logGens
    logGens = ""
    generationNumber = 1
    logGens += "\n> Generation # " + str( generationNumber ) + "\n"
    population = Population.Population( POPULATION_SIZE )
    population.get_schedules().sort( key=lambda x: x.get_fitness(), reverse=True )
    logGens += str( generations.print_generation( population ) )
    logGens += str( generations.print_schedule_as_table( population.get_schedules()[0] ) )
    geneticAlgorithm = GA.GeneticAlgorithm()
    while population.get_schedules()[0].get_fitness() != 1.0:
        population: object = geneticAlgorithm.evolve( population )
        population.get_schedules().sort(key=lambda x: x.get_fitness(),reverse= True)
        logGens += str( generations.print_generation( population ) )
        logGens += str( generations.print_schedule_as_table( population.get_schedules()[0] ) )
    print( "\n\n" )

    root.destroy()
    last_gen = generations.get_generated( population.get_schedules()[0] )
    Generated_Table( last_gen )


def main():
    global root
    root = Tk()
    root.title( "Faculty Time Table" )
    root.geometry( '600x600' )
    root.resizable( False, False )

    top_left_frame = Frame( root )
    bottom_left_frame = Frame( root )
    bottom_frame = Frame( root )

    depts_tree = ttk.Treeview( bottom_left_frame, selectmode='browse' )

    courses_tree = ttk.Treeview( top_left_frame, selectmode='browse' )

    rooms_tree = ttk.Treeview( bottom_left_frame, selectmode='browse' )

    top_left_frame.pack( anchor="n", padx=5, pady=5, fill=tk.X )
    bottom_left_frame.pack( anchor="n", padx=5, pady=15 )
    bottom_frame.pack( anchor="n", padx=5, pady=15 )

    courses_tree.pack()
    depts_tree.pack( side=LEFT )
    rooms_tree.pack( padx=5 )

    # Defining number of columns
    depts_tree["columns"] = ("1", "2")

    courses_tree["columns"] = ("1", "2", "3", "4")

    rooms_tree["columns"] = ("1", "2")

    # Defining heading
    depts_tree['show'] = 'headings'

    courses_tree['show'] = 'headings'

    rooms_tree['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    depts_tree.column( "1", width=90, anchor='c' )
    depts_tree.column( "2", width=188, anchor='c' )

    courses_tree.column( "1", width=60, anchor='c' )
    courses_tree.column( "2", width=90, anchor='c' )
    courses_tree.column( "3", width=60, anchor='c' )
    courses_tree.column( "4", width=350, anchor='c' )

    rooms_tree.column( "1", width=90, anchor='c' )
    rooms_tree.column( "2", width=185, anchor='c' )

    # Assigning the heading names to the
    # respective columns
    depts_tree.heading( "1", text="Department" )
    depts_tree.heading( "2", text="Courses" )

    courses_tree.heading( "1", text="id" )
    courses_tree.heading( "2", text="Course #" )
    courses_tree.heading( "3", text="Max # of students" )
    courses_tree.heading( "4", text="Instructors" )

    rooms_tree.heading( "1", text="Room #" )
    rooms_tree.heading( "2", text="Max Seating Capacity" )

    dept_courses = generations.Department_Courses()
    for i in range( 0, len( dept_courses ) ):
        depts_tree.insert( "", tk.END, values=dept_courses[len( dept_courses ) - 1 - i] )

    courses_data = generations.Courses()
    for i in range( 0, len( courses_data ) ):
        courses_tree.insert( "", tk.END, values=courses_data[len( courses_data ) - 1 - i] )

    rooms_data = generations.Rooms()
    for i in range( 0, len( rooms_data ) ):
        rooms_tree.insert( "", tk.END, values=rooms_data[len( rooms_data ) - 1 - i] )

    generate_btn = Button( bottom_frame, text="Generate Table", command=generateTable, bg='blue', fg='white', width=79,
                           height=5 )
    generate_btn.pack( anchor='nw' )

    root.mainloop()


def show_gens():
    global root3
    root3 = Tk()
    root3.title( "Faculty Time Table" )
    root3.geometry( '1200x600' )
    root3.resizable( False, False )

    gens_text = Text( root3 )
    gens_text.insert( 'end', logGens )
    gens_text.config( font=("Courier", 8), state=DISABLED )

    gens_text.pack( expand=1, fill=tk.BOTH )

    root3.mainloop()


def Generated_Table(last_gen):
    global root2
    root2 = Tk()
    root2.title( "Faculty Time Table" )
    root2.geometry( '900x400' )
    root2.resizable( False, False )

    menubar = Menu( root2 )
    filemenu = Menu( menubar, tearoff=0 )
    filemenu.add_command( label="Home", command=lambda: [root2.destroy(), main()] )
    filemenu.add_command( label="Exit", command=root2.destroy )
    menubar.add_cascade( label="File", menu=filemenu )

    top_frame = Frame( root2 )
    bottom_frame = Frame( root2 )

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
    generated.column( "6", width=200, anchor='c' )

    # Assigning the heading names to the
    # respective columns
    generated.heading( "1", text="Class #" )
    generated.heading( "2", text="Dept" )
    generated.heading( "3", text="Course (number, max # of students)" )
    generated.heading( "4", text="Room (Capacity)" )
    generated.heading( "5", text="Instructor (id)" )
    generated.heading( "6", text="Meeting Time (id)" )

    for i in range( 0, len( last_gen ) ):
        generated.insert( "", tk.END, values=last_gen[len( last_gen ) - 1 - i] )

    log_Btn = Button( bottom_frame, text="Show Generations", command=show_gens, bg='blue', fg='white', width=120,
                      height=5 )
    log_Btn.pack( anchor='nw' )

    root2.config( menu=menubar )
    root2.mainloop()


if __name__ == "__main__":
    main()