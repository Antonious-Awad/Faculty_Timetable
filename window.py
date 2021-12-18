import csv
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('treeView')
root.geometry("1000x500")
root['background'] = '#856ff8'

my_tree = ttk.Treeview(root)
courses = ttk.Treeview(root)
dept = ttk.Treeview(root)
rooms = ttk.Treeview(root)
# Define Col
# have 4 cols
my_tree['columns'] = ("id", "Name")
# format col
my_tree.column("#0", width=0)
my_tree.column("id", anchor=W, width=100)
my_tree.column("Name", anchor=CENTER, width=150)

# headings

my_tree.heading("id", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=CENTER)

# add data


with open('instructor.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        id = row['number']
        Name = row['name']
        my_tree.insert("", 0, values=(id, Name))

my_tree.place(x=20, y=20)
Button(root, text='Generate Table', width=30, height=2).place(x=440, y=400)

# table courses

# Define Col
# have 4 cols
courses['columns'] = ("number", "Name", "Max no")
# format col
courses.column("#0", width=0)
courses.column("number", anchor=W, width=100)
courses.column("Name", anchor=CENTER, width=150)
courses.column("Max no", anchor=CENTER, width=100)

# headings

courses.heading("number", text="number", anchor=W)
courses.heading("Name", text="Name", anchor=CENTER)
courses.heading("Max no", text="Max no", anchor=W)

# add data


with open('courses.csv') as c:
    reader = csv.DictReader(c, delimiter=',')
    for row in reader:
        Number = row['number']
        Name = row['name']
        Max_no = row['maxNumOfStudents']
        courses.insert("", 0, values=(id, Name, Max_no))

courses.place(x=300, y=20)

# table dept

# Define Col
# have 4 cols
dept['columns'] = ("Name")
# format col
dept.column("#0", width=0)
dept.column("Name", anchor=W, width=100)

# headings

dept.heading("Name", text="Name", anchor=CENTER)

# add data


with open('departments.csv') as dp:
    reader = csv.DictReader(dp, delimiter=',')
    for row in reader:
        Name = row['name']
        dept.insert("", 0, values=(Name))

dept.place(x=300, y=250)

# have 4 cols
rooms['columns'] = ("Number", "Capacity")
# format col
rooms.column("#0", width=0)
rooms.column("Number", anchor=W, width=100)
rooms.column("Capacity", anchor=CENTER, width=150)

# headings

rooms.heading("Number", text="Number", anchor=W)
rooms.heading("Capacity", text="Capacity", anchor=CENTER)

# add data


with open('room.csv') as R:
    reader = csv.DictReader(R, delimiter=',')
    for row in reader:
        Number = row['number']
        Capacity = row['capacity']
        rooms.insert("", 0, values=(Number, Capacity))

rooms.place(x=20, y=250)

root.mainloop()
