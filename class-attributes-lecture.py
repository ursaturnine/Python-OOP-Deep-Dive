"""
                Defining Attributes in Classes

E.G.

class MyClass:
    language = 'Python'
    version = '3.6'

    
Python automatically creates attributes for us
    - e.g. __name__ with a state of 'MyClass'

MyClass also has attributes, "language" and "version"
    - language has a state of 'Python'
    - version has a state of '3.6'


                Retrieving Attribute Values from Objects

getattr() function   getattr(object_symbol, attribute_name, optional_default)
    - ojbect_symbol is "MyClass"
    - attribute_name is any attribute of the class
        - e.g. "language" or "version"

getattr(MyClass, 'language') 
    - property names are always strings

What if an attribute doesn't exist in the class?
    - e.g. getattr(MyClass, "x") ---> AttributeError exception
    - e.g. getattr(MyClass, "x", "N/A") --> 'N/A'

Dot Notation(shorthand)
    - e.g. MyClass.lanugage --> 'Python'
    - e.g. MyClass.x --> AttributeError exception
    - no default option with shorhand


                Setting Attribute Values in Objects 

setattr() function --> setattr(object_symbol, attribute_name, attribute_value)
    - e.g. setattr(MyClass, 'version', '3.7')
    - this modifies, or mutates, the state of the class

Dot Notation(shorthand)
    - e.g. MyClass.version = '3.7'

What if an attribute doesn't exist when we try to set it?
    - Python is a dynamic language --> can modify our classes at runtime (usually)
        - e.g. setattr(MyClass, 'x', 100)
    

                Where is that State Stored?
- In a dictionary
- MyClass.__dict__ --> returns a mapping proxy
    - not a dict type but it's still a dictonary/hashmap (readonly)
    - Python can ensure all of the keys are strings (helps performance/speed)

"The class namespace"
- not directly mutable (but setattr can)
mapping proxy({'__module__': '__main__',
                'language': 'Python',
                'version': '3.6',
                '__dict__': <attribute '__dict__' of 'MyClass' objects>,
                '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
                '__doc__': None
                })

                Deleting Attributes
delattr(obj_symbol, attribute_name) or del keyword
    - e.g. delattr(MyClass, 'version')

Dot Notation(shorthand)
    - e.g. del MyClass.version



"""