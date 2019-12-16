import pymongo

dbClient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = dbClient["MapsaBootCamp"]

mycol = mydb['Msg']

# myChats = [{"_id": 1, "sender": "ashkan", "receiver": "ghasem", "msg": "nokaram!"},
#            {"_id": 2, "sender": "ashkan", "receiver": "negar", "msg": "eyval!"},
#            {"_id": 3, "sender": "ashkan", "receiver": "arash", "msg": "ghor nazan!"},
#            {"_id": 4, "sender": "ashkan", "receiver": "saedeh", "msg": "ishala tashkil misheh!"}, ]

# mycol.delete_one({"receiver": "arash"})

# print(mycol.count({"sender": "ashkan"}))

mycol.find({"receiver"})
for i in mycol.find():
    print(i)