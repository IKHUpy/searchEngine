# Prerequisite checkpoint

import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    user='root', password='passwd', host='127.0.0.1', database='t2_drw')
cursor = cnx.cursor()

# Define the input words
input_words = ['nodules', 'red', 'hair', 'deep', 'skin']

# Construct the dynamic SQL query
query = "SELECT DISTINCT d1.title FROM data d1"
for i in range(1, len(input_words)):
    query += f" JOIN data d{i + 1} ON d1.title = d{i + 1}.title"

query += " WHERE "
for i, word in enumerate(input_words):
    query += f"d{i + 1}.word = '{word}'"
    if i < len(input_words) - 1:
        query += " AND "

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the database connection
cursor.close()
cnx.close()
