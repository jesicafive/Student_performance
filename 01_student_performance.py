student1=(
    {"Name":"Anika", "Maths":76, "English":46, "Science":34
    })
student2=(
    {"Name":"Minakshi", "Maths":67, "English":85, "Science":68})

Total_1=((student1.get("Maths")) + (student1.get("English")) + (student1.get("Science")))
Total_2=((student2.get("Maths")) + (student2.get("English")) + (student2.get("Science")))
Average_1= Total_1/3
Average_2= Total_2/3
print("Anika's total marks are", Total_1)
print("Minakshi's total marks are", Total_2)
print("Anika's average marks are", Average_1)
print("Minakshi's average marks are", Average_2)
if Average_1 >= 40:
    print("Anika passed")
else:
    print("Anika failed")
if(Average_2 >= 40):
    print("Minakshi passed")
else:
    print("Minakshi failed")
