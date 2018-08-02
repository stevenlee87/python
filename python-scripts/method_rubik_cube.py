__author__ = 'stevenlee'


class Operations:

    def say_hi(self, name):
        print('Hello,', name)

    def say_bye(self, name):
        print ('Goodbye,', name)

    def default(self, arg):
        print ('This operation is not supported.')

if __name__ == '__main__':
    operations = Operations()
    # 假设我们做了错误处理
    command, argument = input('> ').split()
    func_to_call = getattr(operations, command, operations.default)
    func_to_call(argument)

# say_hi lee
# test test