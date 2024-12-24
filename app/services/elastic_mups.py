import folium
import os

from app.services.country_cordinates import get_country_coordinates


elastic_map_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'elastic.html')


def elastic_search_to_mup(search_list):
    israel_location = [31.0461, 34.8516]
    map = folium.Map(location=israel_location)

    if len(search_list) < 1:
        folium.Marker(israel_location,
                      popup='no results').add_to(map)

    for index in search_list:
        source = index['_source']
        coordinates = get_country_coordinates(source['country'])
        if coordinates and coordinates[0] and coordinates[1]:
            folium.Marker(coordinates,
                      popup=f'title: {source['title']}, \n date: {source['date']},').add_to(map)
    map.save(elastic_map_path)
