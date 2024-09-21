import cv2
import pyautogui
import time

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return "screenshot.png"

def find_image_in_screenshot(image_path, screenshot_path):
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    screenshot = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)
    
    if template is None or screenshot is None:
        raise FileNotFoundError("bug, report at github/whoispiguo pls!")
    
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val > 0.5:  
        return max_loc
    return None

def click_on_image(image_path, click_location, text_to_type=None):
    screenshot_path = take_screenshot()
    location = find_image_in_screenshot(image_path, screenshot_path)
    
    if location:
        pyautogui.click(click_location[0], click_location[1])
        if text_to_type:
            pyautogui.typewrite(text_to_type)
        print(f"done.")
    else:
        print(f"waiting queue.")

def image_exists(image_path):
    screenshot_path = take_screenshot()
    location = find_image_in_screenshot(image_path, screenshot_path)
    return location is not None

def main():
    text_to_type2 = input("Ban champ: ")
    text_to_type = input("Pick champ: ")
    while True:
        click_on_image('found.png', (920,750))
        time.sleep(5)
        if image_exists('search.png'):
            time.sleep(18)
            click_on_image('search.png', (1220, 190), text_to_type2)
            time.sleep(1)
            click_on_image('search.png', (620, 290))
            time.sleep(3)
            click_on_image('pick.png', (920,850))
            time.sleep(26)
            click_on_image('search.png', (1220, 190), text_to_type)
            time.sleep(1)
            click_on_image('search.png', (620, 290))
            time.sleep(3)
            click_on_image('pick.png', (920,850))


if __name__ == "__main__":
    main()
