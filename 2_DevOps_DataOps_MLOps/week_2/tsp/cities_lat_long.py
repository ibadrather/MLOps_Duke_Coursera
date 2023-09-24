import pandas as pd
import geopy

CITIES = [
    "Birmingham",
    "Baltimore",
    "Fort Worth",
    "Miami",
    "San Diego",
    "Denver",
    "Seattle",
    "San Francisco",
    "Knoxville",
    "Boston",
    "Cleveland",
    "Atlanta",
    "Dallas",
    "Houston",
    "Bangor",
    "New York",
    "Raleigh",
    "Chicago",
    "Phoenix",
    "Los Angeles",
]


def get_lat_long_for_a_city(city):
    """Get the latitude and longitude of a city."""
    locator = geopy.geocoders.Nominatim(user_agent="myGeocoder")
    location = locator.geocode(city)
    return location.latitude, location.longitude


def get_lat_long_for_cities(cities):
    """Get the latitude and longitude of a list of cities."""
    lat_long = []
    for city in cities:
        lat_long.append(get_lat_long_for_a_city(city))
    return lat_long


def get_lat_long_cities_df(cities):
    """Get the latitude and longitude of a list of cities in a dataframe."""
    lat_long = get_lat_long_for_cities(cities)
    df = pd.DataFrame(lat_long, columns=["lat", "long"])
    df["city"] = cities

    return df


if __name__ == "__main__":
    df = get_lat_long_cities_df(CITIES)
    print(df.head())

    df.to_csv("cities_lat_long.csv", index=False)
