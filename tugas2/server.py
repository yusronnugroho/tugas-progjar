import sys
import socket
import logging



def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        request = 'TIME \r\n'
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
    for i in range(1,10):
        kirim_data()