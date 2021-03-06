from todo import *
from login import *
from pprint import *

my_login = Login()
user = pw = pw_repeat = None
while my_login.sign_in(user,pw) is False:
    try:
        select = int(raw_input("1. Sign in" + "\n" + "2. Create Account" + "\n" ))
        if select == 1:
            user = raw_input("Enter your user name: ")
            pw = raw_input("Enter your password: ")
            if my_login.sign_in(user,pw) == True:
                print("Welcome", user)
            else:
                print("\n" + "One more time..." + "\n")
        if select == 2:
            user = raw_input("Select a user name: ")
            pw = raw_input("Choose a password.  Requires 7 characters minimum with one symbol: ")
            pw_repeat = raw_input("Please re-enter your password: ")
            if my_login.create_account(user, pw, pw_repeat) is True:
                print("Success. Welcome", user)
                continue
    except ValueError:
        print("\n" + "Why don't we try this again." + "\n")

my_todos = Todo(user) 
select = -1
while select != 0:
    print( "\n" + "1. Add Todo" + "\n" +
        "2. Update Todo"  + "\n" +
        "3. Delete Todo" + "\n" +
        "4. Complete Todo" + "\n" +
        "5. Delete all completed" + "\n" +
        "6. View all Todo" + "\n" +
        "7. Save this list" + "\n" +
        "8. Open saved list" + "\n" +
        "9. Create new list" + "\n" +
        "0. Quit")
    try:
        select = int(raw_input( "\n" + "Choose option: "))
        if select == 1:
            select = raw_input("Add Todo: ")
            my_todos.add_todo(select)
        elif select == 2:
            select = raw_input("Update Todo at number: ")
            my_todos.update_todo(select)
        elif select == 3:
            select = raw_input("Delete Todo at number: ")
            my_todos.delete_todo(select)
        elif select == 4:
            select = raw_input("Mark as complete at number: ")
            my_todos.complete_todo(select)
        elif select == 5:
            select = raw_input("Delete all complete? 1. Yes 2. No: ")
            my_todos.delete_complete_todo()
        elif select == 6:
            pprint(my_todos.show_todo())
        elif select == 7:
            my_todos.save_todo()
        elif select == 8:
            my_todos.get_files()
            print("\n" + "Do not include '.txt' in the file name")
            my_todos.retrieve_todo()
        elif select == 9:
            my_todos.create_new_list()
        elif select == 0:
            quit()
        else:
            print("\n" + "You have choosen, poorly." + "\n" )
    except ValueError: 
        print("\n" + "Mighty hero!! You have discovered my secrets! To claim your prize, enter a number between 1 and 6" + "\n" )
        
    
