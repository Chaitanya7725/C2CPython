favorite_season = 'summer'
favorite_temperature = 60

# print('My favorite season is ',favorite_season,' and I love asdasasd' \
# 'asdasdasdasdwhen it is ',favorite_temperature,' degrees outside.')

# print(f'My favorite season is {favorite_season} and \nI love when it is {favorite_temperature} degrees outside.')

# new line = \n
# add tab/spaces = \t

# def say_hello(name):
#     print(f'Good Night {name}')
# say_hello('Bob')


def thank_you(name,yourname): # parameter #called function
    print(f'Dear {name},\n\nThank you so much for your ' \
    'gift for Christmas/my graduation/my birthday/etc. ' \
    f'It means so much to me!\n\nYours Truly,\n{yourname}')

# thank_you('Noah','Pranay') # argument #calling function

math_grades_Alexis = ['A-', 'A+', 'Pass', 88, 93, 'Satisfactory']
print(math_grades_Alexis[1])
print(len(math_grades_Alexis))
math_grades_Alexis.append('Chai')
print(math_grades_Alexis)
math_grades_Alexis.insert(0,'Pranay');
print(math_grades_Alexis)
# math_grades_Alexis.reverse()
# print(math_grades_Alexis)

count = 1
for grade in math_grades_Alexis:
    count = count + 1
    print('* '+str(grade))

print(count)