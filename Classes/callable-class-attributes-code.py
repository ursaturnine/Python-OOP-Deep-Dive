
class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}')
        return
    

if __name__ == '__main__':
    print("Program class namespace dictionary:")
    print(Program.__dict__)
    print('\n')

    print("Calling say_hello through dot notation")
    print(Program.say_hello())
    print('\n')