import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["Msg"]

mydict = {"sender" : "negar", "recieve" : "nasim" , "msg" : "Chakeram"}
# mydict1 = {"ashkan" : 20, "javad" : 15}

mycol.insert_one(mydict)
# mycol.insert_one(mydict)

print(myclient.list_database_names())
for i in myclient.list_database_names():
    if i == 'mydatabase':
        print("Nokaram")

# mycol.remove()

for i in mycol.find():
    print(i)