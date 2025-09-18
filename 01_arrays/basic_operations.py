"""
Basic Array Operations - Part 1 (SOLUTION)
Following W3Schools DSA Tutorial: https://www.w3schools.com/dsa/dsa_intro_arrays.php

This module covers fundamental array operations including:
- Array creation and initialization
- Finding minimum and maximum values
- Calculating sum and average
- Basic array traversal and manipulation
"""

def create_sample_array():
    """
    Create and initialize a sample array
    Following the W3Schools example: [7, 12, 9, 4, 11]
    
    Returns:
        list: A sample array of integers
    """
    return [7, 12, 9, 4, 11]

def find_minimum(arr):
    """
    Find the minimum value in an array
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr (list): Input array
        
    Returns:
        int or None: Minimum value, or None if array is empty
        
    Example:
        >>> find_minimum([7, 12, 9, 4, 11])
        4
    """
    if not arr:
        return None
    
    min_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
    
    return min_val

def find_maximum(arr):
    """
    Find the maximum value in an array
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr (list): Input array
        
    Returns:
        int or None: Maximum value, or None if array is empty
        
    Example:
        >>> find_maximum([7, 12, 9, 4, 11])
        12
    """
    if not arr:
        return None
    
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i
    
    return max_val

def calculate_sum(arr):
    """
    Calculate the sum of all elements in an array
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr (list): Input array
        
    Returns:
        int: Sum of all elements
        
    Example:
        >>> calculate_sum([7, 12, 9, 4, 11])
        43
    """
    return sum(arr)

def calculate_average(arr):
    """
    Calculate the average of all elements in an array
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr (list): Input array
        
    Returns:
        float or None: Average of all elements, or None if array is empty
        
    Example:
        >>> calculate_average([7, 12, 9, 4, 11])
        8.6
    """
    if not arr:
        return None
    return sum(arr) / len(arr)

def count_elements(arr, target):
    """
    Count occurrences of a target element in an array
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr (list): Input array
        target: Element to count
        
    Returns:
        int: Number of occurrences
        
    Example:
        >>> count_elements([1, 2, 2, 3, 2], 2)
        3
    """
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count

def reverse_array(arr):
    """
    Reverse the elements of an array
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr (list): Input array (will be modified)
        
    Returns:
        list: The reversed array
        
    Example:
        >>> reverse_array([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

def display_array(arr, title="Array"):
    """
    Display array elements in a formatted way
    
    Args:
        arr (list): Input array
        title (str): Title for the display
    """
    print(f"{title}: {arr}")
    print(f"Length: {len(arr)}")

def demonstrate_basic_operations():
    """
    Demonstrate all basic array operations
    """
    print("=" * 50)
    print("BASIC ARRAY OPERATIONS DEMONSTRATION")
    print("=" * 50)
    
    # Create sample array
    numbers = create_sample_array()
    display_array(numbers, "Original Array")
    
    # Find minimum and maximum
    min_val = find_minimum(numbers)
    max_val = find_maximum(numbers)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
    
    # Calculate sum and average
    total = calculate_sum(numbers)
    avg = calculate_average(numbers)
    print(f"Sum: {total}")
    print(f"Average: {avg:.2f}")
    
    # Count specific elements
    count_9 = count_elements(numbers, 9)
    print(f"Count of 9: {count_9}")
    
    # Demonstrate reverse
    numbers_copy = numbers.copy()
    reversed_arr = reverse_array(numbers_copy)
    display_array(reversed_arr, "Reversed Array")
    
    print("=" * 50)

if __name__ == "__main__":
    demonstrate_basic_operations()