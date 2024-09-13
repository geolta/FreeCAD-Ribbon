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
Utility functions and classes for the *Darwin* backend.
"""

# pylint: disable=C0103
# pylint: disable=R0903
# This module contains wrapper classes

import contextlib
import ctypes
import ctypes.util
import six

import objc
import HIServices

<<<<<<< HEAD
from CoreFoundation import (
    CFRelease
)
=======
from CoreFoundation import CFRelease
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

from Quartz import (
    CFMachPortCreateRunLoopSource,
    CFRunLoopAddSource,
    CFRunLoopGetCurrent,
    CFRunLoopRunInMode,
    CFRunLoopStop,
    CGEventTapCreate,
    CGEventTapEnable,
    kCFRunLoopDefaultMode,
    kCFRunLoopRunTimedOut,
    kCGEventTapOptionDefault,
    kCGEventTapOptionListenOnly,
    kCGHeadInsertEventTap,
<<<<<<< HEAD
    kCGSessionEventTap)
=======
    kCGSessionEventTap,
)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa


from . import AbstractListener


def _wrap_value(value):
    """Converts a pointer to a *Python objc* value.

    :param value: The pointer to convert.

    :return: a wrapped value
    """
    return objc.objc_object(c_void_p=value) if value is not None else None


@contextlib.contextmanager
def _wrapped(value):
    """A context manager that converts a raw pointer to a *Python objc* value.

    When the block is exited, the value is released.

    :param value: The raw value to wrap.
    """
    wrapped_value = _wrap_value(value)

    try:
        yield value
    finally:
        CFRelease(wrapped_value)


class CarbonExtra(object):
    """A class exposing some missing functionality from *Carbon* as class
    attributes.
    """
<<<<<<< HEAD
    _Carbon = ctypes.cdll.LoadLibrary(ctypes.util.find_library('Carbon'))
=======

    _Carbon = ctypes.cdll.LoadLibrary(ctypes.util.find_library("Carbon"))
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

    _Carbon.TISCopyCurrentKeyboardInputSource.argtypes = []
    _Carbon.TISCopyCurrentKeyboardInputSource.restype = ctypes.c_void_p

    _Carbon.TISCopyCurrentASCIICapableKeyboardLayoutInputSource.argtypes = []
<<<<<<< HEAD
    _Carbon.TISCopyCurrentASCIICapableKeyboardLayoutInputSource.restype = \
        ctypes.c_void_p

    _Carbon.TISGetInputSourceProperty.argtypes = [
        ctypes.c_void_p, ctypes.c_void_p]
=======
    _Carbon.TISCopyCurrentASCIICapableKeyboardLayoutInputSource.restype = (
        ctypes.c_void_p
    )

    _Carbon.TISGetInputSourceProperty.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
    _Carbon.TISGetInputSourceProperty.restype = ctypes.c_void_p

    _Carbon.LMGetKbdType.argtypes = []
    _Carbon.LMGetKbdType.restype = ctypes.c_uint32

    _Carbon.UCKeyTranslate.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint16,
        ctypes.c_uint16,
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_uint32),
        ctypes.c_uint8,
        ctypes.POINTER(ctypes.c_uint8),
<<<<<<< HEAD
        ctypes.c_uint16 * 4]
    _Carbon.UCKeyTranslate.restype = ctypes.c_uint32

    TISCopyCurrentKeyboardInputSource = \
        _Carbon.TISCopyCurrentKeyboardInputSource

    TISCopyCurrentASCIICapableKeyboardLayoutInputSource = \
        _Carbon.TISCopyCurrentASCIICapableKeyboardLayoutInputSource

    kTISPropertyUnicodeKeyLayoutData = ctypes.c_void_p.in_dll(
        _Carbon, 'kTISPropertyUnicodeKeyLayoutData')

    TISGetInputSourceProperty = \
        _Carbon.TISGetInputSourceProperty

    LMGetKbdType = \
        _Carbon.LMGetKbdType
=======
        ctypes.c_uint16 * 4,
    ]
    _Carbon.UCKeyTranslate.restype = ctypes.c_uint32

    TISCopyCurrentKeyboardInputSource = _Carbon.TISCopyCurrentKeyboardInputSource

    TISCopyCurrentASCIICapableKeyboardLayoutInputSource = (
        _Carbon.TISCopyCurrentASCIICapableKeyboardLayoutInputSource
    )

    kTISPropertyUnicodeKeyLayoutData = ctypes.c_void_p.in_dll(
        _Carbon, "kTISPropertyUnicodeKeyLayoutData"
    )

    TISGetInputSourceProperty = _Carbon.TISGetInputSourceProperty

    LMGetKbdType = _Carbon.LMGetKbdType
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

    kUCKeyActionDisplay = 3
    kUCKeyTranslateNoDeadKeysBit = 0

<<<<<<< HEAD
    UCKeyTranslate = \
        _Carbon.UCKeyTranslate
=======
    UCKeyTranslate = _Carbon.UCKeyTranslate
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa


@contextlib.contextmanager
def keycode_context():
    """Returns an opaque value representing a context for translating keycodes
    to strings.
    """
    keyboard_type, layout_data = None, None
    for source in [
<<<<<<< HEAD
            CarbonExtra.TISCopyCurrentKeyboardInputSource,
            CarbonExtra.TISCopyCurrentASCIICapableKeyboardLayoutInputSource]:
        with _wrapped(source()) as keyboard:
            keyboard_type = CarbonExtra.LMGetKbdType()
            layout = _wrap_value(CarbonExtra.TISGetInputSourceProperty(
                keyboard,
                CarbonExtra.kTISPropertyUnicodeKeyLayoutData))
=======
        CarbonExtra.TISCopyCurrentKeyboardInputSource,
        CarbonExtra.TISCopyCurrentASCIICapableKeyboardLayoutInputSource,
    ]:
        with _wrapped(source()) as keyboard:
            keyboard_type = CarbonExtra.LMGetKbdType()
            layout = _wrap_value(
                CarbonExtra.TISGetInputSourceProperty(
                    keyboard, CarbonExtra.kTISPropertyUnicodeKeyLayoutData
                )
            )
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
            layout_data = layout.bytes().tobytes() if layout else None
            if keyboard is not None and layout_data is not None:
                break
    yield (keyboard_type, layout_data)


def keycode_to_string(context, keycode, modifier_state=0):
<<<<<<< HEAD
    """Converts a keycode to a string.
    """
=======
    """Converts a keycode to a string."""
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
    LENGTH = 4

    keyboard_type, layout_data = context

    dead_key_state = ctypes.c_uint32()
    length = ctypes.c_uint8()
    unicode_string = (ctypes.c_uint16 * LENGTH)()
    CarbonExtra.UCKeyTranslate(
        layout_data,
        keycode,
        CarbonExtra.kUCKeyActionDisplay,
        modifier_state,
        keyboard_type,
        CarbonExtra.kUCKeyTranslateNoDeadKeysBit,
        ctypes.byref(dead_key_state),
        LENGTH,
        ctypes.byref(length),
<<<<<<< HEAD
        unicode_string)
    return u''.join(
        six.unichr(unicode_string[i])
        for i in range(length.value))
=======
        unicode_string,
    )
    return "".join(six.unichr(unicode_string[i]) for i in range(length.value))
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa


def get_unicode_to_keycode_map():
    """Returns a mapping from unicode strings to virtual key codes.

    :return: a dict mapping key codes to strings
    """
    with keycode_context() as context:
<<<<<<< HEAD
        return {
            keycode_to_string(context, keycode): keycode
            for keycode in range(128)}
=======
        return {keycode_to_string(context, keycode): keycode for keycode in range(128)}
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa


class ListenerMixin(object):
    """A mixin for *Quartz* event listeners.

    Subclasses should set a value for :attr:`_EVENTS` and implement
    :meth:`_handle`.
    """
<<<<<<< HEAD
=======

>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
    #: The events that we listen to
    _EVENTS = tuple()

    #: Whether this process is trusted to monitor input events.
    IS_TRUSTED = False

    def _run(self):
        self.IS_TRUSTED = HIServices.AXIsProcessTrusted()
        if not self.IS_TRUSTED:
            self._log.warning(
<<<<<<< HEAD
                'This process is not trusted! Input event monitoring will not '
                'be possible until it is added to accessibility clients.')
=======
                "This process is not trusted! Input event monitoring will not "
                "be possible until it is added to accessibility clients."
            )
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

        self._loop = None
        try:
            tap = self._create_event_tap()
            if tap is None:
                self._mark_ready()
                return

<<<<<<< HEAD
            loop_source = CFMachPortCreateRunLoopSource(
                None, tap, 0)
            self._loop = CFRunLoopGetCurrent()

            CFRunLoopAddSource(
                self._loop, loop_source, kCFRunLoopDefaultMode)
=======
            loop_source = CFMachPortCreateRunLoopSource(None, tap, 0)
            self._loop = CFRunLoopGetCurrent()

            CFRunLoopAddSource(self._loop, loop_source, kCFRunLoopDefaultMode)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
            CGEventTapEnable(tap, True)

            self._mark_ready()

            # pylint: disable=W0702; we want to silence errors
            try:
                while self.running:
<<<<<<< HEAD
                    result = CFRunLoopRunInMode(
                        kCFRunLoopDefaultMode, 1, False)
=======
                    result = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1, False)
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa
                    try:
                        if result != kCFRunLoopRunTimedOut:
                            break
                    except AttributeError:
                        # This happens during teardown of the virtual machine
                        break

            except:
                # This exception will have been passed to the main thread
                pass
            # pylint: enable=W0702

        finally:
            self._loop = None

    def _stop_platform(self):
        # The base class sets the running flag to False; this will cause the
        # loop around run loop invocations to terminate and set this event
        try:
            if self._loop is not None:
                CFRunLoopStop(self._loop)
        except AttributeError:
            # The loop may not have been created
            pass

    def _create_event_tap(self):
        """Creates the event tap used by the listener.

        :return: an event tap
        """
        return CGEventTapCreate(
            kCGSessionEventTap,
            kCGHeadInsertEventTap,
<<<<<<< HEAD
            kCGEventTapOptionListenOnly if (
                True
                and not self.suppress
                and self._intercept is None)
            else kCGEventTapOptionDefault,
            self._EVENTS,
            self._handler,
            None)
=======
            (
                kCGEventTapOptionListenOnly
                if (True and not self.suppress and self._intercept is None)
                else kCGEventTapOptionDefault
            ),
            self._EVENTS,
            self._handler,
            None,
        )
>>>>>>> 28955392c454aa05a9bf6f258b946901e0139cfa

    @AbstractListener._emitter
    def _handler(self, proxy, event_type, event, refcon):
        """The callback registered with *macOS* for mouse events.

        This method will call the callbacks registered on initialisation.
        """
        self._handle(proxy, event_type, event, refcon)
        if self._intercept is not None:
            return self._intercept(event_type, event)
        elif self.suppress:
            return None

    def _handle(self, proxy, event_type, event, refcon):
        """The device specific callback handler.

        This method calls the appropriate callback registered when this
        listener was created based on the event.
        """
        raise NotImplementedError()
