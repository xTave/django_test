class ThreadPool:
    threads = []

    def run(self):
        while True:
            for i in self.threads:
                if not i.finish:
                    import random
                    r = random.randint(1, 3)
                    i.run(r)
            if all(thread.finish for thread in self.threads):
                break


class Thread:
    def __init__(self, *args):
        self.funcs = args
        self.x = 0
        self.finish = False

    def run(self, x):
        for i in range(self.x, min(self.x + x, len(self.funcs))):
            self.funcs[i]()
        self.x += x
        if self.x >= len(self.funcs):
            self.finish = True


def q1():
    print(1)

def q2():
    print(2)



ThreadPool.threads = [Thread(*[q1 for i in range(10)]), Thread(*[q2 for i in range(10)])]
ThreadPool().run()