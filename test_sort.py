from colorful_test import TestCase, show_message
from sort import Sorter

import time

class TestSorter(TestCase):
    
    # =====================
    # MERGE SORT - BASIC FUNCTIONALITY
    # =====================
    
    @show_message(
        success='merge sort works with unsorted integers (ascending)',
        fail='merge sort failed to sort integers in ascending order.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_asc_integers(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 2, 5, 8, 9])
    
    @show_message(
        success='merge sort works with unsorted integers (descending)',
        fail='merge sort failed to sort integers in descending order.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_desc_integers(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.merge(data, lambda a, b: a > b)
        self.assert_equal(result, [9, 8, 5, 2, 1])
    
    @show_message(
        success='merge sort works with strings (alphabetical)',
        fail='merge sort failed to sort strings alphabetically.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_strings(self):
        data = ['zebra', 'apple', 'banana', 'cherry']
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, ['apple', 'banana', 'cherry', 'zebra'])
    
    @show_message(
        success='merge sort does not modify original list',
        fail='merge sort should not modify the original list.\nOriginal should remain: %s'
    )
    def test_merge_sort_immutable(self):
        data = [5, 2, 8, 1, 9]
        original = data[:]
        Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(data, original)
    
    # =====================
    # MERGE SORT - EDGE CASES
    # =====================
    
    @show_message(
        success='merge sort handles empty list',
        fail='merge sort failed with empty list.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_empty(self):
        data = []
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, [])
    
    @show_message(
        success='merge sort handles single element',
        fail='merge sort failed with single element.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_single(self):
        data = [42]
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, [42])
    
    @show_message(
        success='merge sort handles already sorted list',
        fail='merge sort failed with already sorted list.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 2, 3, 4, 5])
    
    @show_message(
        success='merge sort handles reverse sorted list',
        fail='merge sort failed with reverse sorted list.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 2, 3, 4, 5])
    
    @show_message(
        success='merge sort handles duplicate elements',
        fail='merge sort failed with duplicate elements.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_duplicates(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    @show_message(
        success='merge sort handles negative numbers',
        fail='merge sort failed with negative numbers.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_negatives(self):
        data = [3, -1, 4, -5, 0, 2]
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, [-5, -1, 0, 2, 3, 4])
    
    @show_message(
        success='merge sort handles floats',
        fail='merge sort failed with floats.\nExpected: %s\nReceived %f'
    )
    def test_merge_sort_floats(self):
        data = [3.5, 1.2, 4.7, 2.1]
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, [1.2, 2.1, 3.5, 4.7])
    
    # =====================
    # INSERTION SORT - BASIC FUNCTIONALITY
    # =====================
    
    @show_message(
        success='insertion sort works with unsorted integers (ascending)',
        fail='insertion sort failed to sort integers in ascending order.\nExpected: %s\nReceived %f'
    )
    def test_insertion_sort_asc_integers(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.insertion(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 2, 5, 8, 9])
    
    @show_message(
        success='insertion sort works with unsorted integers (descending)',
        fail='insertion sort failed to sort integers in descending order.\nExpected: %s\nReceived %f'
    )
    def test_insertion_sort_desc_integers(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.insertion(data, lambda a, b: a > b)
        self.assert_equal(result, [9, 8, 5, 2, 1])
    
    @show_message(
        success='insertion sort works with strings (alphabetical)',
        fail='insertion sort failed to sort strings alphabetically.\nExpected: %s\nReceived %f'
    )
    def test_insertion_sort_strings(self):
        data = ['zebra', 'apple', 'banana', 'cherry']
        result = Sorter.insertion(data, lambda a, b: a < b)
        self.assert_equal(result, ['apple', 'banana', 'cherry', 'zebra'])
    
    @show_message(
        success='insertion sort does not modify original list',
        fail='insertion sort should not modify the original list.\nOriginal should remain: %s'
    )
    def test_insertion_sort_immutable(self):
        data = [5, 2, 8, 1, 9]
        original = data[:]
        Sorter.insertion(data, lambda a, b: a < b)
        self.assert_equal(data, original)
    
    # =====================
    # INSERTION SORT - EDGE CASES
    # =====================
    
    @show_message(
        success='insertion sort handles empty list',
        fail='insertion sort failed with empty list.\nExpected: %s\nReceived %f'
    )
    def test_insertion_sort_empty(self):
        data = []
        result = Sorter.insertion(data, lambda a, b: a < b)
        self.assert_equal(result, [])
    
    @show_message(
        success='insertion sort handles single element',
        fail='insertion sort failed with single element.\nExpected: %s\nReceived %f'
    )
    def test_insertion_sort_single(self):
        data = [42]
        result = Sorter.insertion(data, lambda a, b: a < b)
        self.assert_equal(result, [42])
    
    @show_message(
        success='insertion sort handles already sorted list',
        fail='insertion sort failed with already sorted list.\nExpected: %s\nReceived %f'
    )
    def test_insertion_sort_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        result = Sorter.insertion(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 2, 3, 4, 5])
    
    @show_message(
        success='insertion sort handles duplicate elements',
        fail='insertion sort failed with duplicate elements.\nExpected: %s\nReceived %f'
    )
    def test_insertion_sort_duplicates(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = Sorter.insertion(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    @show_message(
        success='insertion sort handles negative numbers',
        fail='insertion sort failed with negative numbers.\nExpected: %s\nReceived %f'
    )
    def test_insertion_sort_negatives(self):
        data = [3, -1, 4, -5, 0, 2]
        result = Sorter.insertion(data, lambda a, b: a < b)
        self.assert_equal(result, [-5, -1, 0, 2, 3, 4])
    
    # =====================
    # BUBBLE SORT - BASIC FUNCTIONALITY
    # =====================
    
    @show_message(
        success='bubble sort works with unsorted integers (ascending)',
        fail='bubble sort failed to sort integers in ascending order.\nExpected: %s\nReceived %f'
    )
    def test_bubble_sort_asc_integers(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.bubble(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 2, 5, 8, 9])
    
    @show_message(
        success='bubble sort works with unsorted integers (descending)',
        fail='bubble sort failed to sort integers in descending order.\nExpected: %s\nReceived %f'
    )
    def test_bubble_sort_desc_integers(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.bubble(data, lambda a, b: a > b)
        self.assert_equal(result, [9, 8, 5, 2, 1])
    
    @show_message(
        success='bubble sort works with strings (alphabetical)',
        fail='bubble sort failed to sort strings alphabetically.\nExpected: %s\nReceived %f'
    )
    def test_bubble_sort_strings(self):
        data = ['zebra', 'apple', 'banana', 'cherry']
        result = Sorter.bubble(data, lambda a, b: a < b)
        self.assert_equal(result, ['apple', 'banana', 'cherry', 'zebra'])
    
    @show_message(
        success='bubble sort does not modify original list',
        fail='bubble sort should not modify the original list.\nOriginal should remain: %s'
    )
    def test_bubble_sort_immutable(self):
        data = [5, 2, 8, 1, 9]
        original = data[:]
        Sorter.bubble(data, lambda a, b: a < b)
        self.assert_equal(data, original)
    
    # =====================
    # BUBBLE SORT - EDGE CASES
    # =====================
    
    @show_message(
        success='bubble sort handles empty list',
        fail='bubble sort failed with empty list.\nExpected: %s\nReceived %f'
    )
    def test_bubble_sort_empty(self):
        data = []
        result = Sorter.bubble(data, lambda a, b: a < b)
        self.assert_equal(result, [])
    
    @show_message(
        success='bubble sort handles single element',
        fail='bubble sort failed with single element.\nExpected: %s\nReceived %f'
    )
    def test_bubble_sort_single(self):
        data = [42]
        result = Sorter.bubble(data, lambda a, b: a < b)
        self.assert_equal(result, [42])
    
    @show_message(
        success='bubble sort handles already sorted list',
        fail='bubble sort failed with already sorted list.\nExpected: %s\nReceived %f'
    )
    def test_bubble_sort_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        result = Sorter.bubble(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 2, 3, 4, 5])
    
    @show_message(
        success='bubble sort handles duplicate elements',
        fail='bubble sort failed with duplicate elements.\nExpected: %s\nReceived %f'
    )
    def test_bubble_sort_duplicates(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = Sorter.bubble(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    # =====================
    # SORT METHOD - DISPATCHER
    # =====================
    
    @show_message(
        success='sort method dispatches to merge sort correctly',
        fail='sort method failed to dispatch to merge sort.\nExpected: %s\nReceived %f'
    )
    def test_sort_method_merge(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.sort(data, lambda a, b: a < b, method='merge')
        self.assert_equal(result, [1, 2, 5, 8, 9])
    
    @show_message(
        success='sort method dispatches to insertion sort correctly',
        fail='sort method failed to dispatch to insertion sort.\nExpected: %s\nReceived %f'
    )
    def test_sort_method_insertion(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.sort(data, lambda a, b: a < b, method='insertion')
        self.assert_equal(result, [1, 2, 5, 8, 9])
    
    @show_message(
        success='sort method dispatches to bubble sort correctly',
        fail='sort method failed to dispatch to bubble sort.\nExpected: %s\nReceived %f'
    )
    def test_sort_method_bubble(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.sort(data, lambda a, b: a < b, method='bubble')
        self.assert_equal(result, [1, 2, 5, 8, 9])
    
    @show_message(
        success='sort method defaults to merge sort',
        fail='sort method should default to merge sort.\nExpected: %s\nReceived %f'
    )
    def test_sort_method_default(self):
        data = [5, 2, 8, 1, 9]
        result = Sorter.sort(data, lambda a, b: a < b)
        self.assert_equal(result, [1, 2, 5, 8, 9])
    
    @show_message(
        success='sort method is case-insensitive for method names',
        fail='sort method should be case-insensitive.\nExpected: %s\nReceived %f'
    )
    def test_sort_method_case_insensitive(self):
        data = [5, 2, 8, 1, 9]
        result1 = Sorter.sort(data, lambda a, b: a < b, method='MERGE')
        result2 = Sorter.sort(data, lambda a, b: a < b, method='Insertion')
        result3 = Sorter.sort(data, lambda a, b: a < b, method='BuBbLe')
        self.assert_equal(result1, [1, 2, 5, 8, 9])
        self.assert_equal(result2, [1, 2, 5, 8, 9])
        self.assert_equal(result3, [1, 2, 5, 8, 9])
    
    # =====================
    # ERROR HANDLING
    # =====================
    
    @show_message(
        success='sort method raises ValueError for unknown method',
        fail='sort method should raise ValueError for unknown method'
    )
    def test_sort_method_invalid(self):
        data = [5, 2, 8, 1, 9]
        self.assert_raises(ValueError, Sorter.sort, data, lambda a, b: a < b, 'quicksort')
    
    @show_message(
        success='sort method raises ValueError with empty method string',
        fail='sort method should raise ValueError with empty method string'
    )
    def test_sort_method_empty_string(self):
        data = [5, 2, 8, 1, 9]
        self.assert_raises(ValueError, Sorter.sort, data, lambda a, b: a < b, '')
    
    # =====================
    # COMPLEX SCENARIOS
    # =====================
    
    @show_message(
        success='all sort methods produce same result for same input',
        fail='all sort methods should produce the same sorted result'
    )
    def test_all_methods_consistency(self):
        data = [7, 3, 9, 1, 5, 2, 8, 4, 6]
        comparator = lambda a, b: a < b
        
        result_merge = Sorter.merge(data, comparator)
        result_insertion = Sorter.insertion(data, comparator)
        result_bubble = Sorter.bubble(data, comparator)
        
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assert_equal(result_merge, expected)
        self.assert_equal(result_insertion, expected)
        self.assert_equal(result_bubble, expected)
    
    @show_message(
        success='sort methods work with custom objects and comparators',
        fail='sort methods should work with custom objects.\nExpected: %s\nReceived %f'
    )
    def test_sort_custom_objects(self):
        data = [
            {'name': 'Charlie', 'age': 35},
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 30}
        ]
        comparator = lambda a, b: a['age'] < b['age']
        
        result = Sorter.merge(data, comparator)
        self.assert_equal(result[0]['name'], 'Alice')
        self.assert_equal(result[1]['name'], 'Bob')
        self.assert_equal(result[2]['name'], 'Charlie')
    
    @show_message(
        success='sort methods handle large lists efficiently',
        fail='sort methods should handle large lists.\nExpected sorted list'
    )
    def test_sort_large_list(self):
        import random
        data = list(range(100, 0, -1))  # [100, 99, 98, ..., 1]
        result = Sorter.merge(data, lambda a, b: a < b)
        self.assert_equal(result, list(range(1, 101)))
    

    # ====================
    # PERFORMANCE
    # ====================

    @show_message(
        success='merge sort completes within reasonable time for large dataset',
        fail='merge sort took too long. Should complete in under 0.7 seconds.'
    )
    def test_merge_sort_performance(self):
        import random
        data = [random.randint(1, 100000) for _ in range(100000)]
        
        start_time = time.time()
        result = Sorter.merge(data, lambda a, b: a < b)
        elapsed_time = time.time() - start_time
        
        # Verify it's actually sorted
        self.assert_equal(result, sorted(data))
        self.assert_true(elapsed_time < 0.7)

    @show_message(
        success='insertion sort completes within reasonable time for moderate dataset',
        fail='insertion sort took too long. Should complete in under 0.1 seconds.'
    )
    def test_insertion_sort_performance(self):
        import random
        data = [random.randint(1, 1000) for _ in range(1000)]
        
        start_time = time.time()
        result = Sorter.insertion(data, lambda a, b: a < b)
        elapsed_time = time.time() - start_time
        
        self.assert_equal(result, sorted(data))
        self.assert_true(elapsed_time < 0.1)

    @show_message(
        success='bubble sort completes within reasonable time for moderate dataset',
        fail='bubble sort took too long. Should complete in under 0.3 seconds.'
    )
    def test_bubble_sort_performance(self):
        import random
        data = [random.randint(1, 1000) for _ in range(1000)]
        
        start_time = time.time()
        result = Sorter.bubble(data, lambda a, b: a < b)
        elapsed_time = time.time() - start_time
        
        self.assert_equal(result, sorted(data))
        self.assert_true(elapsed_time < 0.3)


if __name__ == '__main__':
    TestSorter.run_and_output_results(fail_fast=False)
