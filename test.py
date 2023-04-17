import mysql.connector

# The goal is to enter the dataset and is expected to know the title based on an user input


def create_connection():
    connection = mysql.connector.connect(
        user='root',
        password='09218692170',
        host='127.0.0.1',
        database='t2_drw'
    )
    return connection


def insert_data(connection, title, title_tokens, source):
    cursor = connection.cursor()
    ins_title = f'INSERT INTO t2_drw.title (name, source) VALUES ("{title}", "{source}");'
    print(ins_title)
    cursor.execute(ins_title)
    for token in title_tokens:
        ins_data = f'INSERT INTO data (word, title, source) VALUES ("{token}", "{title}", "{source}")'
        cursor.execute(ins_data)
    connection.commit()
    cursor.close()


insert_data(create_connection(), 'tt', ['1', '2', '3'], 'mayoclinic')
