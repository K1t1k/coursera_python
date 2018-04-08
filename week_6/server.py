import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.db = list()
#        db.append('test_key 12.0 1503319740')
#        db.append('test_key 13.0 1503319739')
#        db.append('another_key 10 1503319739')

    def connection_made(self, transport):
        self.transport = transport
        peername = transport.get_extra_info("peername")
        print('connection made: {}'.format(peername))

    def data_received(self, data):
        print(f'получен запрос: {data.decode()}')
        resp = self.process_data(data.decode())
#        print('данные для отправки: {}'.format(resp.encode()))
        self.transport.write(resp.encode())

#    def connection_lost(self, exc):
#        print('connection is down')
#        yield from asyncio.sleep(1)

    def process_data(self, data):
        cmd = self._parse(data)

        return cmd

    def _parse(self, data):
        temp = data.replace('\n', '').replace('\r', '')
        temp = temp.split(' ')
        print('список в работу: {}'.format(temp))

        if temp[0] == 'get':
            if temp[1] == '*':
                if self.db:
                    answer = ''
                    for record in self.db:
                        answer += record
                    answer = 'ok\n{}\n\n'.format(answer)
                    return answer
                else:
                    return 'ok\n\n'

            else:
                answer = ''
                for record in self.db:
                    if temp[1] in record:
                        answer += record
                if answer:
                    return answer
                else:
                    return 'ok\n\n'

        elif temp[0] == 'put':
            record = '{}{}{}'.format(temp[1],str(float(temp[2])), str(int(temp[3])))
            self.db.append(record)
            print('data is put')
            return ''

        else:
            return 'error\nwrong command\n\n'


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


if __name__ == '__main__':
    run_server('127.0.0.1', 8888)
