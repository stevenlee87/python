__author__ = 'stevenlee'


class IterableServer:

    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]

    def __init__(self):
        self.current_pos = 0  # 我们初始化当前位置为 0

    def __iter__(self):  # 我们可以在这里返回 self，因为实现了 __next__
        return self

    def __next__(self):
        while self.current_pos < len(self.services):
            service = self.services[self.current_pos]
            self.current_pos += 1
            if service['active']:
                return service['protocol'], service['port']
        raise StopIteration

    next = __next__  # 可选的 Python2 兼容性


if __name__ == "__main__":
    for protocol, port in IterableServer():
        print('service %s is running on port %d' % (protocol, port))
