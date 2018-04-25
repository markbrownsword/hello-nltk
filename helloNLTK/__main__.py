import sys
from puncpy.tagger import Tagger
from puncpy.common import process_tagged_text


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    tagger = Tagger('This is my own invention')
    result = tagger.tag_text()

    process_tagged_text(result)


if __name__ == '__main__':
    main()
