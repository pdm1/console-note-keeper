from todo import *
from login import *
from pprint import *

    


my_todos = Todo("Billy Bob") 
select = -1
while select != 0:
    print("1. Add Todo" + "\n" +
        "2. Update Todo"  + "\n" +
        "3. Delete Todo" + "\n" +
        "4. Complete Todo" + "\n" +
        "5. Delete all completed" + "\n" +
        "6. View all Todo" + "\n" +
        "0. Quit")
    try:
        select = int(raw_input("choose option "))
        if select == 1:
            select = raw_input("Add Todo:  ")
            my_todos.add_todo(select)
        if select == 2:
            select = raw_input("Update Todo at number:  ")
            my_todos.update_todo(select)
        if select == 3:
            select = raw_input("Delete Todo at number:  ")
            my_todos.delete_todo(select)
        if select == 4:
            select = raw_input("Mark as complete at number:  ")
            my_todos.complete_todo(select)
        if select == 5:
            select = raw_input("Delete all complete? 1. Yes 2. No  ")
            my_todos.delete_complete_todo()
        if select == 6:
            pprint(my_todos.show_todo())
        if select == 0:
            quit()
        else:
            print("You have choosen, poorly.")
    except ValueError: 
        print("Mighty hero!! You have discovered my secrets! To claim your prize, enter a number between 1 and 6")
        
    
