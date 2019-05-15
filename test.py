from modules.database import Database

Database.initialize()
Database.insert(collection="test", data={"name": "Kevin", "age": "20"})
Database.insert(collection="test", data={"name": "Leo", "age": "20"})
# print(Database.find_one(collection="test", query={"name": "Kevin"}))
# print(Database.find(collection="test", query={"age": "20"})[0])
# print(Database.find_all(collection="test")[0])