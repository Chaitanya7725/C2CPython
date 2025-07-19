def say_hello():
    print('Hello!')
    return "This method has been invoked!"

# Calling a method/invoking

# captured_value = say_hello()
# print(captured_value)
# print(say_hello())


# addition= +
# sub= -
# mul= *
# division= /
# print("This is the calculator application")
def addition(a,b): #parameters
    added_value = a+b
    return added_value

added_value = addition(1,2) #arguments
print(added_value)


# Order
def hello():
    print("Hi, how are you?")


def goodbye():
    print("Bye! Cya!")


# hello()
# goodbye()

# Concatenate
# concatenated_string = 'first'
# concatenated_string = concatenated_string + 'second'
# print(concatenated_string)

# Casting
# check_concatenate = 'first' #first2
# second_var = 2
# check_concatenate = check_concatenate + str(second_var)
# print(check_concatenate)

# print(type(second_var))

# Casted var at start
# check_concatenate = 'first' #first2
# second_var = str(2)
# check_concatenate = check_concatenate + second_var
# print(check_concatenate)

# print(type(second_var))

# My name is Chai. I stay in Texas
# My name is John. I stay in NY

def print_details(name,state):
    print('My name is',name,'. I stay in',state)

print_details('Chai','Texas')
print_details('John','NY')

number_of_eggs = 3
print('We are using ' + str(number_of_eggs) + ' eggs in our cake.')







# subtraction

def subtract(a,b):
    updated_var = a-b
    return updated_var

subtracted_var = subtract(5,2)
print(subtracted_var)