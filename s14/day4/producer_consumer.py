import time
__author__ = "Steven Lee"
# 协程


def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
        baozi = yield

        print("包子[%s]来了,被[%s]吃了!" % (baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("%s做了1个包子,分成了两半!" % name)
        c.send(i)
        c2.send(i)

producer("alex")
