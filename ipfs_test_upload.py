import requests
import os
from dotenv import load_dotenv
import pprint

# load environmental variable
load_dotenv()

PINATA_JWT_TOKEN=os.getenv('PINATA_JWT_TOKEN')
FILE_PATH = 'commont.txt'

def upload_to_pinata(filepath, jwt_token):
    url="https://api.pinata.cloud/pinning/pinFileToIPFS" #This url should be updated witht the latest node in Gatway tab

    headers = {'Authorization': f'Bearer {jwt_token}'}

    with open(filepath, 'rb') as file:
        response = requests.post(url, files={'file':file}, headers=headers)
        return response.json()

pprint.pprint(upload_to_pinata(FILE_PATH, PINATA_JWT_TOKEN))