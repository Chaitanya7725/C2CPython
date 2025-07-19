# inventory = [
#   {'prod_Id': 4327, 'type': 'Shoes', 'price': 100.0, 'total': 20},
#   {'prod_Id': 3915, 'type': 'Tshirts', 'price': 43.5, 'total': 32},
#   {'prod_Id': 2119, 'type': 'Pants', 'price': 34.0, 'total': 19},
#   {'prod_Id': 1194, 'type': 'Jumpers', 'price': 250.0, 'total': 5},  
#   {'prod_Id': 1300, 'type': 'Blouse', 'price': 24.76, 'total': 3},
#   {'prod_Id': 1118, 'type': 'Dress', 'price': 50.0, 'total': 10}, 
#   {'prod_Id': 1664, 'type': 'Suits', 'price': 250.0, 'total': 5}
# ]
# class Product:
#     def __init__(self, product_id ,type, price, total):
#         self.product_id = product_id
#         self.type = type
#         self.price = price
#         self.total = total


#     def display_menu():
#         print("\n **GenZ STORE INVENTORY SYSTEM**")  
#         print("1. View Store Inventory ") 
#         print("2. Add A New Product")    
#         print("3. Remove Products")  
#         print("4. Exit\n") 
#     def display_inventory():
#         print("\n **GEN-Z STORE INVENTORY**")
#         for item in inventory:
#             print("------------")
#             for key,value in item.items():
#                 print(key,value)
#         print("------------")

#     def add_to_inventory(self):
#         print("Adding to the inventory->")
#         inventory.append({'prod_Id': self.product_id, 'type': self, 'price': 100.0, 'total': 20})

#     def user_selection():
#         user_choice = int(input("Enter a number between 1-5: "))
#         if user_choice == 1:  #Go to Store Inventory.
#             display_inventory()
#         elif user_choice == 2:  #Initiate New Product Process.
#             print('add a new product') 
#             # inventory.append({'prod_Id': 9999, 'type': 'food', 'price': 100.0, 'total': 20})
#         elif user_choice == 3:  #Initiate Removing a Product.
#             print('remove a product')
#         elif user_choice == 4:  #Initiate Removing a Product.
#             print('update product')
#         elif user_choice == 5:  #Exit the program
#             print("Goodbye message")
#         else:
#             print("\nSorry, Not a Valid Choice. Please try again!")

logs = []
class Student:
    def __init__(self,student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
    
def add(self,id,name,grade):
    logs.append({"id":id,"name":name,"grade":grade})

# def remove(self,id,name,grade):

def display(self):
    for log in logs:
        print("----------")
        for key,value in logs.items:
            print(key,value)

def start_menu():
    