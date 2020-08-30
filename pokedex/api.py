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


# Unused due to inability to get all pokemon from wikipedia e.g ivysaur
def get_wikipedia_image(search_keywords):
    response = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/{}'.format(search_keywords))
    image_link = response.json()['originalimage']['source']
    return image_link


def get_pokemon_wiki_page(str_pokemon_name):
    response = requests.get('https://pokemon.fandom.com/api.php?action=query&titles={}&format=json'.format(str_pokemon_name))
    page = next(iter(response.json()['query']['pages']))

    return int(page)


def get_pokemon_wiki_image(str_pokemon_name):
    page_id = get_pokemon_wiki_page(str_pokemon_name)
    response = requests.get('https://pokemon.fandom.com/api/v1/Articles/Details?ids={}'.format(page_id))
    image_url = response.json()['items'][str(page_id)]['thumbnail']

    return image_url


def get_pokemon_wiki_summary(str_pokemon_name):
    page_id = get_pokemon_wiki_page(str_pokemon_name)
    response = requests.get('https://pokemon.fandom.com/api/v1/Articles/AsSimpleJson?id={}'.format(page_id))
    ls_physiology_text = [text['content'][0]['text'] for text in response.json()['sections'] if text['title'] in ['Physiology', 'Characteristics', 'Behavior']]
    physiology_text = '<br><br>'.join(ls_physiology_text)
    return physiology_text
    
