from colorful_test import TestCase, show_message
from search import Search, NotFoundError

import time


class TestSearch(TestCase):
    
    # =====================
    # LINEAR SEARCH - BASIC FUNCTIONALITY
    # =====================
    
    @show_message(
        success='linear search finds element in list of integers',
        fail='linear search failed to find element in integer list.\nExpected: %s\nReceived %f'
    )
    def test_linear_find_integer(self):
        data = [5, 3, 8, 1, 9, 2]
        result = Search.linear(data, 8, lambda a, b: a == b)
        self.assert_equal(result, 2)
    
    @show_message(
        success='linear search finds element in list of strings',
        fail='linear search failed to find element in string list.\nExpected: %s\nReceived %f'
    )
    def test_linear_find_string(self):
        data = ['apple', 'banana', 'cherry', 'date']
        result = Search.linear(data, 'cherry', lambda a, b: a == b)
        self.assert_equal(result, 2)
    
    @show_message(
        success='linear search finds first element',
        fail='linear search failed to find first element.\nExpected: %s\nReceived %f'
    )
    def test_linear_find_first(self):
        data = [10, 20, 30, 40]
        result = Search.linear(data, 10, lambda a, b: a == b)
        self.assert_equal(result, 0)
    
    @show_message(
        success='linear search finds last element',
        fail='linear search failed to find last element.\nExpected: %s\nReceived %f'
    )
    def test_linear_find_last(self):
        data = [10, 20, 30, 40]
        result = Search.linear(data, 40, lambda a, b: a == b)
        self.assert_equal(result, 3)
    
    @show_message(
        success='linear search finds element in single-element list',
        fail='linear search failed with single-element list.\nExpected: %s\nReceived %f'
    )
    def test_linear_single_element(self):
        data = [42]
        result = Search.linear(data, 42, lambda a, b: a == b)
        self.assert_equal(result, 0)
    
    # =====================
    # LINEAR SEARCH - EDGE CASES
    # =====================
    
    @show_message(
        success='linear search raises NotFoundError when element not in list',
        fail='linear search should raise NotFoundError when element is not found'
    )
    def test_linear_not_found(self):
        data = [1, 2, 3, 4, 5]
        self.assert_raises(NotFoundError, Search.linear, data, 10, lambda a, b: a == b)
    
    @show_message(
        success='linear search raises NotFoundError with empty list',
        fail='linear search should raise NotFoundError with empty list'
    )
    def test_linear_empty_list(self):
        data = []
        self.assert_raises(NotFoundError, Search.linear, data, 5, lambda a, b: a == b)
    
    @show_message(
        success='linear search finds first occurrence of duplicate',
        fail='linear search should find first occurrence of duplicate.\nExpected: %s\nReceived %f'
    )
    def test_linear_duplicate_elements(self):
        data = [1, 2, 3, 2, 4]
        result = Search.linear(data, 2, lambda a, b: a == b)
        self.assert_equal(result, 1)  # Should find first occurrence
    
    @show_message(
        success='linear search works with custom comparator',
        fail='linear search failed with custom comparator.\nExpected: %s\nReceived %f'
    )
    def test_linear_custom_comparator(self):
        data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
        result = Search.linear(data, 'Bob', lambda a, b: a.get('name') == b)
        self.assert_equal(result, 1)
    
    @show_message(
        success='linear search works with floats',
        fail='linear search failed with float values.\nExpected: %s\nReceived %f'
    )
    def test_linear_floats(self):
        data = [1.5, 2.7, 3.9, 4.2]
        result = Search.linear(data, 3.9, lambda a, b: a == b)
        self.assert_equal(result, 2)
    
    @show_message(
        success='linear search works with negative numbers',
        fail='linear search failed with negative numbers.\nExpected: %s\nReceived %f'
    )
    def test_linear_negative_numbers(self):
        data = [-5, -3, 0, 2, 4]
        result = Search.linear(data, -3, lambda a, b: a == b)
        self.assert_equal(result, 1)

    # =====================
    # LINEAR SEARCH - PERFORMANCE
    # =====================

    @show_message(
        success='linear search completes within reasonable time for large dataset',
        fail='linear search took too long. Should complete in under 0.1 second.'
    )
    def test_linear_search_performance(self):
        # Create large dataset
        data = list(range(100000))
        target = 99999  # Worst case - last element
        
        start_time = time.time()
        result = Search.linear(data, target, lambda a, b: a == b)
        elapsed_time = time.time() - start_time
        
        self.assert_equal(result, 99999)
        self.assert_true(elapsed_time < 0.1)
    
    # =====================
    # BINARY SEARCH - BASIC FUNCTIONALITY
    # =====================
    
    @show_message(
        success='binary search finds element in sorted list',
        fail='binary search failed to find element in sorted list.\nExpected: %s\nReceived %f'
    )
    def test_binary_find_middle(self):
        data = [1, 3, 5, 7, 9, 11, 13]
        result = Search.binary(data, 7, lambda a, b: a - b)
        self.assert_equal(result, 3)
    
    @show_message(
        success='binary search finds first element',
        fail='binary search failed to find first element.\nExpected: %s\nReceived %f'
    )
    def test_binary_find_first(self):
        data = [2, 4, 6, 8, 10]
        result = Search.binary(data, 2, lambda a, b: a - b)
        self.assert_equal(result, 0)
    
    @show_message(
        success='binary search finds last element',
        fail='binary search failed to find last element.\nExpected: %s\nReceived %f'
    )
    def test_binary_find_last(self):
        data = [2, 4, 6, 8, 10]
        result = Search.binary(data, 10, lambda a, b: a - b)
        self.assert_equal(result, 4)
    
    @show_message(
        success='binary search finds element in single-element list',
        fail='binary search failed with single-element list.\nExpected: %s\nReceived %f'
    )
    def test_binary_single_element_found(self):
        data = [42]
        result = Search.binary(data, 42, lambda a, b: a - b)
        self.assert_equal(result, 0)
    
    @show_message(
        success='binary search works with two-element list',
        fail='binary search failed with two-element list.\nExpected: %s\nReceived %f'
    )
    def test_binary_two_elements(self):
        data = [5, 10]
        result1 = Search.binary(data, 5, lambda a, b: a - b)
        result2 = Search.binary(data, 10, lambda a, b: a - b)
        self.assert_equal(result1, 0)
        self.assert_equal(result2, 1)
    
    # =====================
    # BINARY SEARCH - EDGE CASES
    # =====================
    
    @show_message(
        success='binary search returns NotFoundError when element not in list',
        fail='binary search should return NotFoundError when element not found'
    )
    def test_binary_not_found(self):
        data = [1, 3, 5, 7, 9]
        self.assert_raises(NotFoundError, Search.binary, data, 6, lambda a, b: a - b)

    @show_message(
        success='binary search returns NotFoundError with empty list',
        fail='binary search should return NotFoundError with empty list'
    )
    def test_binary_empty_list(self):
        data = []
        self.assert_raises(NotFoundError, Search.binary, data, 5, lambda a, b: a - b)

    @show_message(
        success='binary search returns NotFoundError for element smaller than all',
        fail='binary search should return NotFoundError for element smaller than all'
    )
    def test_binary_target_too_small(self):
        data = [10, 20, 30, 40]
        self.assert_raises(NotFoundError, Search.binary, data, 5, lambda a, b: a - b)

    @show_message(
        success='binary search returns NotFoundError for element larger than all',
        fail='binary search should return NotFoundError for element larger than all'
    )
    def test_binary_target_too_large(self):
        data = [10, 20, 30, 40]
        self.assert_raises(NotFoundError, Search.binary, data, 50, lambda a, b: a - b)
    
    @show_message(
        success='binary search works with negative numbers',
        fail='binary search failed with negative numbers.\nExpected: %s\nReceived %f'
    )
    def test_binary_negative_numbers(self):
        data = [-10, -5, 0, 5, 10]
        result = Search.binary(data, -5, lambda a, b: a - b)
        self.assert_equal(result, 1)
    
    @show_message(
        success='binary search works with floats',
        fail='binary search failed with floats.\nExpected: %s\nReceived %f'
    )
    def test_binary_floats(self):
        data = [1.1, 2.2, 3.3, 4.4, 5.5]
        result = Search.binary(data, 3.3, lambda a, b: int((a - b) * 10))
        self.assert_equal(result, 2)
    
    @show_message(
        success='binary search works with large sorted list',
        fail='binary search failed with large sorted list.\nExpected: %s\nReceived %f'
    )
    def test_binary_large_list(self):
        data = list(range(0, 1000, 2))  # [0, 2, 4, ..., 998]
        result = Search.binary(data, 500, lambda a, b: a - b)
        self.assert_equal(result, 250)
    
    @show_message(
        success='binary search works with strings using custom comparator',
        fail='binary search failed with strings.\nExpected: %s\nReceived %f'
    )
    def test_binary_strings(self):
        data = ['apple', 'banana', 'cherry', 'date', 'grape']
        def string_comparator(a, b):
            if a < b:
                return -1
            elif a > b:
                return 1
            return 0
        result = Search.binary(data, 'cherry', string_comparator)
        self.assert_equal(result, 2)

    # =====================
    # BINARY SEARCH - PERFORMANCE
    # =====================

    @show_message(
        success='binary search completes within reasonable time for large dataset',
        fail='binary search took too long. Should complete in under 0.01 seconds.'
    )
    def test_binary_search_performance(self):
        # Create large sorted dataset
        data = list(range(1000000))
        target = 999999  # Worst case
        
        start_time = time.time()
        result = Search.binary(data, target, lambda a, b: a - b)
        elapsed_time = time.time() - start_time
        
        self.assert_equal(result, 999999)
        self.assert_true(elapsed_time < 0.01)
    
    # =====================
    # ERROR HANDLING
    # =====================
    
    @show_message(
        success='NotFoundError can be caught and handled properly',
        fail='NotFoundError should be catchable'
    )
    def test_not_found_error_exception(self):
        data = [1, 2, 3]
        try:
            Search.linear(data, 10, lambda a, b: a == b)
            # Should not reach here
            assert False
        except NotFoundError as e:
            # Expected behavior
            assert True


if __name__ == '__main__':
    TestSearch.run_and_output_results(fail_fast=False)
