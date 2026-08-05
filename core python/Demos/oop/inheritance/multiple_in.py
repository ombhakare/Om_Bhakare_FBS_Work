class A:
    def somefun(self):
        print("hello, i am base class")

class B(A):
    def somefun(self):
        print("hello, i am b class")

class C(A):
    def somefun(self):
        print("hello, i am c class")

class D(C,B):
     pass# def somefun(self):
    #     print("hello, i am from d class")

obj = B()
obj.somefun()

obj = C()
obj.somefun()

obj = D()
obj.somefun()