"""Demonstrate PEP 8 layout

This module does nothing useful, aside from demonstrating most of the
layout rules of PEP 8.

"""

import sys
import re
from pickle import loads, dumps

class Elephant:
    """Tracks elephants and their optional associated dormice.

    """
    def __init__(self, dormouse = None):
        """Create an Elephant, and optionally tie it to a DorMouse.

        If specified, the dormouse parameter should be a DorMouse
        instance which should be associated with this Elephant.

        """
        self.dormouse = dormouse

        if dormouse:
            dormouse.set_elephant(self)


class DorMouse:
    """Tracks dormice, optionally associated with elephants.

    Each DorMouse instance has the ability to associate with 0 or 1
    Elephant instances. Use the set_elephant method to establish that
    association.

    """
    def __init__(self):
        """Initialize the DorMouse, setting the Elephant to None."""
        self.elephant = None

    def set_elephant(self, elephant):
        """Associate an Elephant with this DorMouse.

        The elephant parameter must be an Elephant instance, or None.
        Setting the elephant to None breaks the association between
        this DorMouse and its Elephant.

        """
        if self.elephant:
            self.elephant.dormouse = None
        self.elephant = elephant


# The ScarePair function creates a ScarePair object, which is actually
# just a tuple containing a linked Elephant and DorMouse pair.
def ScarePair():
    """Create a ScarePair object linking an Elephant and a DorMouse.

    Both the Elephant and the DorMouse instances of the pair are newly
    created. They are fully associated before the pair is returned.

    """
    dormouse = DorMouse()
    elephant = Elephant(dormouse)

    return elephant, dormouse


def munge(left, right):
    """Make a horrible mess.

    This function takes a pair of ScarePair objects and twists them up
    into a pretzel.

    """
    left[1].set_elephant(right[0])
    right[1].set_elephant(left[0])

    new_left = (left[0], right[1])
    new_right = (right[0], left[1])

    return lew_left, new_right
