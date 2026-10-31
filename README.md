# Free Typing

There are many real-world scenarios where users need to enter text into web pages or software interfaces that explicitly restrict pasting. Simulating keyboard input is one way to solve this problem. However, mature third-party Python libraries such as `PyAutoGUI` offer very limited support for Chinese characters or emojis. Common workarounds, such as using the `pyperclip` library or a Chinese IME, are not suitable in many situations.

Free Typing is a pure Python implementation that does not rely on any third-party libraries. It simulates keyboard input for any character by calling the Win32 API, with support for non-ASCII characters, emojis, and multi-line text.

## Installation

### Prerequisites

Before you begin, please make sure you have [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed. Additionally, we recommend installing [uv](https://docs.astral.sh/uv/getting-started/installation/) to make it easier to install and manage project dependencies.

### Installing the Package (Download a Precompiled `.whl` File)

#### Download the Latest Precompiled Wheel from GitHub

1. Open the project’s **GitHub Releases** page.
2. Go to **Latest release**.
3. Under **Assets** on the release page, download the file ending in `.whl`; the filename is typically similar to `freetyping-1.0.0-py3-none-any.whl`.

#### Install the wheel

Run the following command:

```bash
pip install freetyping-1.0.0-py3-none-any.whl
```

Or use uv:

```bash
uv add ./freetyping-1.0.0-py3-none-any.whl
uv sync
```

### Building from Source

Run the following commands:

```bash
git clone https://github.com/asss-whom/freetyping.git
cd freetyping
uv build
```

The build output should be located in the `dist` folder.

## How to use

```python
import freetyping
```

`freetyping` supports single-line text:

```python
freetyping.send_text("Hello, world!")
```

`freetyping` supports multi-line text:

```python
freetyping.send_text("Line 1\nLine 2\nLine 3")
```

`freetyping` supports non-ASCII text:

```python
freetyping.send_text("中文：你好！日本語：こんにちは！한국어：안녕하세요!")
```

`freetyping` supports Emoji text:

```python
freetyping.send_text("Emoji test: 😀🚀✨")
```
