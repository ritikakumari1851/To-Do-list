from datetime import datetime

def Addtasks():
    lst = []
    tasks = int(input("Enter the number of task to add: "))
    for i in range(tasks):
        task = input(f"Task {i + 1} : ")
        lst.append(task)
    print("Task Added Sucessfully !")
    proceed = input("Press anykey to Exit : \nPress R to restart :")
    if proceed == "R" or proceed == "r":
        Ask()
    else:
        exit()

    return lst

def get_date():
    date = input("Enter the date in (YYYY-MM-DD) format: ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        print("Invalid date format.")
        return None

def display(user):
    date = get_date()
    if not date:
        return

    with open("data.txt", "r") as f:
        data = f.readlines()
        found = False
        for line in data:
            line = line.strip()
            parts = line.split(":")
            if len(parts) >= 3:
                line_date = parts[0]
                line_user = parts[1]
                if line_user == user and line_date == date:
                    print(line)
                    found = True
        if not found:
            print("No tasks found for that date.")

    proceed = input("Press any key to Exit : \nPress R to restart : ")
    if proceed.lower() == "r":
        Ask()
    else:
        exit()


def remove(user):
    date = get_date()
    if not date:
        return

    found = False
    with open("data.txt", "r") as f:
        lines = f.readlines()

    with open("data.txt", "w") as f:
        for line in lines:
            line = line.strip()
            parts = line.split(":")
            if len(parts) >= 3:
                line_date = parts[0]
                line_user = parts[1]
                if line_user == user and line_date == date:
                    found = True
                    continue 
            f.write(line + "\n")

    if found:
        print("Task successfully deleted.")
    else:
        print("No matching task found.")

    proceed = input("Press any key to Exit : \nPress R to restart :")
    if proceed.lower() == "r":
        Ask()
    else:
        exit()

    
            
def Add(user):
    date = input("Enter the date in : (YYYY-MM-DD) Formate : ")
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        print("You entered:", date_obj.date())
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return 
    lst = Addtasks()

    with open("data.txt", "a") as f:
        f.write(f"{date}:{user}:{lst}\n")
    return date

def datastore(user):
    task = int(input("Choose task to perform: \n CLICK(1,2,3):\n 1. Add new Task \n 2. Remove task \n 3. Display task \n "))
    if task.lower() == 'e':
        print("Goodbye!")
        exit()
    if task == 1:
        Add(user)
    elif task == 2:
        remove(user)
    elif task == 3:
        display(user)
    else:
        print("You Entered invalid choice, try again.")
        datastore(user)

def olduser():
    print("Please proceed further:")
    user = input("Enter Username: ")
    pas = input("Enter Your password: ")
    with open("database.txt", "r") as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            if user in line and pas in line:
                print("Login Successfully!")
                print("Start Your day with to-do list. Welcome", user)
                datastore(user)
                return user
        print("Incorrect username or password!")

def Ask():
    choice = input("Are You a new User? (y/n): ")
    if choice.lower() == "y":
        user = input("UserName: ")
        pas = input("New Password: ")
        with open("database.txt", "a") as f:
            f.write(f"{user}:{pas}\n")
        olduser()
    elif choice.lower() == "n":
        olduser()

print("Welcome to To-Do List!")
print("Choose Your preference:")
Ask()
