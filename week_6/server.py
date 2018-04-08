import asyncio


class ClientServerProtocol(asyncio.Protocol):

    db = list()

    def connection_made(self, transport):
        self.transport = transport
        peername = transport.get_extra_info("peername")
        print('connection made: {}'.format(peername))

    def data_received(self, data):
        print(f'получен запрос: {data.decode()}')
        resp = self.process_data(data.decode())
        print(f'данные для отправки: {resp}')
        self.transport.write(str(resp).encode())

    @classmethod
    def process_data(cls, data):
        temp = data.replace('\n', '').replace('\r', '')
        temp = temp.split(' ')
        print('список в работу: {}'.format(temp))

        if temp[0] == 'get':
            if temp[1] == '*':
                if cls.db:
                    answer = ''
                    for record in cls.db:
                        answer += record
                    answer = 'ok\n{}\n\n'.format(answer)
                    return answer
                else:
                    return 'ok\n\n'

            else:
                answer = ''
                for record in cls.db:
                    if temp[1] in record:
                        answer += f'{record}'
                        print(f'answer: {answer}')
                if answer:
                    return f'ok\n{answer}\n'
                else:
                    return 'ok\n\n'

        elif temp[0] == 'put':
            record = '{} {} {}\n'.format(temp[1], str(float(temp[2])), str(int(temp[3])))
            if not record in cls.db:
                cls.db.append(record)
                print('data is put')
                print(cls.db)
                return 'ok\n\n'
            else:
                return 'ok\n\n'

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
