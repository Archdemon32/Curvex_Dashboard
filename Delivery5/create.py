# Imports
import mysql.connector as mc
from pymongo import MongoClient
# Connecting to the server
connection = mc.connect(host='dp-base.mysql.database.azure.com',
                                     user='archdemon32@dp-base',
                                     password='Pepega321998')
cursor = connection.cursor()
# Creating the database
cursor.execute('CREATE DATABASE IF NOT EXISTS mydatabase')
# Creating table
def CreateTable():
    connection = mc.connect(host='dp-base.mysql.database.azure.com',
                                     database='mydatabase',
                                     user='archdemon32@dp-base',
                                     password='Pepega321998')
    cursor = connection.cursor()
    test2 ='CREATE TABLE IF NOT EXISTS test2 (Delta VARCHAR(255), Theta VARCHAR(255), Low_Alpha VARCHAR(255), High_Alpha VARCHAR(255), Low_Beta VARCHAR(255), High_Beta VARCHAR(255), Low_Gamma VARCHAR(255), Middle_Gamma VARCHAR(255));'
    cursor.execute(test2)
    return
CreateTable()

#Creating a pymongo client
client = MongoClient('mongodb://localhost:27017')

#Creating the database and the collection
pepa= client['mydb']
collection = pepa['Deliv5']
