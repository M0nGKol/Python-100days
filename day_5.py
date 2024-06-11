student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
Total_height = 0
for n in student_heights:
    Total_height += n
print(f"total height = {Total_height}")
number_of_stuudents = len(student_heights)
print(f"number of students = {number_of_stuudents}")
average = round(Total_height/number_of_stuudents)
print(f"average height = {average}")

