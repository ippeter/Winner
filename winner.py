import time
import os
import random as rd

from pymongo import MongoClient

# Get values from environment variables
strMongoHost = os.environ['MONGO_SERVICE_HOST']
strMongoPort = os.environ['MONGO_SERVICE_PORT']
strMongoUser = os.environ['MONGO_USERNAME']
strMongoPswd = os.environ['MONGO_PASSWORD']

# Open the connection to the database
strConnectionString = 'mongodb://' + strMongoUser + ":" + strMongoPswd + "@" + strMongoHost + ":" + strMongoPort
db_conn = MongoClient(strConnectionString)

# Wait until no more records in the database
records_count = db_conn.demo.demo.count_documents({})
print("{} documents found so far. Let people add more..".format(records_count))
time.sleep(60)

temp_count = db_conn.demo.demo.count_documents({})

while (temp_count != records_count):
    print("New documents arrived.")
    records_count = temp_count
    time.sleep(30)
    temp_count = db_conn.demo.demo.count_documents({})
    
user_ids = db_conn.demo.demo.distinct("userId")

# Randomly select the winner
winner = rd.choice(user_ids)

# Write the winner id to the file
f = open("/winner/winner.txt", "w")
f.write("And the winner is " + winner + "\n")

# Get all DB entries for the winner
all_winner_records = db_conn.demo.demo.find({ "userId" : winner})

# And write them to the file
for doc in all_winner_records:
    f.write("{}, pod IP: {} running at node {}\n".format(doc['userId'], doc['podIP'], doc['nodeName']))

# Clean up the resources
f.close()
db_conn.close()

