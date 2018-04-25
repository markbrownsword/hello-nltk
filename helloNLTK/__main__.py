import sys
from puncpy.classmodule import MyClass
from puncpy.funcmodule import my_function


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    my_function('hello world')

    my_object = MyClass('This is my own invention')
    result = my_object.tag_text()

    for item in result:
        print(item)


if __name__ == '__main__':
    main()
