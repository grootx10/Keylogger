
# Python Keylogger

A simple keylogger written in Python for educational purposes to demonstrate how keypress events can be captured on a local system. This project is intended to help users understand how keyboard input is handled programmatically and is not designed for malicious purposes.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)
- [Disclaimer](#disclaimer)

---

## Overview

This Python-based keylogger captures and logs keystrokes on a local machine. It demonstrates the basic principles of handling keyboard input in Python using various libraries. The project includes:

- Keystroke logging functionality
- Logging to a local file
- Lightweight and minimal dependencies

**Note**: This project is intended for educational purposes only. Please ensure you have proper authorization before using this code on any system.

---

## Features

- **Captures keystrokes**: Records keypress events on the local machine.
- **Log output**: Saves keystrokes in a local text file for later review.
- **Cross-platform**: Works on Windows, macOS, and Linux systems.
- **Low-level logging**: Uses Python libraries to directly interface with the keyboard and capture input events.

---

## Installation

To install and run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/python-keylogger.git
   cd python-keylogger
   ```

2. **Install dependencies**:

   This project requires the `pynput` library to capture keyboard input. Install it via `pip`:

   ```bash
   pip install pynput
   ```

---

## Usage

1. **Run the keylogger script**:

   To start the keylogger, simply run the `keylogger.py` script:

   ```bash
   python keylogger.py
   ```

2. **Keystroke Logging**:

   The script will run in the background and log any keystrokes into a file named `keylog.txt`. You can open this file to view the captured keystrokes.

3. **Stopping the keylogger**:

   To stop the keylogger, you can interrupt the script by pressing `Ctrl + C` in the terminal or by terminating the process in your task manager.

---

## How It Works

The keylogger uses the `pynput` library to listen for keyboard events. Here's a brief breakdown of how it functions:

1. **Event Listener**: The `pynput.keyboard.Listener` listens for keypress events.
2. **Logging**: When a key is pressed, it is logged into a local text file (default: `keylog.txt`).
3. **Background Operation**: The keylogger runs in the background and operates until manually stopped by the user.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

This code is intended for **educational purposes only**. Use it responsibly and always obtain consent before running software that records user input. Unauthorized use of keyloggers is illegal and unethical. The creator of this software is not responsible for any misuse of the code.

- **Do not use this code for malicious purposes**.
- **Do not deploy this code on any machine without the explicit consent of the owner**.

Please make sure to comply with all relevant laws and ethical standards.

---

If you have any questions or suggestions, feel free to open an issue or pull request.
