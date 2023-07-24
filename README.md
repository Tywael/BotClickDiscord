# Discord Bot for Pattern-Based Interaction

![Project Logo](project_logo.png)

## Description

This Python project is a Discord bot designed to interact with the Discord application by locating and clicking on specific patterns within the Discord window. The bot utilizes the `pygetwindow`, `opencv-python`, and `pyautogui` libraries to achieve its functionality.

## Features

- **Discord Window Detection**: The bot can detect the Discord window and retrieve its position and size on the screen.
- **Pattern Search**: The bot searches for a specific pattern (image) within the Discord window using OpenCV's pattern matching technique. The pattern is represented by the image in `img.png`.
- **Interaction**: Once the pattern is found, the bot clicks on the specified positions on the Discord window to interact with certain elements or buttons.

## Requirements

- Python 3.x
- `pygetwindow` library (`pygetwindow`)
- OpenCV library (`opencv-python`)
- `pyautogui` library (`pyautogui`)

## Usage

1. Save the image of the pattern you want to search for as `img.png` in the same directory as the script.
2. Install the required libraries by running `pip install pygetwindow opencv-python pyautogui` in the terminal.
3. Run the Python script to activate the Discord window, maximize it, and start searching for the pattern.
4. The bot will continuously search for the pattern in the Discord window and click on any occurrences found.

**Note**: Ensure that Discord is running, and its window is visible on the screen before running the bot.

## Limitations

- The pattern matching technique relies on the quality and uniqueness of the pattern image for accurate results.
- The bot assumes that the Discord window is titled with " - Discord" to identify it. Ensure that the Discord window title matches this format for proper detection.
- The bot will continuously search and click on the pattern, which may result in multiple clicks if the pattern is present in various places. Please handle this behavior with caution to avoid unintended actions.

*Disclaimer: Automated interactions with applications, including Discord, may violate their Terms of Service. Use this bot responsibly and in compliance with the service's policies to avoid any adverse consequences.*

## License

This project is licensed under the [MIT License](LICENSE).
