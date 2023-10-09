import os
from os.path import join,dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

DBIP = os.environ.get("Database_IP")
USN = os.environ.get("sqlUserName")
PWD = os.environ.get("sqlPass")
openaiKey = os.environ.get("openaiKey")