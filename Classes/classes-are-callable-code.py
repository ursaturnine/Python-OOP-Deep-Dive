

class Program:
    language = 'Python'

    def say_hello():
        print(f"Hello from {Program.language}")


if __name__ == '__main__':

    print('Creating instance of class Program...')
    p = Program()
    print('\n')
    print('Type of object, p, is class, Program:')
    print(type(p))
    print('\n')

    print('Checking if p is of type Program w isinstance method...')
    print(isinstance(p, Program))
    print('\n')