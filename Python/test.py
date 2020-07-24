class A(object):
    static = "alsdjflkajds;lf"


class B(A):
    def method(self):
        print(self.static)


b = B()
b.method()
