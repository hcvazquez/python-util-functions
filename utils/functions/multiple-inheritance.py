class A(object):
    def foo(self):
        print('A.foo()')

class B(object):
    def foo(self):
        print('B.foo()')

class C(B, A):
    def foo(self):
        print('C.foo()')
        #A.foo(self)
        #B.foo(self)
        super().foo()
        super(C, self).foo()
        
print("multiple")
c = C()
print(c.foo())
