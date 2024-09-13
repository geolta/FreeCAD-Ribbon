# coding=utf-8
# pynput
# Copyright (C) 2015-2024 Moses Palmér
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
The keyboard implementation for *macOS*.
"""

# pylint: disable=C0111
# The documentation is extracted from the base classes

# pylint: disable=R0903
# We implement stubs

import enum

from Quartz import (
    CGEventCreateKeyboardEvent,
    CGEventGetFlags,
    CGEventGetIntegerValueField,
    CGEventGetType,
    CGEventKeyboardGetUnicodeString,
    CGEventKeyboardSetUnicodeString,
    CGEventMaskBit,
    CGEventPost,
    CGEventSetFlags,
    kCGEventFlagMaskAlternate,
    kCGEventFlagMaskCommand,
    kCGEventFlagMaskControl,
    kCGEventFlagMaskShift,
    kCGEventFlagsChanged,
    kCGEventKeyDown,
    kCGEventKeyUp,
    kCGHIDEventTap,
    kCGKeyboardEventKeycode,
    NSEvent,
<<<<<<< HEAD
    NSSystemDefined)
=======
    NSSystemDefined,
)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

from pynput._util.darwin import (
    get_unicode_to_keycode_map,
    keycode_context,
<<<<<<< HEAD
    ListenerMixin)
=======
    ListenerMixin,
)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
from pynput._util.darwin_vks import SYMBOLS
from . import _base


# From hidsystem/ev_keymap.h
NX_KEYTYPE_PLAY = 16
NX_KEYTYPE_MUTE = 7
NX_KEYTYPE_SOUND_DOWN = 1
NX_KEYTYPE_SOUND_UP = 0
NX_KEYTYPE_NEXT = 17
NX_KEYTYPE_PREVIOUS = 18

# pylint: disable=C0103; We want to use the names from the C API
# This is undocumented, but still widely known
kSystemDefinedEventMediaKeysSubtype = 8

# We extract this here since the name is very long
otherEventWithType = getattr(
<<<<<<< HEAD
        NSEvent,
        'otherEventWithType_'
        'location_'
        'modifierFlags_'
        'timestamp_'
        'windowNumber_'
        'context_'
        'subtype_'
        'data1_'
        'data2_')
=======
    NSEvent,
    "otherEventWithType_"
    "location_"
    "modifierFlags_"
    "timestamp_"
    "windowNumber_"
    "context_"
    "subtype_"
    "data1_"
    "data2_",
)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
# pylint: enable=C0103


class KeyCode(_base.KeyCode):
    _PLATFORM_EXTENSIONS = (
        # Whether this is a media key
<<<<<<< HEAD
        '_is_media',
=======
        "_is_media",
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
    )

    # Be explicit about fields
    _is_media = None

    @classmethod
    def _from_media(cls, vk, **kwargs):
        """Creates a media key from a key code.

        :param int vk: The key code.

        :return: a key code
        """
        return cls.from_vk(vk, _is_media=True, **kwargs)

    def _event(self, modifiers, mapping, is_pressed):
        """This key as a *Quartz* event.

        :param set modifiers: The currently active modifiers.

        :param mapping: The current keyboard mapping.

        :param bool is_press: Whether to generate a press event.

        :return: a *Quartz* event
        """
        vk = self.vk or mapping.get(self.char)
        if self._is_media:
            result = otherEventWithType(
                NSSystemDefined,
                (0, 0),
<<<<<<< HEAD
                0xa00 if is_pressed else 0xb00,
=======
                0xA00 if is_pressed else 0xB00,
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
                0,
                0,
                0,
                8,
<<<<<<< HEAD
                (self.vk << 16) | ((0xa if is_pressed else 0xb) << 8),
                -1).CGEvent()
        else:
            result = CGEventCreateKeyboardEvent(
                None, 0 if vk is None else vk, is_pressed)
=======
                (self.vk << 16) | ((0xA if is_pressed else 0xB) << 8),
                -1,
            ).CGEvent()
        else:
            result = CGEventCreateKeyboardEvent(
                None, 0 if vk is None else vk, is_pressed
            )
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

        CGEventSetFlags(
            result,
            0
<<<<<<< HEAD
            | (kCGEventFlagMaskAlternate
               if Key.alt in modifiers else 0)

            | (kCGEventFlagMaskCommand
               if Key.cmd in modifiers else 0)

            | (kCGEventFlagMaskControl
               if Key.ctrl in modifiers else 0)

            | (kCGEventFlagMaskShift
               if Key.shift in modifiers else 0))

        if vk is None and self.char is not None:
            CGEventKeyboardSetUnicodeString(
                result, len(self.char), self.char)
=======
            | (kCGEventFlagMaskAlternate if Key.alt in modifiers else 0)
            | (kCGEventFlagMaskCommand if Key.cmd in modifiers else 0)
            | (kCGEventFlagMaskControl if Key.ctrl in modifiers else 0)
            | (kCGEventFlagMaskShift if Key.shift in modifiers else 0),
        )

        if vk is None and self.char is not None:
            CGEventKeyboardSetUnicodeString(result, len(self.char), self.char)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

        return result


# pylint: disable=W0212
class Key(enum.Enum):
    # Default keys
    alt = KeyCode.from_vk(0x3A)
    alt_l = KeyCode.from_vk(0x3A)
    alt_r = KeyCode.from_vk(0x3D)
    alt_gr = KeyCode.from_vk(0x3D)
    backspace = KeyCode.from_vk(0x33)
    caps_lock = KeyCode.from_vk(0x39)
    cmd = KeyCode.from_vk(0x37)
    cmd_l = KeyCode.from_vk(0x37)
    cmd_r = KeyCode.from_vk(0x36)
    ctrl = KeyCode.from_vk(0x3B)
    ctrl_l = KeyCode.from_vk(0x3B)
    ctrl_r = KeyCode.from_vk(0x3E)
    delete = KeyCode.from_vk(0x75)
    down = KeyCode.from_vk(0x7D)
    end = KeyCode.from_vk(0x77)
    enter = KeyCode.from_vk(0x24)
    esc = KeyCode.from_vk(0x35)
    f1 = KeyCode.from_vk(0x7A)
    f2 = KeyCode.from_vk(0x78)
    f3 = KeyCode.from_vk(0x63)
    f4 = KeyCode.from_vk(0x76)
    f5 = KeyCode.from_vk(0x60)
    f6 = KeyCode.from_vk(0x61)
    f7 = KeyCode.from_vk(0x62)
    f8 = KeyCode.from_vk(0x64)
    f9 = KeyCode.from_vk(0x65)
    f10 = KeyCode.from_vk(0x6D)
    f11 = KeyCode.from_vk(0x67)
    f12 = KeyCode.from_vk(0x6F)
    f13 = KeyCode.from_vk(0x69)
    f14 = KeyCode.from_vk(0x6B)
    f15 = KeyCode.from_vk(0x71)
    f16 = KeyCode.from_vk(0x6A)
    f17 = KeyCode.from_vk(0x40)
    f18 = KeyCode.from_vk(0x4F)
    f19 = KeyCode.from_vk(0x50)
    f20 = KeyCode.from_vk(0x5A)
    home = KeyCode.from_vk(0x73)
    left = KeyCode.from_vk(0x7B)
    page_down = KeyCode.from_vk(0x79)
    page_up = KeyCode.from_vk(0x74)
    right = KeyCode.from_vk(0x7C)
    shift = KeyCode.from_vk(0x38)
    shift_l = KeyCode.from_vk(0x38)
    shift_r = KeyCode.from_vk(0x3C)
<<<<<<< HEAD
    space = KeyCode.from_vk(0x31, char=' ')
=======
    space = KeyCode.from_vk(0x31, char=" ")
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
    tab = KeyCode.from_vk(0x30)
    up = KeyCode.from_vk(0x7E)

    media_play_pause = KeyCode._from_media(NX_KEYTYPE_PLAY)
    media_volume_mute = KeyCode._from_media(NX_KEYTYPE_MUTE)
    media_volume_down = KeyCode._from_media(NX_KEYTYPE_SOUND_DOWN)
    media_volume_up = KeyCode._from_media(NX_KEYTYPE_SOUND_UP)
    media_previous = KeyCode._from_media(NX_KEYTYPE_PREVIOUS)
    media_next = KeyCode._from_media(NX_KEYTYPE_NEXT)
<<<<<<< HEAD
=======


>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
# pylint: enable=W0212


class Controller(_base.Controller):
    _KeyCode = KeyCode
    _Key = Key

    def __init__(self):
        super(Controller, self).__init__()
        self._mapping = get_unicode_to_keycode_map()

    def _handle(self, key, is_press):
        with self.modifiers as modifiers:
            CGEventPost(
                kCGHIDEventTap,
                (key if key not in (k for k in Key) else key.value)._event(
<<<<<<< HEAD
                    modifiers, self._mapping, is_press))
=======
                    modifiers, self._mapping, is_press
                ),
            )
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa


class Listener(ListenerMixin, _base.Listener):
    #: The events that we listen to
    _EVENTS = (
<<<<<<< HEAD
        CGEventMaskBit(kCGEventKeyDown) |
        CGEventMaskBit(kCGEventKeyUp) |
        CGEventMaskBit(kCGEventFlagsChanged) |
        CGEventMaskBit(NSSystemDefined)
=======
        CGEventMaskBit(kCGEventKeyDown)
        | CGEventMaskBit(kCGEventKeyUp)
        | CGEventMaskBit(kCGEventFlagsChanged)
        | CGEventMaskBit(NSSystemDefined)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
    )

    # pylint: disable=W0212
    #: A mapping from keysym to special key
<<<<<<< HEAD
    _SPECIAL_KEYS = {
        (key.value.vk, key.value._is_media): key
        for key in Key}
=======
    _SPECIAL_KEYS = {(key.value.vk, key.value._is_media): key for key in Key}
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
    # pylint: enable=W0212

    #: The event flags set for the various modifier keys
    _MODIFIER_FLAGS = {
        Key.alt: kCGEventFlagMaskAlternate,
        Key.alt_l: kCGEventFlagMaskAlternate,
        Key.alt_r: kCGEventFlagMaskAlternate,
        Key.cmd: kCGEventFlagMaskCommand,
        Key.cmd_l: kCGEventFlagMaskCommand,
        Key.cmd_r: kCGEventFlagMaskCommand,
        Key.ctrl: kCGEventFlagMaskControl,
        Key.ctrl_l: kCGEventFlagMaskControl,
        Key.ctrl_r: kCGEventFlagMaskControl,
        Key.shift: kCGEventFlagMaskShift,
        Key.shift_l: kCGEventFlagMaskShift,
<<<<<<< HEAD
        Key.shift_r: kCGEventFlagMaskShift}
=======
        Key.shift_r: kCGEventFlagMaskShift,
    }
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

    def __init__(self, *args, **kwargs):
        super(Listener, self).__init__(*args, **kwargs)
        self._flags = 0
        self._context = None
<<<<<<< HEAD
        self._intercept = self._options.get(
            'intercept',
            None)
=======
        self._intercept = self._options.get("intercept", None)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

    def _run(self):
        with keycode_context() as context:
            self._context = context
            try:
                super(Listener, self)._run()
            finally:
                self._context = None

    def _handle(self, _proxy, event_type, event, _refcon):
        # Convert the event to a KeyCode; this may fail, and in that case we
        # pass None
        try:
            key = self._event_to_key(event)
        except IndexError:
            key = None

        try:
            if event_type == kCGEventKeyDown:
                # This is a normal key press
                self.on_press(key)

            elif event_type == kCGEventKeyUp:
                # This is a normal key release
                self.on_release(key)

            elif key == Key.caps_lock:
                # We only get an event when caps lock is toggled, so we fake
                # press and release
                self.on_press(key)
                self.on_release(key)

            elif event_type == NSSystemDefined:
                sys_event = NSEvent.eventWithCGEvent_(event)
                if sys_event.subtype() == kSystemDefinedEventMediaKeysSubtype:
                    # The key in the special key dict; True since it is a media
                    # key
<<<<<<< HEAD
                    key = ((sys_event.data1() & 0xffff0000) >> 16, True)
                    if key in self._SPECIAL_KEYS:
                        flags = sys_event.data1() & 0x0000ffff
                        is_press = ((flags & 0xff00) >> 8) == 0x0a
=======
                    key = ((sys_event.data1() & 0xFFFF0000) >> 16, True)
                    if key in self._SPECIAL_KEYS:
                        flags = sys_event.data1() & 0x0000FFFF
                        is_press = ((flags & 0xFF00) >> 8) == 0x0A
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
                        if is_press:
                            self.on_press(self._SPECIAL_KEYS[key])
                        else:
                            self.on_release(self._SPECIAL_KEYS[key])

            else:
                # This is a modifier event---excluding caps lock---for which we
                # must check the current modifier state to determine whether
                # the key was pressed or released
                flags = CGEventGetFlags(event)
                is_press = flags & self._MODIFIER_FLAGS.get(key, 0)
                if is_press:
                    self.on_press(key)
                else:
                    self.on_release(key)

        finally:
            # Store the current flag mask to be able to detect modifier state
            # changes
            self._flags = CGEventGetFlags(event)

    def _event_to_key(self, event):
        """Converts a *Quartz* event to a :class:`KeyCode`.

        :param event: The event to convert.

        :return: a :class:`pynput.keyboard.KeyCode`

        :raises IndexError: if the key code is invalid
        """
<<<<<<< HEAD
        vk = CGEventGetIntegerValueField(
            event, kCGKeyboardEventKeycode)
=======
        vk = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
        event_type = CGEventGetType(event)
        is_media = True if event_type == NSSystemDefined else None

        # First try special keys...
        key = (vk, is_media)
        if key in self._SPECIAL_KEYS:
            return self._SPECIAL_KEYS[key]

        # ...then try characters...
<<<<<<< HEAD
        length, chars = CGEventKeyboardGetUnicodeString(
            event, 100, None, None)
=======
        length, chars = CGEventKeyboardGetUnicodeString(event, 100, None, None)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
        try:
            printable = chars.isprintable()
        except AttributeError:
            printable = chars.isalnum()
<<<<<<< HEAD
        if not printable and vk in SYMBOLS \
                and CGEventGetFlags(event) \
                & kCGEventFlagMaskControl:
=======
        if (
            not printable
            and vk in SYMBOLS
            and CGEventGetFlags(event) & kCGEventFlagMaskControl
        ):
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
            return KeyCode.from_char(SYMBOLS[vk], vk=vk)
        elif length > 0:
            return KeyCode.from_char(chars, vk=vk)

        # ...and fall back on a virtual key code
        return KeyCode.from_vk(vk)
