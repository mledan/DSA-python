"""
Test cases for basic array operations
"""

import pytest
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arrays.basic_arrays import (
    create_array, find_minimum, find_maximum, 
    array_sum, array_average, print_array
)

class TestBasicArrays:
    """Test cases for basic array operations"""
    
    def test_create_array(self):
        """Test array creation"""
        arr = create_array()
        assert arr == [7, 12, 9, 4, 11]
        assert len(arr) == 5
    
    def test_find_minimum(self):
        """Test finding minimum value"""
        arr = [7, 12, 9, 4, 11]
        assert find_minimum(arr) == 4
        
        # Test with single element
        assert find_minimum([5]) == 5
        
        # Test with empty array
        assert find_minimum([]) is None
    
    def test_find_maximum(self):
        """Test finding maximum value"""
        arr = [7, 12, 9, 4, 11]
        assert find_maximum(arr) == 12
        
        # Test with single element
        assert find_maximum([5]) == 5
        
        # Test with empty array
        assert find_maximum([]) is None
    
    def test_array_sum(self):
        """Test array sum calculation"""
        arr = [7, 12, 9, 4, 11]
        assert array_sum(arr) == 43
        
        # Test with empty array
        assert array_sum([]) == 0
    
    def test_array_average(self):
        """Test array average calculation"""
        arr = [7, 12, 9, 4, 11]
        assert array_average(arr) == 8.6
        
        # Test with single element
        assert array_average([5]) == 5.0
        
        # Test with empty array
        assert array_average([]) is None

if __name__ == "__main__":
    pytest.main([__file__])

