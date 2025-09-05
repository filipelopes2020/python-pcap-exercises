O = object
class X(O): pass
class Y(O): pass
class A(X,Y): pass
class B(Y,X): pass

class Foo(Y, B): pass
class Foo(B, Y): pass
class Foo(X, A): pass
class Foo(B, A): pass
class Foo(A, X): pass
class Foo(A, B): pass