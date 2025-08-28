roles = ["admin", "user"] # different user role types

# usernames are role types

while True:
    try:
        role = input("Enter username: ")

        if role not in roles:
            raise ValueError # simple error handling
        
        break
        
    except ValueError: # making sure only valid roles can continue through code
        print("Not a valid username.")
        print("Please try again")
        print("")
        continue

if role == "user": # shows personal information of user. Things could include tax forms, personal address, pay stubs, etc
    print("You selected the user route.")
    print("Showing random important personal information here.")

if role == "admin": # shows company information. Things could include finances, upcomming projects, etc
    print("You selected the admin route.")
    print("Showing random important company information here.")