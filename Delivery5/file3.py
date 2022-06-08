# Imports
import pandas as pd
from pymongo import MongoClient
import pika

# Creating a datarame from the try.csv file
df = pd.read_csv(r"C:\Users\archd\Desktop\demo\try.csv", index_col=False, delimiter = ';')

# Making a Connection with MongoClient
def get_database():
    client = MongoClient("mongodb://localhost:27017/mydb")
    return client['mydb']
if __name__ == "__main__":
    dbname = get_database()
# Inserting customer data into Deliv5 collection in MongoDB
collection_name = dbname["Deliv5"]
collection_name.insert_many(df.apply(lambda x: x.to_dict(), axis=1).to_list())

# Sending a message through RabitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='data')

channel.basic_publish(exchange='', routing_key='data', body=("Record inserted successfully into Deliv5 collection in MongoDB"))
connection.close()
