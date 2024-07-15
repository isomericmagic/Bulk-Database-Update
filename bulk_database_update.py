import mysql.connector
from mysql.connector import Error
import csv

try:
    cnx = mysql.connector.connect(host='localhost',
                                         database='test_database',
                                         user='root',
                                         password='notpassword')
    if cnx.is_connected():
        cursor = cnx.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

counter = 0

with open('contacts.csv') as contacts_csv:
  updates_reader = csv.reader(contacts_csv, delimiter=',')
  for row in updates_reader:
    counter += 1
    update_contact = row[0]
    cursor.execute(update_contact)
    cnx.commit()
    if (counter % 1000 == 0):
        print(f"Processed {counter} rows")

cursor.close()
cnx.close()
print("MySQL connection is closed")