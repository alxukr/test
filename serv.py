import socket
import threading

def foo(co, ad):
    while True:
        data = co.recv(1024)
        if data.decode() == "close": break
        co.send(data)
    co.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    np = threading.Thread(target=foo, args=(conn, addr))
    np.start()

