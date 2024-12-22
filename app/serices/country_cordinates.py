from app.serices.read_fille import find_coordinates_in_csv, countries_and_coordinates_path


def get_country_coordinates(country_name):
    country = find_coordinates_in_csv(countries_and_coordinates_path, country_name)
    if country:
        return [float(country["Longitude (average)"].split('"')[1]),
                float(country["Longitude (average)"].split('"')[1])]
