import pymongo

class Database(object):
    URI = ['localhost:27017']
    DATABASE = None

    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['currency']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_all(collection):
        return Database.DATABASE[collection].find()

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data)