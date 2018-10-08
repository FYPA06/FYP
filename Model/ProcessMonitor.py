
import threading
from time import sleep
import  os

import requests
from Model.Screenshot import *



class ProcessMonitor(threading.Thread):

    def __init__(self, api: str, key: str):
        super().__init__()
        self.name = "ProcessMonitor"
        self.api = api
        self.key = key
        self.black_list_process = []

    def run(self):
        while True:

            try:

                response = requests.post("https://"+self.api+"/process",
                                         headers={ "x-api-key": self.key})

                Screenshot
                files = {'file': ('Screenshot.png', open('Screenshot.png', 'rb'), 'image/png', {'Expires': '0'})}
                if response.ok:
                    print(response.json())
                    upload = response.json()

                    r = requests.post(upload['url'], data=upload['fields'], files=files)
                    
                    

                else:
                    print(response.status_code)
                    print(response.reason)


            except Exception as e:
                print(e)
            sleep(5)

    
