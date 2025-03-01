"""
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


scores = input("Enter scores: ").split()
max_scores = max(scores)
print(max_scores



#1
scores = input("Enter scores : ").split()
max_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score
print(max_score)

#2
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)

#3
point = input("Enter scores; ").split()
print(max(point))
"""

#Final Project
#Password Generator Project
import string
import random
letters = string.ascii_lowercase and string.ascii_uppercase
numbers = string.digits
punctuation = string.punctuation

letter = int(input("Enter how many letter you want in your password?\n"))
number = int(input("Enter how many number you want in your password?\n"))
symbols = int(input("Enter how many symbol you want in your password?\n"))
Password_list = []
for i in range(1,letter + 1):
    Password_list.append(random.choice(letters))
for j in range(1, number + 1):
    Password_list += random.choice(numbers)
for k in range(1, symbols + 1):
    Password_list += random.choice(punctuation)

random.shuffle(Password_list)

password = ""
for char in Password_list:
  password += char
print("There are ",len(password),"character in the passwords")
print("The password is: ",password)