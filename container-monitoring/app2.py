import time
import docker
import datetime
import schedule
from pymongo import MongoClient

cliente = MongoClient('mongodb://192.168.50.3:27018/')
cli = docker.from_env()

def insert():
    banco = cliente.redes
    containers = banco.containers

    for container in cli.containers.list():
        stats = container.stats(decode=True,stream=True)
        current = next(stats)

        try:
            container = {
                "timestamp": datetime.datetime.now(),
                "id": container.id,
                "nome": container.name,
                "uso-cpu": current["cpu_stats"]["cpu_usage"]["total_usage"],
                "memoria": current["memory_stats"]["usage"],
                "rx": current["networks"]["eth0"]["rx_bytes"],
                "tx": current["networks"]["eth0"]["tx_bytes"]
                }

            containers.insert_one(container).inserted_id
        except:
            print("An exception occurred")

schedule.every(1).minutes.do(insert)

while True:
    schedule.run_pending()
    time.sleep(1)
