#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Class MyInt drived from int."""
    def __eq__(self, val):
        """Overrides == to !=."""
        return self.real != val

    def __ne__(self, val):
        """Overrides != to ==."""
        return self.real == val
