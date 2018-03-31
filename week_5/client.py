import socket
import time


class ClientError(OSError):
    pass


class Client():
    def __init__(self, host, port, timeout=None):
        self.conn = socket.create_connection((host, port), float(timeout))

    def put(self, metric, value, timestamp):
        if not timestamp:
            timestamp = str(int(time.time()))
        message = "put {} {} {}\n".format(metric, value, timestamp)
        self.conn.sendall(message.encode("utf-8"))
        server_answer = self.conn.recv(4096).decode('utf8')
        if server_answer == "error\nwrong command\n\n":
            raise ClientError

    def get(self, metric):
        answer = dict()
        message = "get {}\n".format(metric)
        self.conn.sendall(message.encode("utf-8"))
        serv_ans = self.conn.recv(4096).decode('utf8')
        if serv_ans == 'ok\n\n':
            return {}
        elif serv_ans[0:2] == "ok" and serv_ans[-2:] == "\n\n":
            serv_ans = serv_ans.replace('ok\n', '').replace('\n\n', '')
            data = serv_ans.split('\n')
            records_count = len(data)
            for i in range(records_count):
                data[i] = data[i].split(' ')

            for i in range(records_count):
                if data[i][0] in answer:
                    answer[data[i][0]].append((int(data[i][2]),
                                               float(data[i][1])))
                else:
                    answer[data[i][0]] = list()
                    answer[data[i][0]].append((int(data[i][2]),
                                               float(data[i][1])))
            for key in answer:
                answer[key].sort()

                return answer

        else:
            print("Server error")
            raise ClientError


def main():
    client = Client("127.0.0.1", 8888, 5)
    client.put("load", '301.0', 3)
    client.get('*')
    client.get("key_not_exists")

if __name__ == "__main__":
    main()
