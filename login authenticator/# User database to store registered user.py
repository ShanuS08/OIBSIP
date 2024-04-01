user_database = {}

def register():
    print("Please enter your details to register:")
    username = input("Username: ")
    password = input("Password: ")
    if username in user_database:
        print("Username already exists. Please try again.")
    else:
        user_database[username] = password
        print("Registration successful!")

def login():
    print("Please enter your login details:")
    username = input("Username: ")
    password = input("Password: ")
    if username in user_database and user_database[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def secure_page():
    print("Welcome to the secure page!")

def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Access Secure Page")
        print("4. Exit")
        choice = input("Please enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                secure_page()
        elif choice == '3':
            print("Please login to access the secure page.")
            if login():
                secure_page()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
