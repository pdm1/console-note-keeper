import re
import os

class Todo:
 
    def __init__(self,name):
        self.name = name
        self.all_todo =[]
        self.all_completed =[]
    
    def create_new_list(self):
        self.all_todo = []
        self.all_completed = []

        
    def add_todo(self, todo):
        if todo:
            self.all_todo.append(todo)
            self.all_completed.append(False)
        return
    
    
    def show_todo(self):
        for i, (done, todo) in enumerate(zip(self.all_completed, self.all_todo)):
            print (i + 1,done,todo)
    
    def save_todo(self, fname=None):
        """This really should have been a dictionary... 
        get this to work... come back later and refactor
        ... seriously.. fix this.. cause what follows is an abomination :(
        """
        
        if fname == None:
            fname = raw_input("Name this list:  ")
        fname = re.sub(r"[^\w\s]", '', fname) # strip special characters from file name
        fname = re.sub(r"\s+", '_', fname) # replace " " with _
        user_name = re.sub(r"\s+", '_', self.name)
        fname += ".txt"
        path = os.path.join("todos/", user_name, fname)
        if not os.path.exists("todos/"+user_name):
            os.makedirs("todos/"+user_name)
        file = open(path, "w")
        for item in self.all_todo:
            file.write(item + "\n")
        file.write("****COMPLETE****\n") #<-- bleh.. such ugly
        for item in self.all_completed:
            file.write(str(item) + "\n")        
        file.close
        
        return fname
        
    def retrieve_todo(self, fname=None):
        self.all_todos = []
        self.all_completed = []
        my_todos = []
        if fname == None:
            fname = raw_input("List to retrieve:  ")
        user_name = re.sub(r"\s+", '_', self.name)
        path = os.path.join("todos/", user_name, fname + ".txt")
        with open(path) as f:
            content = f.readlines()
        for lines in content:
            lines = lines.strip("\n")
            lines = lines.split("****COMPLETE****")
            my_todos.append(lines[0])

        for i in range(len(my_todos)):
            if my_todos[i] == "True" or my_todos[i] == "False":
                self.all_completed.append(my_todos[i])
            elif my_todos[i] != '':
                self.all_todo.append(my_todos[i])

    def get_files(self):
        user_name = re.sub(r"\s+", '_', self.name)
        for file in os.listdir("todos/"+user_name):
            if file.endswith(".txt"):
                print(file)
            
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
'''   
me = Todo("billy bob")

me.add_todo("cookies")
me.add_todo("Buy milk")
me.add_todo("get a life")
me.complete_todo(1)

me2 = Todo("SallySue")
me2.add_todo("cookies")
me2.add_todo("Buy milk")
me2.add_todo("get a life")
me2.complete_todo(2)
print me.save_todo()
print me2.save_todo()

me.retrieve_todo("Test")

print me.all_completed
print me.all_todo
print me.show_todo()
'''