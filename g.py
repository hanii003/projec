def register_user():
    while True:
        user_id = str(input("Enter your id:"))
        if user_id in users.keys():
            print("This user exist!")
        else:
            first_name = input("Enter first name:")
            last_name = input("Enter last name:")
            national_id = input("Enter national ID:")
            birth_date = input("Enter birth date:")
            address = input("Enter address:")
            registration_date = ()
            users[user_id] = {
                'user_id' : user_id,
                'first_name': first_name,
                'last_name': last_name,
                'national_id': national_id,
                'birth_date': birth_date,
                'address': address,
                'registration_date': registration_date
            }
            print(f"Registration successful. Your user ID is:{user_id}")
            break
def display():
    for x , y in users.items():
        print(x , y)
        
def edit_user():
    user_id = input("Enter user ID: ")
    if user_id in users.keys():
            user = input("enter a choice for edit ==> first_name/last_name/national_id/birth_date/address")
            if user == "first_name":
                new_first_name = input("please enter a new first name for edit:")
                users[user_id][first_name] = new_first_name
            elif user == "last_name":
                new_last_name = input("please enter a new last name for edit:")
                users[user_id][last_name] = new_last_name
            elif user == "national_id":
                new_national_id = int(input("please enter a new national id for edit:"))
                users[user_id][national_id] = new_national_id
            elif user == "birth_date":
                new_birth_date = int(input("please enter a new birth date for edit"))
                users[user_id][birth_date] = new_birth_date
            elif user == "address":
                new_address = input("please enter a new address:")
                users[user_id][address] = new_addsress
                print("User information updated successfully.")
            else:
                print("User not found.")

def delete_user():
    user_id = input("Enter user ID: ")
    if user_id in users.keys():
        pass
        
    else:
        print("User not found.")


def main_menu():
    while True:
        print("Welcome to the library management system.")
        print("1. Register user")
        print("2. Edit user information")
        print("3. Delete user")
        print("4. Add book")
        print("5. Delete book")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            display()
            edit_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            add_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
users = {}
books = {}

while True:
    user = input("please enter /help/ for show menu:)")
    if user == "help":
        main_menu()
    else:
        print("cammand not found!")
    break

















        


