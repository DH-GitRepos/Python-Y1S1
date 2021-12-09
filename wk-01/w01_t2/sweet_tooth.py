# PROJECT: (WK-01) Sweet tooth
# Solution written by Darren Halpin

number_of_sweets = int(40)
number_of_students = int(14)

sweets_per_student = number_of_sweets // number_of_students
sweets_left = number_of_sweets % number_of_students

print("Each of the " + str(number_of_students) + " students get: " + str(sweets_per_student) + " sweets each.")
print("The teacher gets: " + str(sweets_left) + " sweet(s).")

