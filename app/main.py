class Todo:
    ALL_TODO = []
    COMPLETED = []

        
    def add_todo(self, todo):
        if todo:
            Todo.ALL_TODO.append(todo)
            Todo.COMPLETED.append(False)
        return
    
    def show_todo(self):
        for i, (done, todo) in enumerate(zip(Todo.COMPLETED, Todo.ALL_TODO)):
            print (i + 1,done,todo)
    
    def _is_valid_int(self, index):
        '''Check initial value to ensure type int
        
        '''
        try:
            index = int(index)
        except:
            while isinstance(index,int) is False:
                try:
                    index = int(raw_input("Feed me a number between %d and %d: " % (1,len(Todo.ALL_TODO) )))
                except ValueError:
                    print("Todo selection must be an integer.")  
        return index
    
    
    def _is_valid_range(self, index):
        '''Ensure int is in todo index
        
        '''
        try:
            index = int(raw_input("You Fool! Give me a number in range %d to %d " % (1,len(Todo.ALL_TODO) )))
        except ValueError:
                print("You ninny! I need a number!")        
        return index
    
    
    def delete_todo(self, num):
        index = self._is_valid_int(num)  
        while index > len(Todo.ALL_TODO) or index == 0:
            index = self._is_valid_range(index)
        if index <= len(Todo.ALL_TODO):
            old = Todo.ALL_TODO[index - 1]
            del Todo.ALL_TODO[index - 1]
            print("Deleted: ",old )
        return
    
    
    def update_todo(self, num):
        index = self._is_valid_int(num) 
        while index > len(Todo.ALL_TODO) or index == 0:
            index = self._is_valid_range(index)
        if index <= len(Todo.ALL_TODO):
            update = raw_input("Edit: %s  :" % (Todo.ALL_TODO[index - 1]))
            Todo.ALL_TODO[index - 1] = update
            print("Edit Complete")
        return
    
    def complete_todo(self,num):
        index = self._is_valid_int(num)
        while index > len(Todo.COMPLETED) or index == 0:
            index = self._is_valid_range(index)  
        if index <= len(Todo.COMPLETED):
            Todo.COMPLETED[index -1] = True
            print("Todo Complete: ", (Todo.ALL_TODO[index -1]))
        return
    
    def delete_complete_todo(self):
        index = -1
        while index < 1 or index > 2:
            try:
                index = int(raw_input("Delete all completed Todos, are you sure? (1)Yes (2)No: "))
            except ValueError:
                
                    try:
                        index = int(raw_input("So... about that number..."))
                    except ValueError:
                        print("RTFM! 1 == Yes. 2 == No.")
        if index == 1:
            for i in Todo.COMPLETED:
                if i == True:
                    del Todo.COMPLETED[i - 1]
                    del Todo.ALL_TODO[i - 1]
        return
            
        
    

          
        
            
my_todos = Todo()    
yarp = Todo()    
get_todo = raw_input("What to add?  ")
my_todos.add_todo(get_todo)
get_todo = raw_input("What to add?  ")
my_todos.add_todo(get_todo)
get_todo = raw_input("What to add?  ")
my_todos.add_todo(get_todo)

del_todo = raw_input("Which one to delete?  ")
my_todos.delete_todo(del_todo)

get_update = raw_input("Choose item to edit:  ")
my_todos.update_todo(get_update)

complete = raw_input("Choose todo to complete: ")
my_todos.complete_todo(complete)

my_todos.delete_complete_todo()
print my_todos.show_todo()
print yarp.show_todo()
    