import os
from dataEntry import tokenization
from drwsql import create_connection, token_search_notation


def per_combination(combinations: list):
    records = []
    for items in combinations:
        result = token_search_notation(items)
        for string in result:
            found = False
            for record in records:
                if record[0] == string:
                    record[1] += 1
                    found = True
                    break
            if not found:
                records.append([string, 1])

    return records


def calculate_odd(tokens: list):
    pairs = [[]]


def powerset(tokens: list):
    result = [[]]

    for item in tokens:
        result.extend([subset + [item] for subset in result])

    return result[1:]


def main():

    choices = ['Text input', 'Text file']
    choice = input(
        f'What will be the data test type?\n0 - {choices[0]}\n1 - {choices[1]}\ninput here: ')
    if choice == '0':
        text = input('text to tokenize: ')
        tokens = tokenization(text, [])
        combinations = powerset(tokens)
        print(per_combination(combinations))

    elif choice == '1':
        text = ''
        dir_input = input('dir to tokenize: ')
        with open(str(dir_input), 'r') as f:
            text = f.read()
        tokens = tokenization(text, [])
        combinations = powerset(tokens)

    return


if __name__ == '__main__':
    main()
    # print(powerset(['a', 'b', 'c', 'd']))
    # for item in powerset(['a', 'b', 'c', 'd']):
    #    print(item)
