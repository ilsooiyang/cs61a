class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color

    def talk(self):
        print(self.name + " says woof!")

class Cat(object):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + " says meow!")

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False

####################################################

class Foo(object):
    def __init__(self, a):
        self.a = a

    def garply(self):
        return self.baz(self.a)

class Bar(Foo):
    a = 1
    def baz(self, val):
        return val

f = Foo(4)
b = Bar(3)

print(f.a)
print(b.a)

# f.garply()
print(b.garply())

b.a = 9
print(b.garply())

f.baz = lambda val: val * val
print(f.garply())

####################################################

class A:
    def f(self):
        return 2

    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

x, y = A(), B()
print(x.f())
print(B.f())
print(x.g(x, 1))
print(y.g(x, 2))

####################################################

class Yolo:
    def __init__(self, motto):
        self.motto = motto

    def g(self, x):
        return self.motto + x

x = Yolo(1)
print(x.g(3))
print(x.g(5))
x.motto = 5
print(x.g(5))




