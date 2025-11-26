import sys

with open("D:\\NewVision\\resource\\sample_student_data.txt","r") as f:
    student_Data=f.read()

for i in range(student_Data):
    slpitted_data = student_Data.split("\t")
    print(slpitted_data)

