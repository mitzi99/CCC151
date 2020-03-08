# Mitzi V. Dorato
# 2018-5849


from tkinter import *
import csv


# Columns in the csv file where fields of the student's information is saved
file_headers = ['ID Number', 'First Name', 'Last Name', 'Year Level', 'Course']
# Name of the csv file
database = 'file_students.csv'


# Quit Button
def quit_button(event):

    exit()


# Function to add a new student
def add_student(event):

    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    file_headers
    database

    student_data = []
    for field in file_headers:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("*** Student data saved successfully ***")
    return


# Function to view the students' data in the csv file
def view_students(event):

    file_headers
    database

    print("*** Student Records ***")

    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for data in file_headers:
            print(data, end=' |\t| ')
        print("\n--------------------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end=" |\t| ")
            print("\n")


# Function to search a student using ID number
def search_student(event):
    file_headers
    database

    print("*** Search Student ***")
    idnumber = input("Enter student ID Number to search: ")
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if idnumber == row[0]:
                    print("*** Student Found ***")
                    print("ID Number: ", row[0])
                    print("First Name: ", row[1])
                    print("Last Name: ", row[2])
                    print("Year Level: ", row[3])
                    print("Course: ", row[4])
                    break
        else:
            print("Student ID Nnumber is not found in our database")


# Function to update a student record using the ID number
def update_student(event):

    file_headers
    database

    print("*** Update Student ***")
    idnumber = input("Enter student ID Number to update: ")
    student = None
    updated_data = []
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if idnumber == row[0]:
                    student = counter
                    print("Student Found at row: ", student)
                    student_data = []
                    for fields in file_headers:
                        value = input("Enter " + fields + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1
        print("Student with ID Number ", idnumber, " was updated successfully")

    # Check if the student record is found or not
    if student is not None:
        with open(database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Student ID Number is not found in our database")


# Function to delete a student record by searching the student's ID number
def delete_student(event):

    file_headers
    database

    print("** Delete Student ***")
    idnumber = input("Enter student ID Number to delete: ")
    student_found = False
    updated_data = []
    with open(database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if idnumber != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student with ID Number ", idnumber, "was deleted successfully")
    else:
        print("Student ID Number is not found in our database")

#Menus Window
def menus():

    # Setting up the Gui frame
    windowFrame = Tk()
    windowFrame.geometry("570x400")

    # Setting up and placing text in the Gui frame
    welcomelabel = Label(windowFrame, text="Welcome to MSU Student Management System", font=('Times New Roman', '15'))
    welcomelabel.grid(row=0, columnspan=6)

    # Placing an image in the gui frame
    img = PhotoImage(file="seal.png")
    imglabel = Label(windowFrame, image=img)
    imglabel.grid(row=1, columnspan=6)

    # Setting up and placing a button in the Gui frame that is bounded to the add_student function
    addstudbutton = Button(windowFrame, text="Add student")
    addstudbutton.grid(row=3, column=1, sticky=N)
    addstudbutton.bind("<Button-1>", add_student)

    # Setting up and placing a button in the Gui frame that is bounded to the view_students function
    viewstudbutton = Button(windowFrame, text="View Student Records")
    viewstudbutton.grid(row=3, column=2, sticky=N)
    viewstudbutton.bind("<Button-1>", view_students)

    # Setting up and placing a button in the Gui frame that is bounded to the search_student function
    searchstudbutton = Button(windowFrame, text="Search a Student")
    searchstudbutton.grid(row=3, column=3, sticky=N)
    searchstudbutton.bind("<Button-1>", search_student)

    # Setting up and placing a button in the Gui frame that is bounded to the update_student function
    updatestudbutton = Button(windowFrame, text="Update Student Records")
    updatestudbutton.grid(row=3, column=4, sticky=N)
    updatestudbutton.bind("<Button-1>", update_student)

    # Setting up and placing a button in the Gui frame that is bounded to the delete_student function
    delstudbutton = Button(windowFrame, text="Delete a Student")
    delstudbutton.grid(row=3, column=5, sticky=N)
    delstudbutton.bind("<Button-1>", delete_student)

    # Setting up and placing a button in the Gui frame that is bounded to the quit_button function
    quitbutton = Button(windowFrame, text="Quit")
    quitbutton.grid(row=3, column=6, sticky=N)
    quitbutton.bind("<Button-1>", quit_button)

    # keeps the whole Gui Frame running until the quit button is clicked
    windowFrame.mainloop()

# Calling the Gui Window
menus()


