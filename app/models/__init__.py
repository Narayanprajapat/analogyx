import pymongo
from os import getenv

mongo = pymongo.MongoClient(getenv('DATABASE_URL'), connect=False)

database = mongo['analogy']
