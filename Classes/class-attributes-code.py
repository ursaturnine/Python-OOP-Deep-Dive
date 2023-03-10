
class Person:
    pass
    
class Program:
    language = 'Python'
    version = '3.8'

if __name__ == "__main__":
    # Person
    print("Dunder name for Person class returns 'Person': ")
    print(Person.__name__)
    print("\n")
    # Program
    print("Dunder name for Program class returns 'Program:")
    print(Program.__name__)
    print("\n") 
    print("The type of Program class is 'type: ")
    print(type(Program))
    print("\n")

    print("The 'language' attribute in the Program class returns 'Python': ")
    print(Program.language)
    print("\n")

    print("Mutating the version attribute, so 'version' is now 3.9:")
    Program.version = '3.9'
    print(Program.version)
    print("\n")

    print("Getting the language attribute from the Program class with the getattr function: ")
    print(getattr(Program, 'language'))
    print('\n')

    print("Mutating the 'version' attribute in the Program class with the setattr function:")
    setattr(Program, 'version', '3.8')
    print(Program.version)