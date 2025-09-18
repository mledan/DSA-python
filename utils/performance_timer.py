"""
Performance timing utilities for DSA algorithms
"""

import time
import functools
from typing import Callable, Any

def time_function(func: Callable) -> Callable:
    """Decorator to time function execution"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper

def compare_algorithms(algorithms: list, test_data: list, *args, **kwargs):
    """Compare execution time of multiple algorithms"""
    print(f"Comparing {len(algorithms)} algorithms with test data of size {len(test_data)}")
    print("-" * 50)
    
    results = []
    for name, algorithm in algorithms:
        start_time = time.time()
        result = algorithm(test_data.copy(), *args, **kwargs)  # Use copy to avoid modifying original
        end_time = time.time()
        execution_time = end_time - start_time
        results.append((name, execution_time, result))
        print(f"{name}: {execution_time:.6f} seconds")
    
    # Sort by execution time
    results.sort(key=lambda x: x[1])
    print("\nRanking (fastest to slowest):")
    for i, (name, exec_time, _) in enumerate(results, 1):
        print(f"{i}. {name}: {exec_time:.6f} seconds")
    
    return results

def generate_test_data(size: int, data_type: str = "random") -> list:
    """Generate test data for algorithm testing"""
    import random
    
    if data_type == "random":
        return [random.randint(1, 1000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(1, size + 1))
    elif data_type == "reverse_sorted":
        return list(range(size, 0, -1))
    elif data_type == "nearly_sorted":
        data = list(range(1, size + 1))
        # Randomly swap some elements
        for _ in range(size // 10):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            data[i], data[j] = data[j], data[i]
        return data
    else:
        raise ValueError("data_type must be 'random', 'sorted', 'reverse_sorted', or 'nearly_sorted'")

if __name__ == "__main__":
    # Example usage
    @time_function
    def example_function(data):
        return sum(data)
    
    test_data = generate_test_data(1000)
    result = example_function(test_data)
    print(f"Sum: {result}")

