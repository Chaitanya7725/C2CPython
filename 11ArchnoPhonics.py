# 1. choose the random word from list using random library
# 2. Assign no of lives to a var
# 3. start the function where while loop is executed keeping the number of lives in count:
#     if entered char exists in the guessed word -> 
#     else -> Drawing the spider and lives --
# 4. Display + - message in the end

# Create a function named find_max_min.
# The function should take a list of numbers as an argument.
# Inside the function, initialize two variables max_num and min_num to the first element of the list.
# Use a for loop to iterate through the list.
# Use an if statement to update max_num if a larger number is found.
# Use another if statement to update min_num if a smaller number is found.
# Return both max_num and min_num.

max_num = 0
min_num = 0

def find_max_min(list1):
    max_num = list1[0]
    min_num = list1[0]
    for number in list1:
        if number < min_num:
            min_num = number
        elif number > max_num:
            max_num = number
    return min_num,max_num

print(find_max_min([1,87,93,23,67,40,43,8,3,0])) # 0,93