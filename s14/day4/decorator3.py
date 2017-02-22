__author__ = "Steven Lee"

x = 0
def grandapa():
    x = 1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    dad()
grandapa()