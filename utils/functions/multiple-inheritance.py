class A(object):
    def foo(self):
        print('A.foo()')

class B(object):
    def foo(self):
        print('B.foo()')

class C(A, B):
    def foo(self):
        print('C.foo()')
        super().foo()
        
print("multiple")
c = C()
c.foo()
print(C.__mro__)
