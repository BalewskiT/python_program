

name = input('What is your name? ')
birth_year = input('What is your birth year? ')
age = 2019 - int(birth_year)
weight_lbs = input('weight lbs: ')
weight_kg = int(weight_lbs) * 0.45
print(name + ' is ' + str(age) + ' years old and weighs ' + str(weight_kg) + ' kilograms')
