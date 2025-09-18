"""
Stack Implementation
Following W3Schools DSA Tutorial: https://www.w3schools.com/dsa/dsa_intro_stacks.php
"""

class Stack:
    """Stack implementation using Python list"""
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def display(self):
        """Display all items in the stack (top to bottom)"""
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):", self.items[::-1])

# Example usage
if __name__ == "__main__":
    # Create a new stack
    stack = Stack()
    
    # Check if stack is empty
    print(f"Is stack empty? {stack.is_empty()}")
    
    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Display stack
    stack.display()
    
    # Peek at top element
    print(f"Top element: {stack.peek()}")
    
    # Pop elements
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")
    
    # Display stack after popping
    stack.display()
    
    # Get stack size
    print(f"Stack size: {stack.size()}")

