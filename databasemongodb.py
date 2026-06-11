import pymongo


myClient = pymongo.MongoClient('mongodb+srv://murio:AlLLvOzmmLEJq2zv@cluster0.4amgxdq.mongodb.net/?appName=Cluster0')
mydb = myClient['python_test_db_2']
mycol = mydb['customers']
mycol.drop()
