import asyncio


class ClientServerProtocol(asyncio.Protocol):

    db = dict()

    def connection_made(self, transport):
        self.transport = transport
        peername = transport.get_extra_info("peername")
        print('connection made: {}'.format(peername))

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())
        self.transport.close()

    def connection_lost(self, exc):
        print('connection is down')

    def process_data(self, data):
        cmd = self._parse(data)

        resp = data
        return resp

    def _parse(self, data):
        temp = data.split(' ')

        if temp[0] == 'get':
            if temp[1] == '*':
                answer = self.db
                return answer
            else:
                if temp[1] in self.db:
                    answer = dict()
                    answer[temp[1]] = self.db[temp[1]]
                    return answer
                else:
                    return 'ok\n\n'

        elif temp[0] == 'put':
            if temp[1] in self.db:
                self.db[temp[1]].append((int(temp[3]), float(temp[2])))
            else:
                self.db[temp[1]] = list()
                self.db[temp[1]].append((int(temp[3]), float(temp[2])))
            print('data is put')
            print(self.db)
            return 'ok\n\n'

        else:
            print('Error')
            return 'wrong command\n'
        print(temp)


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


def main():
    run_server('127.0.0.1', 8181)


if __name__ == '__main__':
    main()