from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from pokedex.api import get_pokemon_data, get_pokemon_wiki_image, get_pokemon_wiki_summary


def home(request):
    context = {}
    if "searched_pokemon" in request.POST:
        search_input = request.POST.get('searched_pokemon').lower()
        context['pokemon_name'] = search_input.capitalize()
        try:
            searched_pokemon_data = get_pokemon_data(str_pokemon_name=search_input)
            pokemon_wiki_summary = mark_safe(get_pokemon_wiki_summary(str_pokemon_name=search_input)) #get_wikipedia_summary(search_keywords=search_input)
            pokemon_wiki_image = get_pokemon_wiki_image(str_pokemon_name=search_input) #get_wikipedia_image(search_keywords=search_input)
            dex_id = str(searched_pokemon_data['id'])
            while len(dex_id) < 3:
                dex_id = '0' + dex_id
            else:
                dex_id
            context['id'] = dex_id
            context['type'] = '/'.join([pokemon['type']['name'].capitalize() for pokemon in searched_pokemon_data['types']])
            context['summary'] = pokemon_wiki_summary
            context['image'] = pokemon_wiki_image
        except Exception as e:
            print('Invalid pokemon name. {}'.format(e))


    return render(request, 'pages/home.html', context=context)

 
