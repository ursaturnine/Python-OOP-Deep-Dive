"""
Classes Are Callable

                Class Instantiation --> 'Instantiating the Class'

When We Create a Class Using the 'class' Keyword...

Python automatically adds behavior to the class
    - it adds something to make the class callable
    - the return value of that callable is an object
    - the type of that object is the class object
    - the object is an instance of the class

When we call a class...
A class instance object is created
    - The class instance object has its own namespace (its own dictionary that contains its own state)
    - distinct from the namespace of the class that was used to create the object

Python automatically adds some attributes
    - __dict__
        - the object's local namespace
    - __class__
        - tells us which class was used to instantiate the object
        - prefer using type(obj) or isinstance(obj, class)
"""