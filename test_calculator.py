"""
Unit tests for the calc lib
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)


    def test_subtraction(self):
        assert 4 == calculator.sub(6, 2)
