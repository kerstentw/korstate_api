import sqlite3
import csv

class sqlHandler(object):
    def __init__(self, connect):
        conStr = "./dumps/real_estate.db"
        self.conn_obj = sqlite3.connect(conStr)
        self.cursor = self.conn_ob.cursor()

    def createTable(self,table_name):
        sqlQuery = """CREATE TABLE `listings` (
                      Name varchar(200)
        );"""

    def insertDict(self,_dict):
        pass


class csvHandler(object):

    def __init__(self,_fieldnames,_filename):
        """
        __init__(list, str)

        Inserts a fieldname list and a csv file string into an instance of a
        csvHandler object.
        """
        self.csv_file = open(_filename,"w")
        self.writer = csv.DictWriter(self.csv_file, fieldnames = _fieldnames)

    def insertDict(self, _dict):
        self.writer.writerow(_dict)

    def finalize(self):
        self.writer.close()
