import socket
import time
from random import randrange, shuffle

UDP_IP = "127.0.0.1"
UDP_PORT = 12345

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

ctr = 0
message = [0]*1024
sleep_time = 0.1

def send_data(prefix, data, force_sleep_time=None):
    sock.sendto(bytearray(prefix+data), (UDP_IP, UDP_PORT))
    time.sleep(force_sleep_time or sleep_time)


while True:

    lst1 = list(range(255))
    lst2 = list(range(255))
    lst3 = list(range(255))
    shuffle(lst1)
    shuffle(lst2)
    shuffle(lst3)
    
    for i in range(len(lst1)):
        for j in range(0, len(lst1) - i - 1):
            if lst1[j] > lst1[j + 1]:
                lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
                send_data([0],lst1, force_sleep_time=0.001)
        send_data([0], lst1)


    for i in range(1, len(lst2)):
        key = lst2[i]
        j = i - 1
        while j >= 0 and key < lst2[j]:
            lst2[j + 1] = lst2[j]
            j -= 1
        lst2[j + 1] = key
        send_data([1], lst2)


    for i in range(len(lst3)):
        min_index = i
        for j in range(i + 1, len(lst3)):
            if lst3[min_index] > lst3[j]:
                min_index = j

        lst3[i], lst3[min_index] = lst3[min_index], lst3[i]
        send_data([2], lst3)

