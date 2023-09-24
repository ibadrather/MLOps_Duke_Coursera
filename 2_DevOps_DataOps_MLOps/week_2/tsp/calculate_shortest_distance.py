import pandas as pd
from geopy import distance


CITIES_df = pd.read_csv(
    "/home/ibad/Desktop/MLOps_Duke_Coursera/2_DevOps_DataOps_MLOps/week_2/tsp/cities_lat_long.csv"
)


def calculate_distance_between_cities(cities_df):
    cities_list = cities_df["city"].values.tolist()

    distances_betwen_cities = {}

    for origin_city in cities_list:
        for destination_city in cities_list:
            if origin_city == destination_city:
                continue
            else:
                origin_city_lat = CITIES_df[CITIES_df["city"] == origin_city][
                    "lat"
                ].values[0]
                origin_city_long = CITIES_df[CITIES_df["city"] == origin_city][
                    "long"
                ].values[0]
                destination_city_lat = CITIES_df[CITIES_df["city"] == destination_city][
                    "lat"
                ].values[0]
                destination_city_long = CITIES_df[
                    CITIES_df["city"] == destination_city
                ]["long"].values[0]

                origin = (origin_city_lat, origin_city_long)
                destination = (destination_city_lat, destination_city_long)

                distance_calculated = distance.distance(origin, destination).miles

                distances_betwen_cities[
                    (origin_city, destination_city)
                ] = distance_calculated

    return distances_betwen_cities


if __name__ == "__main__":
    import os

    os.system("clear")

    distances_betwen_cities = calculate_distance_between_cities(CITIES_df)

    print(distances_betwen_cities)
