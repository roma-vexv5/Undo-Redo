# Undo/Redo Stack 7/9/25

class UndoRedoStack:
    def __init__(self): #initializes the undo and redo stacks, creates lists to keep track of actions that can completed
        self.undo_stack = [] #keeps track of actions that can be undone
        self.redo_stack = [] #keeps track of actions that can be redone
        

    def do_action(self, action):
        self.undo_stack.append(action)#this adds a new action to the undo stack
        self.redo_stack.clear()  #this clears the redo stack on new action because once a new action is completed you cannot redo the previous actions 

    def undo(self): #creates an undo function
        if len(self.undo_stack) > 0:#if the length of the undo list is greater than 0 (essentially it has something inside)
            object = self.undo_stack.pop()#this removes the last item in the undo stack list
            self.redo_stack.append(object)#this adds the last item from the undo stack to the redo stack 
            return object
        return None #if there is no item in the list then nothing will happen

    def redo(self): #creates a redo function
        if len(self.redo_stack) > 0: #if there is an item in the redo list then only it will work
            object = self.redo_stack.pop()# if this function is run, it removes the last item from the redo list
            self.undo_stack.append(object) #whatever is removed from the redo stack is added to the undo stack 
            return object
        return None #if there is nothing inside of the list nothing will happen
    

obj1 = UndoRedoStack()
obj1.do_action("hello")
obj1.undo()
