#simulates a keypress to bounce the cube on Mac
from Quartz.CoreGraphics import CGEventCreateKeyboardEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGHIDEventTap
import time

def bounce():
    CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x7E, True))
    time.sleep(0.05)
    CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x7E, False))

def restart():
    CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x31, True))
    time.sleep(0.05)
    CGEventPost(kCGHIDEventTap, CGEventCreateKeyboardEvent(None, 0x31, False))
