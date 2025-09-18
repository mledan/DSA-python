"""
Singly Linked List Implementation
Following W3Schools DSA Tutorial: https://www.w3schools.com/dsa/dsa_intro_linkedlists.php
"""

class Node:
    """Node class for linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Singly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None
    
    def get_size(self):
        """Get the size of the linked list"""
        return self.size
    
    def prepend(self, data):
        """Add element at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def append(self, data):
        """Add element at the end"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def insert_at(self, index, data):
        """Insert element at specific index"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_first(self):
        """Delete the first element"""
        if self.is_empty():
            return None
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def delete_last(self):
        """Delete the last element"""
        if self.is_empty():
            return None
        
        if self.size == 1:
            data = self.head.data
            self.head = None
            self.size = 0
            return data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        data = current.next.data
        current.next = None
        self.size -= 1
        return data
    
    def search(self, data):
        """Search for an element in the linked list"""
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def display(self):
        """Display all elements in the linked list"""
        if self.is_empty():
            print("Linked list is empty")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))

# Example usage
if __name__ == "__main__":
    # Create a new linked list
    ll = SinglyLinkedList()
    
    # Add elements
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    
    # Display the linked list
    print("Linked List:")
    ll.display()
    
    # Search for an element
    index = ll.search(20)
    print(f"Element 20 found at index: {index}")
    
    # Get size
    print(f"Size of linked list: {ll.get_size()}")
    
    # Delete elements
    deleted = ll.delete_first()
    print(f"Deleted first element: {deleted}")
    ll.display()

