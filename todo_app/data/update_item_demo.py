import requests
import dotenv
import os
dotenv.load_dotenv()

reqUrl = f"https://trello-proxy.azure-api.net/1/cards/65958f186f3d72ec16de8dd3"

query_params = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "idList": os.getenv("TRELLO_DONE_LIST_ID"),
    
}


response = requests.put(reqUrl, params = query_params)

print(response.text)