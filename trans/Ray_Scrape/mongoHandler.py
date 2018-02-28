from pymongo import MongoClient
import datetime
import pprint

#ToDO Add index queries and test performance
#ToDo::: Add better error handling and return keys

class MongoHandler(object):
    def __init__(self, conn_string = None, db_name =  None, set_collection = None):
        self.conn_string = conn_string
        self.client = MongoClient(self.conn_string) #Composition style
        self.db = self.client[db_name]
        self.set_collection = set_collection

    def processBSONKey(self,_key):
        for char in _key:
            if char.isalpha() == False:
                _key = _key.replace(char, " ")

        return _key

    def createIndexOn(self,_collection,_ref):
        self.db[_collection].ensure_index(_ref, unique = True)
        return True

    def connectToMongoInstance(self,conn_string = None):
        if conn_string == None:
            self.client = MongoClient()

        self.conn_string = conn_string
        self.client = MongoClient(self.conn_string)

    def setCollection(self, collection_name):
        self.set_collection = collection_name

    def connectToDatabase(self, db_name):
        self.db = self.client[db_name]

    def findOne(self,query_dict, collection_name = None):
        if collection_name == None:
            collection_name = self.set_collection

        return self.db[collection_name].find_one((query_dict))

    def findMany(self, query_dict, projection = "", collection_name = None):
        if collection_name == None:
            collection_name = self.set_collection

        return self.db[collection_name].find(query_dict, projection)


    def queryDatabase(self):
        pass

    def queryCollection(self):
        pass

    def insertDocument(self,collection_name = None, dict_to_insert = None, date_insert = True):
        """Inserts a datetime post then places into DB"""
        if not collection_name and set_collection: collection_name = self.set_collection

        if date_insert == True:
            dict_to_insert["savedDate"] = datetime.datetime.utcnow()


        _id = self.db[collection_name].insert_one(dict_to_insert)

        return _id

    def insertManyDocuments(self,collection_name = None, list_to_insert = None, date_insert = True):
        if not collection_name and set_collection: collection_name = self.set_collection
        print("FROM DATABASE HANDLER::: ADDING %s to %s" % (type(list_to_insert), collection_name))

        _id = self.db[collection_name].insert_many(iter(list_to_insert))


    def findOneDocument(self, searchDict):
        """If search Dictionary is None will, find last insert """
        pprint.pprint(self.db[self.set_collection].find_one(searchDict))

    def findDocumentByID(self, _id):
        pprint.pprint()
