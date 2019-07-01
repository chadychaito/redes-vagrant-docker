import time
import psutil
import socket
import datetime
import schedule
from pymongo import MongoClient

cliente = MongoClient('mongodb://172.17.0.3:27017/')

def insert():
    banco = cliente.redes
    vms = banco.vms

    vm = {
        "timestamp": datetime.datetime.now(), 
        "nome": socket.gethostname(),
        "cpu": psutil.cpu_percent(),
        "memoria": psutil.virtual_memory()[2]
        }

    vms.insert_one(vm).inserted_id

schedule.every(1).minutes.do(insert)

while True:
    schedule.run_pending()
    time.sleep(1)
