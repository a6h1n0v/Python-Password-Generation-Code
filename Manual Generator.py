# Copyright Owner: Abhinav_dev
# You Need To Enter The Details Inside the names and numbers 
# After Entering Just Run The Program You Will Get Different Types Of Combination Of Passwords
# This is only for educational pourpose

import itertools

names = ['name1', 'name2']  # Change Or Add Names inside The Box. And also need to be separated with a comma Eg: ['name1', 'name2']
numbers = ['num1', 'num2', 'num3']  # Change or Add Numbers inside the Box. And also need to be separated with a comma Eg: ['num1', 'num2']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-']
passwords = []

for name in names:
    for number in numbers:
        for symbol in symbols:
            passwords.append(name + symbol + number)

combinations = list(itertools.product(names, symbols, numbers))
for combo in combinations:
    passwords.append(''.join(combo))

passwords = list(set(passwords))

for i in range(10):
    print(passwords[i])

print("Copyright Owner: Abhinav_dev")
