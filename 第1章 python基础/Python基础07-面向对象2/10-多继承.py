class Base(object):
    def test(self):
        print("---test---")

class A(Base):
    def test1(self):
        print("---test1---")

class B(Base):
    def test2(self):
        print("---test2---")

class C(A,B):
    pass

c = C()
c.test()
c.test1()
c.test2()
