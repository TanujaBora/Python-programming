#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# to create a random password and strong password easy way
# range function
password_str = ''
for i in range(0,nr_letters):
    password_str += random.choice(letters)
for i in range(0,nr_symbols):
    password_str += random.choice(symbols)
for i in range(0,nr_numbers):
    password_str += random.choice(numbers)
print(f'your password is {password_str}')

# range function
password_str1 = ''
for i in range(1,nr_letters+1):
    password_str1 += random.choice(letters)
for i in range(1,nr_symbols+1):
    password_str1 += random.choice(symbols)
for i in range(1,nr_numbers+1):
    password_str1 += random.choice(numbers)
print(f'your password is {password_str1}')

# to create a random password and strong password hard way
password_list = []
for i in range(nr_letters):
    password_list.append(random.choice(letters))
for i in range(nr_symbols):
    password_list.append(random.choice(symbols))
for i in range(nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)

# to convert list into str method 1
password1 = ''.join(password_list)
print(f'your password is {password1}')

# to convert list into str method 2
password = ''
for i in password_list:
    password += i
print(f'your password is {password}')