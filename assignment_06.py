#--------------------------------------------------------------#
# Title: Assignment06
# DESC: This assignment demonstrates using constants, variables,
#        operators, formatting, and files
# and calculations
# Change Log: (Who, When, What)
# Ryan, 5/21/2024, Created Script
#--------------------------------------------------------------#
from pathlib import Path
import json

#Define the Data Constants
MENU:str = """
Select and enter a number based on the following options:
1. Register a student for a course
2. Show current data
3. Save data to a file
4. Exit the program
    """
FILE_NAME:str = "Enrollments.json"

counter:int = 0
menu:str = ''
choice:str = ''
csv_data:str = ''
file_obj = 0

# When the program starts, read the file data into a list of lists(table)
# Extract the data from the file


# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: list[str] = []
student:list = []
student_csv_string = ""
try:
     with open(FILE_NAME, "r") as file:
        # Transform the data from the file
        # student_data = row.split(',')
            student_data = "[student_data[0], student_data[1], student_data[2]]"
        # Load it into our collection (list of lists)
            student.append(student_data)
            file.close()

except FileNotFoundError as e:
    print("ERROR: File not found.")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error.\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
# Present and Process the data
while (True):
    

    # Present the menu of choices
    print(MENU)
    choice = input("Enter a Menu Option (1-4): ")

    # Input user data
    if choice == "1":
        student_first_name = input("Enter the Student First Name: ")
        student_last_name = input("Enter the Student Last Name: ")
        course_name = input("Enter the Course Name:")
        student_data = [student_first_name, student_last_name, course_name]
        student.append(student_data)

    # Present the current data

    elif choice == "2":
        print(student_data)
        for student in student:
            joined_student_info = ',' .join(student)
            print(joined_student_info)

        
    # Save the data to a file
    elif choice =="3":
        csv_data= open(FILE_NAME,'a')

        #Writing to JSON File
        for student in student:
            student_csv_string = f"{student[0]} {student[1]} {student[2]},  \n"
            student_csv_string = json.dumps(student_data)
            csv_data.write(student_csv_string)
            #csv_data.write = json.dumps(student_csv_string)
            #csv_data.write(student_csv_string)

        # Closing File
        csv_data.close()

        #Output
        print(f' You have registered {student_first_name} {student_last_name} for {course_name}, \n'
              )

    # Stop the loop

    elif choice =="4":
        print("Ending Program")
        exit()

    else:
        print("Enter in 1-4")
