# Data Parsing - Extract Information from Text
data = "Rollno.: 15, Name: Ichigo, Marks: 92; Rollno.: 18, Name: Renji, Marks: 76; Rollno.: 13, Name: Rukia, Marks: 82"

students = data.split('; ')

student_list = []
for student in students:
    parts = student.split(', ')
    student_info = {}
    
    for part in parts:
        key, value = part.split(': ')
        student_info[key] = int(value) if key in ['Rollno.', 'Marks'] else value  
    
    student_list.append(student_info)

print(f"Student List: {student_list}")
