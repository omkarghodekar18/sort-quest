from typing import Any, Callable

class Helpers:
    """
    A collection of static comparator helper functions.
    Each comparator returns True if the first element should come before the second.
    """

    # --- Numeric Comparators ---
    @staticmethod
    def number_asc(a: int | float, b: int | float) -> bool:
        """Ascending order for numbers (int, float, or numeric strings)."""
        return float(a) < float(b)

    @staticmethod
    def number_desc(a: int | float, b: int | float) -> bool:
        """Descending order for numbers (int, float, or numeric strings)."""
        return float(a) > float(b)

    # --- Alphabetical Comparators ---
    @staticmethod
    def alpha_asc(a: str, b: str) -> bool:
        """Alphabetical (A → Z), case-insensitive."""
        return str(a).lower() < str(b).lower()

    @staticmethod
    def alpha_desc(a: str, b: str) -> bool:
        """Reverse alphabetical (Z → A), case-insensitive."""
        return str(a).lower() > str(b).lower()

    # --- Length-based Comparators ---
    @staticmethod
    def length_asc(a: str, b: str) -> bool:
        """Shorter → longer (based on string length)."""
        return len(str(a)) < len(str(b))

    @staticmethod
    def length_desc(a: str, b: str) -> bool:
        """Longer → shorter (based on string length)."""
        return len(str(a)) > len(str(b))

    # --- Reverse Wrapper ---
    @staticmethod
    def reverse(comparator: Callable[[Any, Any], bool]) -> Callable[[Any, Any], bool]:
        """Reverses the logic of any comparator."""
        return lambda a, b: not comparator(a, b)

