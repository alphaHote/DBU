import pymongo as mgbd

client=mgbd.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['ouvrier']
information= mydb.table1

# rec=[
#     {
#         "nom" : "hnaoui",
#         "prenom" : "yassine",
#         "age": 80,
#         "sex": "bogosse",
#         "stage" : "lw7ch"
#     }
# ]

# information.insert_many(rec)

# for name in mydb.list_collection_names():
#     print(name)

collection=mydb["table1"]

# for x in collection.find({}): #, {"_id":0, "coursename": 1, "price": 1 }):
#     print(x)

for x in collection.find({}, {"nom": 1, "prenom": 1 }):
    print(x["nom"],x["prenom"])