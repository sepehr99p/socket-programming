import socket
import time


server_time = time.ctime() #corrunt time,zaman felli ro set mikone roye server_time

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock_ip = "localhost"
sock_port = 9999

#mige beshin be in ip va port montazer bash ke behet vasl beshan
sock.bind((sock_port,sock_ip)



#mige ka maximum chand nafar mitunan behem connect beshan
sock.listen(1)

while True:
    c , addr = sock.accept()
    #in accept 2 ta return mikone
    #c manzur cliente va addr adresehse fekr konam

    print("one client has been connected !")  # ino vase khodam minevisam ke motevajeh besham ke kasi connect shod behem
    #vase client ino mifrestam vaghti ke be man connect shod
    try:
        c.send("hello there")
    except TypeError:
        print("an type error has fucked me")
    finally:
        c.close()