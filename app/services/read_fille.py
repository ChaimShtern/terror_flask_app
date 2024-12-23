import os
import pandas as pd

countries_and_coordinates_path = os.path.join(os.path.dirname(__file__), '..', 'data',
                                               'countries_codes_and_coordinates.csv')


def find_coordinates_in_csv(file_path, country_name):
    try:
        countries = pd.read_csv(file_path, encoding="utf-8").filter(
            items=["Country", 'Latitude (average)', 'Longitude (average)']).to_dict(orient="records")
        countries_with_coordinates = {country['Country']: {**country} for country in countries}
        return countries_with_coordinates.get(country_name)
    except UnicodeDecodeError:
        return pd.read_csv(file_path, encoding="latin1").to_dict(orient="records")