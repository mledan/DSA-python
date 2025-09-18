"""
Test cases for basic array operations
"""

import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from basic_operations import (
    create_sample_array, find_minimum, find_maximum, 
    calculate_sum, calculate_average, count_elements,
    reverse_array, display_array
)

class TestBasicArrayOperations:
    """Test cases for basic array operations"""
    
    def test_create_sample_array(self):
        """Test sample array creation"""
        arr = create_sample_array()
        assert arr == [7, 12, 9, 4, 11]
        assert len(arr) == 5
        assert all(isinstance(x, int) for x in arr)
    
    def test_find_minimum(self):
        """Test finding minimum value"""
        # Test with sample array
        arr = [7, 12, 9, 4, 11]
        assert find_minimum(arr) == 4
        
        # Test with single element
        assert find_minimum([5]) == 5
        
        # Test with empty array
        assert find_minimum([]) is None
        
        # Test with negative numbers
        assert find_minimum([-1, -5, -3]) == -5
        
        # Test with duplicate minimum values
        assert find_minimum([1, 1, 2, 3]) == 1
    
    def test_find_maximum(self):
        """Test finding maximum value"""
        # Test with sample array
        arr = [7, 12, 9, 4, 11]
        assert find_maximum(arr) == 12
        
        # Test with single element
        assert find_maximum([5]) == 5
        
        # Test with empty array
        assert find_maximum([]) is None
        
        # Test with negative numbers
        assert find_maximum([-1, -5, -3]) == -1
        
        # Test with duplicate maximum values
        assert find_maximum([1, 3, 3, 2]) == 3
    
    def test_calculate_sum(self):
        """Test array sum calculation"""
        # Test with sample array
        arr = [7, 12, 9, 4, 11]
        assert calculate_sum(arr) == 43
        
        # Test with empty array
        assert calculate_sum([]) == 0
        
        # Test with single element
        assert calculate_sum([5]) == 5
        
        # Test with negative numbers
        assert calculate_sum([-1, 2, -3]) == -2
        
        # Test with zeros
        assert calculate_sum([0, 0, 0]) == 0
    
    def test_calculate_average(self):
        """Test array average calculation"""
        # Test with sample array
        arr = [7, 12, 9, 4, 11]
        assert calculate_average(arr) == 8.6
        
        # Test with single element
        assert calculate_average([5]) == 5.0
        
        # Test with empty array
        assert calculate_average([]) is None
        
        # Test with negative numbers
        assert calculate_average([-2, 4, -6]) == -4/3
        
        # Test with zeros
        assert calculate_average([0, 0, 0]) == 0.0
    
    def test_count_elements(self):
        """Test counting element occurrences"""
        # Test with sample array
        arr = [1, 2, 2, 3, 2]
        assert count_elements(arr, 2) == 3
        assert count_elements(arr, 1) == 1
        assert count_elements(arr, 4) == 0
        
        # Test with empty array
        assert count_elements([], 5) == 0
        
        # Test with single element
        assert count_elements([5], 5) == 1
        assert count_elements([5], 3) == 0
    
    def test_reverse_array(self):
        """Test array reversal"""
        # Test with sample array
        arr = [1, 2, 3, 4, 5]
        reversed_arr = reverse_array(arr)
        assert reversed_arr == [5, 4, 3, 2, 1]
        
        # Test with empty array
        empty_arr = []
        assert reverse_array(empty_arr) == []
        
        # Test with single element
        single_arr = [42]
        assert reverse_array(single_arr) == [42]
        
        # Test with two elements
        two_arr = [1, 2]
        assert reverse_array(two_arr) == [2, 1]
        
        # Test that original array is modified
        original = [1, 2, 3]
        reverse_array(original)
        assert original == [3, 2, 1]

if __name__ == "__main__":
    pytest.main([__file__])
