import socket
import time


class ClientError(OSError):
    pass


class Client():
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = float(timeout)

    def put(self, metric, value, timestamp):
        if not timestamp:
            timestamp = str(int(time.time()))
        message = "put {} {} {}\n".format(metric, value, timestamp)

        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(message.encode("utf-8"))
                server_answer = sock.recv(4096).decode('utf8')
                if server_answer == "error\nwrong command\n\n":
                    raise ClientError

            except socket.timeout:
                print("Client send data timeout")
            except socket.error:
                print("Client send data error")

    def get(self, metric):
        answer = dict()
        message = "get {}\n".format(metric)

        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(message.encode("utf-8"))
                server_answer = sock.recv(4096).decode('utf8')

                if server_answer == 'ok\n\n':
                    return {}
                elif server_answer[0:2] == "ok" and server_answer[-2:] == "\n\n":
                    server_answer = server_answer.replace('ok\n', '').replace('\n\n','')
                    data = server_answer.split('\n')
                    records_count = len(data)
                    for i in range(records_count):
                        data[i] = data[i].split(' ')

                    for i in range(records_count):
                        if data[i][0] in answer:
                            answer[data[i][0]].append((int(data[i][2]), float(data[i][1])))
                        else:
                            answer[data[i][0]] = list()
                            answer[data[i][0]].append((int(data[i][2]), float(data[i][1])))

                    for key in answer:
                        answer[key].sort()

                        return answer

                else:
                    raise ClientError

            except socket.timeout:
                print("Client send data timeout")
            except socket.error:
                print("Client send data error")


def main():
    client = Client("127.0.0.1", 10001, 5)
    client.put("load", '301.0', 3)
    client.get('*')
    client.get("key_not_exists")

if __name__ == "__main__":
    main()
