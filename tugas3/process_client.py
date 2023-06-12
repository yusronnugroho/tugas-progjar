import sys
import socket
import logging
from multiprocessing import Process

def kirim_request():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    request = 'TIME \r\n'

    try:
        # Send data
        logging.warning(f"[CLIENT] request {request}")
        sock.sendall(request.encode())
        while True:
            data = sock.recv(16)
            logging.warning(f"[WAKTU DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    thread = 0
    for i in range(0, 1000):
        thread += 1
        process = Process(target=kirim_request)
        process.start()
        print(f"Process amount: {thread}")