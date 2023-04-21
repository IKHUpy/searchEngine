import os
from dataEntry import tokenization


def main():

    choices = ['Text input', 'Text file']
    choice = input(
        f'What will be the data test type?\n0 - {choices[0]}\n2 - {choices[1]}\ninput here: ')
    if choice == '0':
        text = ''
    elif choice == '1':
        text = ''

    return


if __name__ == '__main__':
    main()
