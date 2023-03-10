"""
What is an Object?
- Container
Contains data (state and attributes)
Contains functionality (behavior and methods)

E.G

Object: my_car

State:

brand = Ferrari
model = 599XX
year = 2010

Behavior:

accelerate
brake
steer


Access State and Behavior with dot notation


How Do We Create the Container?
- a class-based approach
    - A class is like a template to create objects
    - A class is also called a type
    - Objects created from a type, or class, are called, "instances"
    - Classes are themselves called objects (they have attributes/state and behavior/methods)
    - classes are created from the type, "metaclass"
    - classes have "behavior" -> they are callable (e.g. MyClass()) <-- this returns an instance of a class

Instance
- their type is the class they were created from

How Do We Create a Class?
- use "class" keyword
1. Python creates an object --> class MyClass: pass
    - called, "MyClass"
    - of type, "type"
2. This automatically provides us certain attributes (state) and methods (behavior)
    - e.g. MyClass.__name__
        - dunder name attribute
        - returns the string, "MyClass"
        - (state)
    - e.g. MyClass()
    - returns an instance of MyClass
    - (behavior)

"""