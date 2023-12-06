#
# This file is part of Dragonfly.
# (c) Copyright 2023 by Joshua Webb
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

"""
Win32 input wrapper functions.

This file implements an interface to the Win32 GetAsyncKeyState function
for observing keyboard and mouse events.
"""

import sys
from ctypes import (c_short, c_ushort, c_long, c_int, windll, wintypes)


class KeyStateGetter:
    def __init__(self, virtual_key_code=None, toggle_mode=0):
        if virtual_key_code is None:
            self._vkey = None
            self._toggle_mode = toggle_mode
            self._last_state = True
            self._current_toggle = False
        else:
            self._vkey = virtual_key_code
            self._toggle_mode = toggle_mode
            self._last_state = False
            self._current_toggle = False

    def get(self):
        if self._vkey is None:
            return True
        key_state = self._get_async_key_state()
        is_pressed = (key_state >> 15) == 1
        # press and hold
        if self._toggle_mode <= 0:
            self._last_state = is_pressed
            return is_pressed
        # toggle
        else:
            if is_pressed and not self._last_state:
                self._current_toggle = not self._current_toggle
            self._last_state = is_pressed
            return self._current_toggle

    def reset(self):
        self._last_state = False
        self._current_toggle = False

    def _get_async_key_state(self):
        gaks = windll.user32.GetAsyncKeyState
        gaks.argtypes = [c_int]
        gaks.restype = wintypes.USHORT # should actually be SHORT, but use USHORT for printing
        key_state = gaks(self._vkey)
        return key_state
