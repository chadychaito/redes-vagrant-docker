import socket
import time
import schedule

host = '172.17.0.4'
port = 8220
address = (host, port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

count = 1

def job():
    global count

    fname = 'arquivos/teste' + str(count) + '.txt'
    arq = open(fname, 'rb')
    
    for i in arq.readlines():
        client_socket.send(i)

    while client_socket.recv(2048) != (b"ack"):
        print ("Waiting for ACK...")

    print ("ACK received! File", count, "sent.")
    count = count + 1
    if count > 4:
        count = 1

schedule.every(0.4).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
