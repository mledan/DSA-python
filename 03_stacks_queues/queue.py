"""
Queue Implementation
Following W3Schools DSA Tutorial: https://www.w3schools.com/dsa/dsa_intro_queues.php
"""

class Queue:
    """Queue implementation using Python list"""
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def peek(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)
    
    def display(self):
        """Display all items in the queue (front to rear)"""
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue (front to rear):", self.items)

# Example usage
if __name__ == "__main__":
    # Create a new queue
    queue = Queue()
    
    # Check if queue is empty
    print(f"Is queue empty? {queue.is_empty()}")
    
    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    # Display queue
    queue.display()
    
    # Peek at front element
    print(f"Front element: {queue.peek()}")
    
    # Dequeue elements
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    
    # Display queue after dequeuing
    queue.display()
    
    # Get queue size
    print(f"Queue size: {queue.size()}")

