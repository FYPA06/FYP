import time


# Get the time and date
class Screenshot:
    timestr = time.strftime("%Y%m%d-%H%M%S")

    def window(self,time):
        import pyautogui
        # Take screenshot
        pic = pyautogui.screenshot()

        # Save the image
        return pic.save(str(time) + '.png')

    def linux(self,time):
        import numpy as np
        import pyautogui
        import imutils
        import cv2
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        return cv2.imwrite(str(time) + '.png', image)
