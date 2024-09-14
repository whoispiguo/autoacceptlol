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
        raise FileNotFoundError("No se pudo cargar la imagen. Verifica que los archivos estén en la misma carpeta que el script.")
    
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val > 0.5:  
        return max_loc
    return None

def click_on_image(image_path):
    screenshot_path = take_screenshot()
    location = find_image_in_screenshot(image_path, screenshot_path)
    
    if location:
        pyautogui.click(location[0] + 360, location[1] + 600)
        print("Partida aceptada.")

    else:
        print("No salta cola.")

def main():
    while True:
        click_on_image('found.png')
        time.sleep(5)

if __name__ == "__main__":
    main()