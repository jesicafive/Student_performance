''' Student Performance Analyzer

A simple Python program to calculate total marks, average,
and pass/fail status of students using dictionaries
and conditional statements.

## Technologies
- Python

## Concepts Used
- Lists
- Dictionaries
- Loops
- Conditional statements
'''
# Refactored code using list and loop for multiple students

students= [  
    {"Name":"Anika", "Maths":76, "English":46, "Science":34 }, 

    {"Name":"Minakshi", "Maths":67, "English":85, "Science":68},
    {"Name":"Riya", "Maths": 23, "English":12, "Science":26 }]

for student in students:

    total= (student.get("Maths") + student.get("English") + student.get("Science"))
    print("\nName:", student.get("Name")) 
    print("Total Marks :", total)

    average=total/3
    print("Average marks :", average)

    if(average>=40):
        print("Result: Passed")
    else:
        print("Result: Failed")


