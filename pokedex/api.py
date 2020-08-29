import requests
import json


def get_list_all_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=2000')
    dc_all_pokemon_response = response.json()
    ls_all_pokemon_names = [pokemon['name'] for pokemon in dc_all_pokemon_response['results']]
    return ls_all_pokemon_names


def get_total_number_pokemon():
    return len(get_list_all_pokemon())


def get_pokemon_data(str_pokemon_name):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(str_pokemon_name))
    return response.json()


def get_wikipedia_summary(search_keywords):
    response = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/{}'.format(search_keywords))
    summary_data = response.json()['extract']
    return summary_data


def get_wikipedia_image(search_keywords):
    response = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/{}'.format(search_keywords))
    image_link = response.json()['originalimage']['source']
    return image_link
