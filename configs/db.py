import os

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv('../.env')
db = MongoClient(host=os.getenv('mongodb_host'),
                 port=os.getenv('mongodb_port'),
                 username=os.getenv('mongodb_root_username'),
                 password=os.getenv('mongodb_root_password'))[os.getenv('mongodb_db_name')]