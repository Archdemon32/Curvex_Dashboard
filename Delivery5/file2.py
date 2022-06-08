# Imports
import mysql.connector  as mc
import pika
# Connecting to the databse
try:
    connection = mc.connect(host='dp-base.mysql.database.azure.com',
                                         database='mydatabase',
                                         user='archdemon32@dp-base',
                                         password='Pepega321998')
# Selecting table and fetching the data
    sql_select_Query = "select * from test2"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
# Writting the data into a csv file
    for row in records:
        with open('data/SQL_Customer_data.csv','a+') as l:
            l.write(str(row))
            l.write('\n')
# Error excption
except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
# Using rabitMQ to send a message if the conncetion was sucessfull
finally:
    if connection.is_connected():
        connection1 = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection1.channel()

        channel.queue_declare(queue='data')

        channel.basic_publish(exchange='', routing_key='data', body=("Records retrieved successfully from MYSQL database"))
        connection.close()
        cursor.close()
