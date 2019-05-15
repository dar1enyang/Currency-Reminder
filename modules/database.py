import pymongo
import configparser


class Database(object):
    #URI = ['localhost:27017']
    config = configparser.ConfigParser()
    config.read('MLAB.cfg')
    URI = []
    URI.append(config.get("MLAB", "URI"))
    DATABASE = None

    def initialize():
        client = pymongo.MongoClient(Database.URI)
        #Database.DATABASE = client['currency']
        Database.DATABASE = client.get_default_database()

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

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)
