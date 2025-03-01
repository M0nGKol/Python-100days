username_credential = [
    {"username": "testuser", "password": "testpass"},
]
check_length = lambda user_password : len(user_password)>=8
check_forupper = lambda user_password : any(char.isupper() for char in user_password)
check_digit = lambda user_password : any(char.isdigit() for char in user_password)
check_special = lambda user_password : any(char in "!@#$%^&*()_+-=" for char in user_password)

def password_verify(user_password):
    if not check_length(user_password):
        return "Password too short. Must contain 8 characters."
    if not check_forupper(user_password):
        return "Password must contain at least one uppercase letter."
    if not check_digit(user_password):
        return "Password must contain at least one digit."
    if not check_special(user_password):
        return "Password must contain at least one special character."
    return "strong"

print("Bonus\n")

def menu():
    print("Menu:\n1.Register\n2.Login\n3.Forgot Password\n4.Exit")
def register():
    registered = False
    while not registered:
        user_username = input("Enter a username to register: ")
        if any(username["username"] == user_username for username in username_credential):
            print("Error: Username already exists. Try again.")
            continue

        while True:
            user_password = input("Enter a password: ")
            verify_message = password_verify(user_password)
            if verify_message == "strong":
                username_credential.append({"username": user_username, "password": user_password})
                print("Registered successfully with a strong password.")
                registered = True
                break
            else:
                print(verify_message)
def login():
    attempts = 0
    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for user in username_credential:
            if user["username"] == username and user["password"] == password:
                print(f"Login successful! Welcome, {username}.")
                return
            else:
                attempts +=1

            if attempts == 3:
                print("Maximum login attempts reached. Try again later.")
                return


# Forgot password function
def forgot_password():
    username = input("Enter your username to retrieve your password: ")
    for user in username_credential:
        if user['username'] == username:
            print(f"Your password is: {user['password']}")
            return
    print("Username not found.")


while True:
    menu()
    user_opt = int(input("Choose an option (1-4): "))
    if user_opt == 1:
        register()
    elif user_opt == 2:
        login()
    elif user_opt == 3:
        forgot_password()
    elif user_opt == 4:
        print("Exist the program.")
        break
