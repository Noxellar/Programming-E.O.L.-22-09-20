class A():
    def kill_a(self):
        print(self)
        del self

    def kill_b(self):
        print(self)


a = A()
b = A()

a.kill_a()
b.kill_b()
