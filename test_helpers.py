from colorful_test import TestCase, show_message
from helpers import Helpers


class TestHelpers(TestCase):
    
    # =====================
    # NUMERIC COMPARATORS
    # =====================
    
    @show_message(
        success='number_asc works correctly with integers',
        fail='number_asc failed with integers. Expected True when first number is smaller.\nExpected: %s\nReceived: %s'
    )
    def test_number_asc_integers(self):
        self.assert_equal(Helpers.number_asc(1, 2), True)
        self.assert_equal(Helpers.number_asc(2, 1), False)
        self.assert_equal(Helpers.number_asc(5, 5), False)
    
    @show_message(
        success='number_asc works correctly with floats',
        fail='number_asc failed with floats.\nExpected: %s\nReceived: %s'
    )
    def test_number_asc_floats(self):
        self.assert_equal(Helpers.number_asc(1.5, 2.7), True)
        self.assert_equal(Helpers.number_asc(3.9, 1.2), False)
        self.assert_equal(Helpers.number_asc(2.5, 2.5), False)
    
    @show_message(
        success='number_asc works correctly with mixed int and float',
        fail='number_asc failed with mixed types.\nExpected: %s\nReceived: %s'
    )
    def test_number_asc_mixed(self):
        self.assert_equal(Helpers.number_asc(1, 2.5), True)
        self.assert_equal(Helpers.number_asc(3.7, 2), False)
    
    @show_message(
        success='number_asc works correctly with negative numbers',
        fail='number_asc failed with negative numbers.\nExpected: %s\nReceived: %s'
    )
    def test_number_asc_negatives(self):
        self.assert_equal(Helpers.number_asc(-5, -2), True)
        self.assert_equal(Helpers.number_asc(-2, -5), False)
        self.assert_equal(Helpers.number_asc(-3, 3), True)
    
    @show_message(
        success='number_asc works correctly with zero',
        fail='number_asc failed with zero.\nExpected: %s\nReceived: %s'
    )
    def test_number_asc_zero(self):
        self.assert_equal(Helpers.number_asc(0, 1), True)
        self.assert_equal(Helpers.number_asc(1, 0), False)
        self.assert_equal(Helpers.number_asc(0, 0), False)
    
    @show_message(
        success='number_desc works correctly with integers',
        fail='number_desc failed with integers. Expected True when first number is larger.\nExpected: %s\nReceived: %s'
    )
    def test_number_desc_integers(self):
        self.assert_equal(Helpers.number_desc(2, 1), True)
        self.assert_equal(Helpers.number_desc(1, 2), False)
        self.assert_equal(Helpers.number_desc(5, 5), False)
    
    @show_message(
        success='number_desc works correctly with floats',
        fail='number_desc failed with floats.\nExpected: %s\nReceived: %s'
    )
    def test_number_desc_floats(self):
        self.assert_equal(Helpers.number_desc(5.8, 2.3), True)
        self.assert_equal(Helpers.number_desc(1.1, 4.4), False)
    
    @show_message(
        success='number_desc works correctly with negative numbers',
        fail='number_desc failed with negative numbers.\nExpected: %s\nReceived: %s'
    )
    def test_number_desc_negatives(self):
        self.assert_equal(Helpers.number_desc(-2, -5), True)
        self.assert_equal(Helpers.number_desc(-5, -2), False)
    
    # =====================
    # ALPHABETICAL COMPARATORS
    # =====================
    
    @show_message(
        success='alpha_asc works correctly with lowercase strings',
        fail='alpha_asc failed with lowercase strings.\nExpected: %s\nReceived: %s'
    )
    def test_alpha_asc_lowercase(self):
        self.assert_equal(Helpers.alpha_asc('apple', 'banana'), True)
        self.assert_equal(Helpers.alpha_asc('zebra', 'ant'), False)
        self.assert_equal(Helpers.alpha_asc('cat', 'cat'), False)
    
    @show_message(
        success='alpha_asc is case-insensitive',
        fail='alpha_asc should be case-insensitive but is not.\nExpected: %s\nReceived: %s'
    )
    def test_alpha_asc_case_insensitive(self):
        self.assert_equal(Helpers.alpha_asc('Apple', 'banana'), True)
        self.assert_equal(Helpers.alpha_asc('ZEBRA', 'ant'), False)
        self.assert_equal(Helpers.alpha_asc('Cat', 'CAT'), False)
    
    @show_message(
        success='alpha_asc works correctly with mixed case',
        fail='alpha_asc failed with mixed case strings.\nExpected: %s\nReceived: %s'
    )
    def test_alpha_asc_mixed_case(self):
        self.assert_equal(Helpers.alpha_asc('AbC', 'aBd'), True)
        self.assert_equal(Helpers.alpha_asc('XyZ', 'abc'), False)
    
    @show_message(
        success='alpha_asc works correctly with single characters',
        fail='alpha_asc failed with single characters.\nExpected: %s\nReceived: %s'
    )
    def test_alpha_asc_single_char(self):
        self.assert_equal(Helpers.alpha_asc('a', 'b'), True)
        self.assert_equal(Helpers.alpha_asc('Z', 'a'), False)
    
    @show_message(
        success='alpha_asc works correctly with empty strings',
        fail='alpha_asc failed with empty strings.\nExpected: %s\nReceived: %s'
    )
    def test_alpha_asc_empty_strings(self):
        self.assert_equal(Helpers.alpha_asc('', 'a'), True)
        self.assert_equal(Helpers.alpha_asc('a', ''), False)
        self.assert_equal(Helpers.alpha_asc('', ''), False)
    
    @show_message(
        success='alpha_desc works correctly with lowercase strings',
        fail='alpha_desc failed with lowercase strings.\nExpected: %s\nReceived: %s'
    )
    def test_alpha_desc_lowercase(self):
        self.assert_equal(Helpers.alpha_desc('banana', 'apple'), True)
        self.assert_equal(Helpers.alpha_desc('ant', 'zebra'), False)
        self.assert_equal(Helpers.alpha_desc('cat', 'cat'), False)
    
    @show_message(
        success='alpha_desc is case-insensitive',
        fail='alpha_desc should be case-insensitive but is not.\nExpected: %s\nReceived: %s'
    )
    def test_alpha_desc_case_insensitive(self):
        self.assert_equal(Helpers.alpha_desc('Zebra', 'apple'), True)
        self.assert_equal(Helpers.alpha_desc('ANT', 'Zebra'), False)
    
    # =====================
    # LENGTH-BASED COMPARATORS
    # =====================
    
    @show_message(
        success='length_asc works correctly with different length strings',
        fail='length_asc failed. Expected True when first string is shorter.\nExpected: %s\nReceived: %s'
    )
    def test_length_asc_basic(self):
        self.assert_equal(Helpers.length_asc('hi', 'hello'), True)
        self.assert_equal(Helpers.length_asc('world', 'hi'), False)
        self.assert_equal(Helpers.length_asc('test', 'test'), False)
    
    @show_message(
        success='length_asc works correctly with empty strings',
        fail='length_asc failed with empty strings.\nExpected: %s\nReceived: %s'
    )
    def test_length_asc_empty(self):
        self.assert_equal(Helpers.length_asc('', 'a'), True)
        self.assert_equal(Helpers.length_asc('a', ''), False)
        self.assert_equal(Helpers.length_asc('', ''), False)
    
    @show_message(
        success='length_asc works correctly with very long strings',
        fail='length_asc failed with very long strings.\nExpected: %s\nReceived: %s'
    )
    def test_length_asc_long_strings(self):
        short = 'a'
        long = 'a' * 1000
        self.assert_equal(Helpers.length_asc(short, long), True)
        self.assert_equal(Helpers.length_asc(long, short), False)
    
    @show_message(
        success='length_desc works correctly with different length strings',
        fail='length_desc failed. Expected True when first string is longer.\nExpected: %s\nReceived: %s'
    )
    def test_length_desc_basic(self):
        self.assert_equal(Helpers.length_desc('hello', 'hi'), True)
        self.assert_equal(Helpers.length_desc('hi', 'world'), False)
        self.assert_equal(Helpers.length_desc('test', 'test'), False)
    
    @show_message(
        success='length_desc works correctly with empty strings',
        fail='length_desc failed with empty strings.\nExpected: %s\nReceived: %s'
    )
    def test_length_desc_empty(self):
        self.assert_equal(Helpers.length_desc('a', ''), True)
        self.assert_equal(Helpers.length_desc('', 'a'), False)
    
    # =====================
    # REVERSE WRAPPER
    # =====================
    
    @show_message(
        success='reverse correctly inverts number_asc comparator',
        fail='reverse failed to invert number_asc.\nExpected: %s\nReceived: %s'
    )
    def test_reverse_number_asc(self):
        reversed_comp = Helpers.reverse(Helpers.number_asc)
        # If number_asc(1, 2) is True, reversed should be False
        self.assert_equal(reversed_comp(1, 2), False)
        self.assert_equal(reversed_comp(2, 1), True)
    
    @show_message(
        success='reverse correctly inverts alpha_asc comparator',
        fail='reverse failed to invert alpha_asc.\nExpected: %s\nReceived: %s'
    )
    def test_reverse_alpha_asc(self):
        reversed_comp = Helpers.reverse(Helpers.alpha_asc)
        self.assert_equal(reversed_comp('apple', 'banana'), False)
        self.assert_equal(reversed_comp('zebra', 'ant'), True)
    
    @show_message(
        success='reverse correctly inverts length_asc comparator',
        fail='reverse failed to invert length_asc.\nExpected: %s\nReceived: %s'
    )
    def test_reverse_length_asc(self):
        reversed_comp = Helpers.reverse(Helpers.length_asc)
        self.assert_equal(reversed_comp('hi', 'hello'), False)
        self.assert_equal(reversed_comp('world', 'hi'), True)
    
    @show_message(
        success='reverse works with custom comparator functions',
        fail='reverse failed with custom comparator.\nExpected: %s\nReceived: %s'
    )
    def test_reverse_custom_comparator(self):
        # Custom comparator: checks if first element is even and second is odd
        def even_before_odd(a, b):
            return (a % 2 == 0) and (b % 2 == 1)
        
        reversed_comp = Helpers.reverse(even_before_odd)
        # Should reverse the logic
        self.assert_equal(reversed_comp(2, 3), False)  # even_before_odd(2, 3) is True, so reverse is False
        self.assert_equal(reversed_comp(3, 2), True)   # even_before_odd(3, 2) is False, so reverse is True


if __name__ == '__main__':
    TestHelpers.run_and_output_results()
