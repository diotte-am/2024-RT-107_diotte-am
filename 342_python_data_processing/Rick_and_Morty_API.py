import requests
import json
import pandas as pd

'''
Requesting data from the Rick and Morty API
'''

base = "https://rickandmortyapi.com/api/"
char_endpoint = "character/"
loc_endpoint = "location/"
epi_endpoint = "episode/"

# save to file

def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()

def save_to_file(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    char_dict = []
    for item in response['results']:
        char = {'name' : item['name'], 
                'no_ep' : len(item['episode'])}
        char_dict.append(char)
    return char_dict


data = main_request(base, char_endpoint, 1)
save_to_file(data)
main_list = []
for x in range (1, get_pages(data) + 1):
    main_list.extend(parse_json(main_request(base, char_endpoint, x)))

print(main_list)

df = pd.DataFrame(main_list)