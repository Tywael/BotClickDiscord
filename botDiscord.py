import pygetwindow as gw
import cv2
import numpy as np
import pyautogui


def find_pattern_on_screen(pattern_image_path, threshold=0.8):
    pattern_image = cv2.imread(pattern_image_path, cv2.IMREAD_GRAYSCALE)

    screenshot = pyautogui.screenshot()
    screenshot_image = np.array(screenshot)
    screenshot_image_gray = cv2.cvtColor(screenshot_image, cv2.COLOR_RGB2GRAY)

    result = cv2.matchTemplate(screenshot_image_gray, pattern_image, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    occurrences = []
    for loc in zip(*locations[::-1]):
        top_left = loc
        occurrences.append(top_left)

    return occurrences


def find_discord_title():
    titles = gw.getAllTitles()
    for title in titles:
        if ' - Discord' in title:
            return title
    return None


def get_process_window_pos():
    process_name = find_discord_title()
    try:
        window = gw.getWindowsWithTitle(process_name)[0]
        print(window)
        return window
    except IndexError:
        return None


def bot_discord():
    app_pos = get_process_window_pos()
    if app_pos:
        app_pos.activate()
        app_pos.maximize()
        while 1:
            clic_pos = find_pattern_on_screen("./img.png")
            for i, pos in enumerate(clic_pos, 1):
                pyautogui.click(pos[0], pos[1])
    else:
        print(f"Application 'Discord' n'est pas en cours d'exécution.")


if __name__ == '__main__':
    bot_discord()