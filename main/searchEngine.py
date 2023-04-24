import os
from dataEntry import tokenization


def main():

    choices = ['Text input', 'Text file']
    choice = input(
        f'What will be the data test type?\n0 - {choices[0]}\n2 - {choices[1]}\ninput here: ')
    if choice == '0':
        text = input('text to tokenize: ')

    elif choice == '1':
        text = ''
        dir_input = input('dir to tokenize: ')
        with open(str(dir_input), 'r') as f:
            text = f.read()

    return


if __name__ == '__main__':
    main()
