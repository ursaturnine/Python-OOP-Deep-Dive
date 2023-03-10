"""
Callable Class Attributes
                Setting a Class Attribute to a Callable
Attribute values can be any object  --> other classes --> any callable --> anything..

E.G.

class MyClass:
    language = 'Python'

    def say_hello():
        print("Hello World!")

- say_hello is an attribute but it is 'callable'

        How Do We Call say_hello?

We Could Get It Straight From The Namespace Dictionary
    - e.g. my_func = MyClass.__dict__['say_hello']
    - my_func() --> 'Hello World!'

    or
    - e.g. MyClass.__dict__['say_hello']()

We Could Use getattr
    - e.g. getattr(MyClass, 'say_hello')()

We Could Use Dot Notation
    - e.g. MyClass.say_hello() --> 'Hello World!'

"""