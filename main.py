# Number Analyzer

# numbers = [10, -5, 0, 20, -8, 0, 15, -2, 7, 0]

# positive = 0
# negative = 0
# zero = 0

# for num in numbers:
#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zero += 1

# print("Positive Numbers =", positive)
# print("Negative Numbers =", negative)
# print("Zero Numbers =", zero)


# Skip multiples of 3

# for i in range(1, 51):
#      if i % 3 == 0:
#          continue
#      print(i)



# # Find the first prime number

# start = 10
# end = 50

# for num in range(start, end + 1):

#     if num < 2:
#         continue

#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("First Prime Number =", num)
#         break


# # Student marks using list


# marks = [78, 85, 92, 67, 88]

# highest = max(marks)
# lowest = min(marks)
# average = sum(marks) / len(marks)

# print("Highest Mark =", highest)
# print("Lowest Mark =", lowest)
# print("Average Mark =", average)

# print("\nMarks Above Average:")

# for mark in marks:
#     if mark > average:
#         print(mark)


# # Dictionary Based Student Record

# student = {"Name": "Sanghamitra",
#             "Roll No": 50,
#             "Marks": 89}

# student["Grade"] = "A"

# student["Marks"] = 90

# print("Student Record")

# for key, value in student.items():
#     print(key, ":", value)





# numbers = []
# choice = 1

# while choice != 3:

#     print("\n1. Add Number")
#     print("2. Display List")
#     print("3. Exit")

#     if choice == 1:
#         numbers.append(10)
#         numbers.append(20)
#         numbers.append(30)
#         print("Numbers Added")

#     elif choice == 2:
#         print("List =", numbers)

#     choice += 1

# print("Program Exited")


# Increasing Pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Reverse Pattern

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()