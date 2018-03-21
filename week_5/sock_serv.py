import socket

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    # создание нескольких процессов
    while True:
        # accept распределится "равномерно" между процессами
        conn, addr = sock.accept()
        # поток для обработки соединения
        with conn:
            print('start server')
            while True:
                data = conn.recv(1024)
                message = 'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
                sock.sendall(message.encode("utf-8"))
                if not data:
                    break
                print(data.decode("utf8"))
