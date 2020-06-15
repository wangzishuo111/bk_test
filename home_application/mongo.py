import pymongo
class MongodbClient(object):
    def __init__(self, host, port, db, table, user, passwd):
        self.client = pymongo.MongoClient(host=host, port=port)
        self.auth = self.client['admin']
        self.auth.authenticate(user, passwd)
        self.db = self.client.get_database(db)
        self.collection = self.db.get_collection(table)

    def insert(self, item, table=None):
        if table != None:
            collection = self.db.get_collection(table)
            return collection.insert(item)
        else:
            return self.collection.insert(item)

    def get_one(self, query, table=None):
        if table != None:
            collection = self.db.get_collection(table)
            ret = collection.find(query)
            for i in ret:
                return i
        else:
            ret = self.collection.find(query)
            for i in ret:
                return i

    def get_all(self, table=None):
        list_all = []
        if table != None:
            collection = self.db.get_collection(table)
            ret = collection.find()
            for i in ret:
                list_all.append(i)
            return list_all
        else:
            ret = self.collection.find()
            for i in ret:
                list_all.append(i)
            return list_all



if __name__ == '__main__':
    db = MongodbClient('10.0.11.148', 27017, 'cmdb', 'cc_HostBase','root', 'eVmA_GTjy6FYJh5HbelU')
