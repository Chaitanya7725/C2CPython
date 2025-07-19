# def move(current_row, current_col, direction):
#     # Start with the current position
#     new_row = current_row
#     new_col = current_col

#     # Update the position based on the direction
#     if direction == 'up':
#         new_row -= 1
#     elif direction == 'down':
#         new_row += 1
#     elif direction == 'left':
#         new_col -= 1
#     elif direction == 'right':
#         new_col += 1
#     else:
#         print("Invalid direction!")

#     return new_row, new_col

# room = [
#   'xxxxx',
#   'x..ex',
#   'x...x',
#   'x...x',
#   'xxxxx',
# ]

# # Let's say the player starts at row 2, col 2
# current_row, current_col = 2, 2

# # Move up
# new_row, new_col = move(current_row, current_col, 'up')
# print(new_row, new_col)  # Output: 1 2

# # Move right
# new_row, new_col = move(current_row, current_col, 'right')
# print(new_row, new_col)  # Output: 2 3



# list = [1,2,3,4,5,6,7,8,9]
# print(list[2:])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0,11):
    print(numbers[0:len(numbers)-i])
# print(numbers[0:11])
# print(numbers[0:10])
# print(numbers[0:9])
# print(numbers[0:8])
# print(numbers[0:7])
# print(numbers[0:6])
# print(numbers[0:5])
# print(numbers[0:4])
# print(numbers[0:3])
# print(numbers[0:2])
# print(numbers[0:1])

import time
start_timer = 10
while start_timer > -1:
    print(start_timer)
    time.sleep(1)
    start_timer = start_timer - 1



shopping_list = ['milk', 'cereal', 'apples', 'rice', 'chicken']
items_to_check = ['milk', 'cereal', 'cheese','apples', 'chicken', 'pasta','rice']
for item in items_to_check:
    if item in shopping_list:
        print(f'Found {item}')
    else:
        print(f'{item} is not in the shopping list.')