# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
#
# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >=81:
#         student_grades[student] = 'Exceeds Expectation'
#     elif score >=71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'
#
# print(student_grades)

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }
#
#
# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }
# starting_dictionary["c"] = 7
# final_dictionary = starting_dictionary
# print(starting_dictionary)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])