import json
import pandas as pd 
import requests
import sys 
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# auto-clear terminal before every run
os.system('cls')

load_dotenv()

API_KEY = os.getenv("API_KEY")

r = requests.get(f"https://cricket.sportmonks.com/api/v2.0/countries?api_token={API_KEY}&include=leagues,")

if r.status_code == 200:
    data = r.json()
    print(json.dumps(data, indent=2))
