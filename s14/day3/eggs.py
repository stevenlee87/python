__author__ = "Steven Lee"


def func_eggs():
    for i in range(100000):
        if i % 1 == 0 and i % 2 == 1 and i % 3 == 0 and i % 4 == 1 and (i + 1) % 5 == 0 and i % 6 == 3 and i % 7 == 0 and i % 8 == 1 and i % 9 == 0:
            print(i)
            break

if __name__ == '__main__':
    func_eggs()
