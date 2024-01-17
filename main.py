import socket
import cv2
from utils import UdpReceiveParser


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)

addr = ("192.168.1.1", 7080)

client_socket.sendto(bytes([32, 54]), addr)

parser = UdpReceiveParser()

while True:
    data, addr = client_socket.recvfrom(65535)

    parser.parse(data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
