#Create Pssword Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password) 


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

password_list = [] 
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

#Lists
"""
for item in list_of_items:
    #Do something to each item
"""
fruits = ["Apelsin", "Mango", "Pear", "Aplle"]
print(fruits)
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
    print(fruits)
print("-------------------------------------------")
print(fruits)

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights) 

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

average_height = total_height / number_of_students
print(average_height)

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
print(min(student_scores))
print(max(student_scores))
print("-----------------------------------------------")
highets_score = 0
for score in student_scores:
    if score > highets_score:
        highets_score = score
print(f"The highest score in the class is: {highets_score}")


for number in range(1, 11):
    print(number)

for number1 in range(1, 11, 3):
    print(number1)

total = 0
for number3 in range(1, 101):
    total += number3
    print(total)

total4 = 0
for number4 in range(2, 101, 2):
    total4 += number4
print(total4)

total5 = 0
for number5 in range(1, 101):
    if number %2 == 0:
        total5 += number5
print(total5)


for numberr in range(1, 101):
    if numberr %3 == 0 and numberr % 5 == 0:
        print("FizzBuzz")
    elif numberr %3 == 0:
        print("Fizz")
    elif numberr %5 == 0 :
        print("Bizz")
    else:
        print(numberr)

















