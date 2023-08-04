# Discord Bot for Pattern-Based Interaction

## Description

This Python project is a Discord bot designed to interact with the Discord application by locating and clicking on specific patterns within the Discord window. The bot utilizes the `pyautogui`, `opencv-python`, and `numpy` libraries for window management, pattern matching, and image processing, respectively.

## Features

- **Pattern Search**: The bot searches for a specific pattern (image) within the Discord window using OpenCV's pattern matching technique. The pattern is represented by the image in `img.png`.
- **Interaction**: Once the pattern is found, the bot clicks on the specified positions on the Discord window to interact with certain elements or buttons.

## Requirements

- Python 3.x
- `pyautogui` library (`pyautogui`)
- OpenCV library (`opencv-python`)
- `numpy` library (`numpy`)

**Note**: The application is designed to work on Windows, macOS, and Linux.

## Usage

1. Save the image of the pattern you want to search for as `img.png` in the same directory as the script.
2. Install the required libraries by running `pip install pyautogui opencv-python numpy` in the terminal.
3. Run the Python script `bot_click.py`.
4. When prompted, enter a recognizable part of the app title (e.g., "Discord") to identify the target application.
5. The bot will activate the Discord window, maximize it, and start searching for the pattern.
6. The bot will continuously search for the pattern in the Discord window and click on any occurrences found.

**Terminating the Application:**
To stop the bot and terminate the application gracefully, simply press `Ctrl+C` in the terminal or command prompt where the script is running.

**Note**: Ensure that Discord is running, and its window is visible on the screen before running the bot.

## Limitations

- The pattern matching technique relies on the quality and uniqueness of the pattern image for accurate results.
- The bot will continuously search and click on the pattern, which may result in multiple clicks if the pattern is present in various places. Please handle this behavior with caution to avoid unintended actions.

*Disclaimer: Automated interactions with applications, including Discord, may violate their Terms of Service. Use this bot responsibly and in compliance with the service's policies to avoid any adverse consequences.*

## License

This project is licensed under the [MIT License](LICENSE).
