import array
import ctypes

from freetyping.winapi import (
    INPUT,
    INPUT_KEYBOARD,
    KEYBDINPUT,
    KEYEVENTF_KEYUP,
    KEYEVENTF_UNICODE,
    VK_RETURN,
    SendInput,
)


def send_line(text: str) -> None:
    """Send a single line of text.

    Args:
        text: The line content to type (line breaks should not included).

    Raises:
        OSError: Raise OSError when fewer input events were sent than expected.
    """
    inputs = []

    chars = array.array("H", text.encode("utf-16-le"))
    for char in chars:
        key_down = INPUT()
        key_down.type = INPUT_KEYBOARD
        key_down.union.ki = KEYBDINPUT(
            wVk=0,
            wScan=char,
            dwFlags=KEYEVENTF_UNICODE,
            time=0,
            dwExtraInfo=0,
        )
        inputs.append(key_down)

        key_up = INPUT()
        key_up.type = INPUT_KEYBOARD
        key_up.union.ki = KEYBDINPUT(
            wVk=0,
            wScan=char,
            dwFlags=KEYEVENTF_UNICODE | KEYEVENTF_KEYUP,
            time=0,
            dwExtraInfo=0,
        )
        inputs.append(key_up)

    n = SendInput(len(inputs), (INPUT * len(inputs))(*inputs), ctypes.sizeof(INPUT))
    if n != len(inputs):
        raise OSError(ctypes.get_last_error())


def press_enter() -> None:
    """Send an Enter key stroke.

    Raises:
        OSError: Raise OSError when fewer input events were sent than expected.
    """
    inputs = []

    enter_down = INPUT()
    enter_down.type = INPUT_KEYBOARD
    enter_down.union.ki = KEYBDINPUT(
        wVk=VK_RETURN,
        wScan=0,
        dwFlags=0,
        time=0,
        dwExtraInfo=0,
    )
    inputs.append(enter_down)

    enter_up = INPUT()
    enter_up.type = INPUT_KEYBOARD
    enter_up.union.ki = KEYBDINPUT(
        wVk=VK_RETURN,
        wScan=0,
        dwFlags=KEYEVENTF_KEYUP,
        time=0,
        dwExtraInfo=0,
    )
    inputs.append(enter_up)

    n = SendInput(len(inputs), (INPUT * len(inputs))(*inputs), ctypes.sizeof(INPUT))
    if n != len(inputs):
        raise OSError(ctypes.get_last_error())


def send_text(text: str) -> None:
    """Simulate keyboard input for any characters, supporting non-ASCII characters and multi-line text.

    Args:
        text: The text to type.

    Raises:
        OSError: Raise OSError when fewer input events were sent than expected.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        send_line(line)
        if i != len(lines) - 1:
            press_enter()
