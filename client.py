import socket

#ye object ya instance sakhtam az class socket va badesh method socket() ro seda zadam
#AF_INET mige ke dari az nemudunam chichie 4 estefade mikoni ke kole donya az 6 estefade mikone vali ma az 4 estefade mikonim
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock_ip = "localhost"
sock_port = 9999

#inja mikhaim talash konim ke connect beshim be server
sock.connect((sock_ip,sock_port))

#mige ke 1024 ta 1024 ta data az samte server mitunam daryaft bokonam
print(sock.recv(1024))
