import os
import time
import pyautogui

FOLDER_PATH = "img/"

def left_click(path) -> bool:
    location = pyautogui.locateCenterOnScreen(path, confidence=0.9)
    flag = True
    for i in range(5):
        if location is not None:
            pyautogui.click(location.x, location.y)
            flag = False
            break
        else:
            time.sleep(1)
    return flag


if __name__ == '__main__':
    dirs = os.listdir(FOLDER_PATH)
    for name in dirs:
        path = os.path.abspath(os.path.join(FOLDER_PATH, name))
        ret = left_click(path)
        if(ret):
            del pyautogui
            pyautogui = __import__('pyautogui')
            if(left_click(path)):
                print("未找到匹配图片:" + path)
            else:
                continue
            break