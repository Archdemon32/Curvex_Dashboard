Descrition of files:

create.py - This file is used to create a SQL and a NOSQL databases and relevant collections and tables

receiveDeliv5.py - Establishing a receiver for messages sent by the other scripts

file.py - Inserting information into an SQL database from a csv file

file2.py - Retreiving information from an SQL database into a csv file

file3.py - Inserting information into a NOSQL database from a csv file

file4.py - Retreiving information from a NOSQL database into a csv file

try.csv - Sample csv data file used for insertion of data

data/NOSQL_Customer_data.csv - Output file for the data collected from a MongoDB database (created by file4.py)

data/SQL_Customer_data.csv - Output file for the data collected from an Azure Database for MySQL single server database (created by file2.py)

Additionally please read the requirments.txt

In order to see the full functionallity of the code (as shown in the report), please install Erlang and RabbitMQ in accordance with this guide: https://kea.officegeek.dk/4sem/09-IT_architecture_Microservice/Rabbitmq.html

Next please run the create.py in order to create the databse and the table on the server (they already exist, but this file is written if you would like to try it for your own server)

Once the conditions have been met, run the receiveDeliv5.py on a a separate terminal, from where you will be running the data insertion/collection scripts (file.py, file2.py, file3.py, file4.py).

Lastly run all the files in asending order and than check out the retrieved information in the data folder.
