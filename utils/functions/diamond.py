class FooBase(object):
    def foo(self, who):
        print('FooBase.foo()', who)

class A(FooBase):
    def foo(self, s):
        print('A.foo() before super()')
        super(A, self).foo("Im A")
        print('A.foo() after super()')

class B(FooBase):
    def foo(self, s):
        print('B.foo() before super()')
        super(B, self).foo("Im B")
        print('B.foo() after super()')

class C(A, B):
    def foo(self, s):
        print('C.foo() before super()')
        super(C, self).foo("")
        print('C.foo() after super()')
        
c = C()
c.foo("")
print(C.__mro__)