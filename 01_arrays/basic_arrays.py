"""
Basic Array Operations
Following W3Schools DSA Tutorial: https://www.w3schools.com/dsa/dsa_intro_arrays.php
"""

def create_array():
    """Create and initialize an array"""
    # In Python, we use lists as arrays
    my_array = [7, 12, 9, 4, 11]
    return my_array

def find_minimum(arr):
    """
    Find the minimum value in an array
    Example from W3Schools DSA tutorial
    """
    if not arr:
        return None
    
    min_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
    
    return min_val

def find_maximum(arr):
    """Find the maximum value in an array"""
    if not arr:
        return None
    
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i
    
    return max_val

def array_sum(arr):
    """Calculate the sum of all elements in an array"""
    return sum(arr)

def array_average(arr):
    """Calculate the average of all elements in an array"""
    if not arr:
        return None
    return sum(arr) / len(arr)

def print_array(arr):
    """Print array elements"""
    print("Array:", arr)

# Example usage
if __name__ == "__main__":
    # Create an array
    numbers = create_array()
    print_array(numbers)
    
    # Find minimum value (W3Schools example)
    min_val = find_minimum(numbers)
    print(f'Lowest value: {min_val}')
    
    # Find maximum value
    max_val = find_maximum(numbers)
    print(f'Highest value: {max_val}')
    
    # Calculate sum and average
    total = array_sum(numbers)
    avg = array_average(numbers)
    print(f'Sum: {total}')
    print(f'Average: {avg:.2f}')

