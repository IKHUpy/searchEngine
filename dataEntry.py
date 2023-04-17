import os
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import mysql.connector


# The goal is to enter the dataset and is expected to know the title based on an user input


def create_connection():
    connection = mysql.connector.connect(
        user='user',
        password='passwd',
        host='localhost',
        database='db'
    )
    return connection


def insert_data(connection, title, title_tokens, source):
    cursor = connection.cursor()
    ins_title = f'INSERT IGNORE INTO db.title (name, source) VALUES ("{title}", "{source}");'
    print(ins_title)
    cursor.execute(ins_title)
    for token in title_tokens:
        ins_data = f'INSERT INTO data (word, title, source) VALUES ("{token}", "{title}", "{source}")'
        cursor.execute(ins_data)
    connection.commit()
    cursor.close()


def html_to_text(html_file):
    # Check if the input HTML file exists
    if not os.path.isfile(html_file):
        print(f"Error: {html_file} not found.")
        return

    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the text from the HTML
    text = soup.get_text()

    return text


# mayoclinic folder is already Text-Only ready.
def surf_source_path(folder_path, source):
    connection = create_connection()
    stop_words = set(stopwords.words('english'))
    irrelevant_strings = ['href=', 'class=', 'id=', '&l', 'symptom']
    for filename in os.listdir(folder_path):
        if filename.endswith(".text"):

            with open(folder_path + '/' + filename, 'r') as f:
                if source == 'webmd':
                    title = filename[:-14].lower()
                    text = f.read()
                elif source == 'mayoclinic':
                    title = filename[:-5].lower()
                    text = f.read()
            title_tokens = tokenization(text, stop_words, irrelevant_strings)
            print(title_tokens)
            insert_data(connection, title, title_tokens, source)


def tokenization(text, stop_words, irrelevant_strings):
    rm_char = ['"', '(', ')', ':', ';', '.', '—', ',']
    for char in rm_char:
        text = text.replace(char, '')
    tokens = text.split()
    excluded_stop_words = [''.join(c for c in token if c not in rm_char).lower()
                           for token in tokens
                           if token.lower() not in stop_words and
                           all(substring not in token.lower() for substring in irrelevant_strings)]
    excluded_stop_words = list(set(excluded_stop_words))
    return excluded_stop_words


def main():
    source_ls = ['', 'mayoclinic', 'webmd']
    choice = input('1 - mayoclinic \n2 - webmd \ninput: ')
    paths = [
        '', 'mayoclinic dir', 'webmd dir']
    path_choice = input(
        f'Given paths:\n1: {paths[1]}\n2: {paths[2]}\npath: ')
    if choice == '1':
        surf_source_path(str(paths[int(path_choice)]),
                         str(source_ls[int(choice)]))
        return
    if choice == '2':
        surf_source_path(str(paths[int(path_choice)]),
                         str(source_ls[int(choice)]))


if __name__ == '__main__':
    main()
