from connection import connections
import requests
import time
import os
import json
from dotenv import load_dotenv
load_dotenv()

print(str(os.getenv("authToken")))