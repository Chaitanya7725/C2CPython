# print('I have two apples. You give me three apples. How many apples do I have?')

# guess = input('Please answer my riddle: ')

# while guess != '5':
#   guess = input('Try again ')

# print('Wow! You got it.')


# person = 'duck'          # Line 1
# count = 0                # 2

# while person != 'goose': # 4
#   if count > 5:          # 5
#     person = 'goose'     # 6

#   print(person)          # 8
#   count += 1 


# color = 'green'

# guess = input('What is my favorite color? ')


# while str.lower(guess) != color:
#   print(f'Nope! {guess} is not my favorite color. ')
#   guess = input('Try again: ')

# print('Yup! It was green. ')

for attempt in range(3):
    guess = int(input(f"Attempt {attempt + 1}/3: What has an eye, but cannot see?: "))

count = 0
while guess != 'a needle' and count < 3:
    print("Wrong guess.")
    count+=1

if(count == 3):
    print("All out of chances")
else:
   print("you are right!")