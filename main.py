import requests
import json
from pprint import pprint
intelligence_list = {}

def get_intelligence_hulk():
    url = "https://superheroapi.com/api/2619421814940190/search/hulk"
    response = requests.get(url=url)
    res = response.json()
    intelligence = (res['results'][0]['powerstats']['intelligence'])
    intelligence_list.setdefault('Hulk', intelligence)
    return intelligence

def get_intelligence_captain_america():
    url = "https://superheroapi.com/api/2619421814940190/search/captain_america"
    response = requests.get(url=url)
    res = response.json()
    intelligence = (res['results'][0]['powerstats']['intelligence'])
    intelligence_list.setdefault('Captain America', intelligence)
    return intelligence

def get_intelligence_thanos():
    url = "https://superheroapi.com/api/2619421814940190/search/thanos"
    response = requests.get(url=url)
    res = response.json()
    intelligence = (res['results'][0]['powerstats']['intelligence'])
    intelligence_list.setdefault('Thanos', intelligence)
    return intelligence


get_intelligence_hulk()
get_intelligence_captain_america()
get_intelligence_thanos()

most_int = sorted(intelligence_list.items(), reverse=True)
print(f' У персонажа "{most_int[0][0]}" самый большой интеллект равный {most_int[0][1]}.')
