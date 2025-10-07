"""
Tests for the main module.
"""

import pytest
from src.main import hello_world, add_numbers


class TestHelloWorld:
    """Test cases for hello_world function."""

    def test_hello_world_default(self):
        """Test hello_world with default parameter."""
        result = hello_world()
        assert result == "Hello, World!"

    def test_hello_world_custom_name(self):
        """Test hello_world with custom name."""
        result = hello_world("Alice")
        assert result == "Hello, Alice!"

    def test_hello_world_empty_string(self):
        """Test hello_world with empty string."""
        result = hello_world("")
        assert result == "Hello, !"


class TestAddNumbers:
    """Test cases for add_numbers function."""

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        result = add_numbers(2, 3)
        assert result == 5

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = add_numbers(-2, -3)
        assert result == -5

    def test_add_zero(self):
        """Test adding with zero."""
        result = add_numbers(5, 0)
        assert result == 5

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        result = add_numbers(10, -3)
        assert result == 7


@pytest.mark.slow
def test_performance_example():
    """Example of a slow test that can be skipped."""
    # This would be a performance test
    result = sum(range(1000000))
    assert result > 0
