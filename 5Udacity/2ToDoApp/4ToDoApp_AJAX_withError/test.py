class test:
    def __init__(self, val):
        self.x = val

    def addVal(self, val):
        print('original self.x = ' + str(self.x))
        self.x += val
        print('new self.x = ' + str(self.x))




example1 = test(1)
example1.addVal(3)