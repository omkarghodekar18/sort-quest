# SortQuest

A lightweight Python library providing common sorting and searching algorithms with a flexible, comparator-based approach.

## Overview

SortQuest is a small educational library that implements fundamental algorithms for sorting and searching data. Each algorithm accepts custom comparator functions, making it easy to sort and search any data type with your own comparison logic.

## Features

- **Multiple Sorting Algorithms**: Merge sort, insertion sort, and bubble sort
- **Search Algorithms**: Linear search and binary search
- **Helper Comparators**: Pre-built comparison functions for common use cases
- **Flexible & Type-Agnostic**: Works with integers, floats, strings, or custom objects
- **Educational**: Clear implementations perfect for learning algorithm fundamentals

## Project Structure

```
.
├── helpers.py         # Comparator helper functions (✅ Complete)
├── sort.py            # Sorting algorithms (🚧 Needs implementation)
├── search.py          # Search algorithms (🚧 Needs implementation)
├── test_helpers.py    # Tests for helpers
├── test_sort.py       # Tests for sorting algorithms
└── test_search.py     # Tests for search algorithms
```

## Contributing

We welcome contributions! This project is a great way to practice implementing classic algorithms and writing clean, tested code.

### Getting Started

1. **Fork and clone this repository**

2. **Install the testing framework**
   ```bash
   pip install colorful-test
   ```

3. **Choose a method to implement**
   - Check `sort.py` or `search.py` for methods that need implementation
   - Each method has comprehensive tests already written
   - The `helpers.py` module is complete and serves as a reference

4. **Implement your chosen method**
   - Read the method's docstring to understand the requirements
   - Follow the existing code style and structure
   - Ensure your implementation handles edge cases

5. **Run the tests**
   ```bash
   python3 -m colorful_test test_sort.py
   # or
   python3 -m colorful_test test_search.py
   # or
   python3 -m colorful_test test_helpers.py
   ```

6. **Ensure all tests pass**
   - Your implementation should pass all associated tests
   - Tests cover basic functionality, edge cases, and error handling
   - Performance tests ensure efficiency

7. **Submit a Pull Request**
   - Create a PR with a clear description of what you implemented
   - Reference the specific method(s) you worked on
   - Make sure all tests pass before submitting

### Implementation Guidelines

- **Do not modify test files** - they are complete and correct
- **Maintain the existing function signatures** - tests depend on them
- **Handle edge cases** - empty lists, single elements, duplicates, etc.
- **Keep it simple** - clear, readable code is better than clever code
- **Test locally first** - make sure everything works before submitting

### What to Implement

#### `sort.py` - Sorting Methods
- `Sorter.merge()` - Merge sort algorithm
- `Sorter.insertion()` - Insertion sort algorithm
- `Sorter.bubble()` - Bubble sort algorithm
- `Sorter.sort()` - Dispatcher method (delegates to other sort methods)

#### `search.py` - Search Methods
- `Search.linear()` - Linear search algorithm
- `Search.binary()` - Binary search algorithm

### Example: Running Tests

```bash
# Run all tests in a specific file
python3 -m colorful_test test_sort.py

# The output will show which tests pass/fail with helpful messages
```

## Usage Examples

Once implemented, the library can be used like this:

```python
from sort import Sorter
from search import Search
from helpers import Helpers

# Sorting
data = [5, 2, 8, 1, 9]
sorted_data = Sorter.merge(data, Helpers.number_asc)
print(sorted_data)  # [1, 2, 5, 8, 9]

# Searching
index = Search.binary(sorted_data, 8, lambda a, b: a - b)
print(index)  # 3

# Custom comparators
words = ['apple', 'pie', 'banana', 'kiwi']
by_length = Sorter.sort(words, Helpers.length_asc)
print(by_length)  # ['pie', 'kiwi', 'apple', 'banana']
```

## Questions?

If you have questions about implementation details or need clarification on any algorithm, feel free to open an issue for discussion.

## License

This project is open source and available for educational purposes.
