pwd = input("What is the master password? : ")

def view():
    pass

def add():
    name = input("Enter your name : ")
    pwd = input("Enter your password : ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + " | " + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? - (view,add, press Q to quite) : ").lower()
    
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
