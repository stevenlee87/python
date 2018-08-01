__author__ = 'stevenlee'


class Server:
    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 21},
    ]

    def __iter__(self):
        for service in self.services:
            if service['active']:
                yield service['protocol'], service['port']


if __name__ == "__main__":
    for protocol, port in Server():
        print('service %s is running on port %d' % (protocol, port))
