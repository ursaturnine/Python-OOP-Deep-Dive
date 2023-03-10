

class Person:
    pass


if __name__ == "__main__":
    # type of Person
    print(type(Person))

    # attribute 
    print(Person.__name__)

    # instance of Person class
    p = Person()
    print(p)
    # instance of Person class is of type, Person
    print(type(p))

    # check if object, "p", is type of Person class
    print(isinstance(p, Person))
