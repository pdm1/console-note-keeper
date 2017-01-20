class Todo:
 
    def __init__(self,name):
        self.name = name
        self.all_todo =[]
        self.all_completed =[]

        
    def add_todo(self, todo):
        if todo:
            self.all_todo.append(todo)
            self.all_completed.append(False)
        return
    
    
    def show_todo(self):
        for i, (done, todo) in enumerate(zip(self.all_completed, self.all_todo)):
            print (i + 1,done,todo)
    
    def _is_valid_int(self, index):
        '''Check initial value to ensure type int
        
        '''
        try:
            index = int(index)
        except:
            while isinstance(index,int) is False:
                try:
                    index = int(raw_input("Feed me a number between %d and %d: " % (1,len(self.all_todo) )))
                except ValueError:
                    print("Todo selection must be an integer.")  
        return index
    
    
    def _is_valid_range(self, index):
        '''Ensure int is in todo index
        
        '''
        try:
            index = int(raw_input("You Fool! Give me a number in range %d to %d " % (1,len(self.all_todo) )))
        except ValueError:
                print("You ninny! I need a number!")        
        return index
    
    
    def delete_todo(self, num):
        index = self._is_valid_int(num)  
        while index > len(self.all_todo) or index == 0:
            index = self._is_valid_range(index)
        if index <= len(self.all_todo):
            old = self.all_todo[index - 1]
            del self.all_todo[index - 1]
            print("Deleted: ",old )
        return
    
    
    def update_todo(self, num):
        index = self._is_valid_int(num) 
        while index > len(self.all_todo) or index == 0:
            index = self._is_valid_range(index)
        if index <= len(self.all_todo):
            update = raw_input("Edit: %s  :" % (self.all_todo[index - 1]))
            self.all_todo[index - 1] = update
            print("Edit Complete")
        return
    
    def complete_todo(self,num):
        index = self._is_valid_int(num)
        while index > len(self.all_completed) or index == 0:
            index = self._is_valid_range(index)  
        if index <= len(self.all_completed):
            self.all_completed[index -1] = True
            print("Todo Complete: ", (self.all_todo[index -1]))
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
            for i in self.all_completed:
                if i == True:
                    del self.all_completed[i - 1]
                    del self.all_todo[i - 1]
        return