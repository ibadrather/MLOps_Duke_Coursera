from calculate_shortest_distance import calculate_distance_between_cities, CITIES_df
import pandas as pd
import os

os.system("clear")

CITIES_df = pd.read_csv(
    "/home/ibad/Desktop/MLOps_Duke_Coursera/2_DevOps_DataOps_MLOps/week_2/tsp/cities_lat_long.csv"
)
distance_between_cities = calculate_distance_between_cities(CITIES_df)

cities_list = CITIES_df["city"].values.tolist()


def get_next_possible_city_with_shortest_distance(
    origin_city, cities_list, distance_between_cities, cities_visited
):
    shortest_distance = 1e4
    next_city = None

    for city in cities_list:
        if city not in cities_visited and city != origin_city:
            distance = distance_between_cities[(origin_city, city)]

            if distance < shortest_distance:
                shortest_distance = distance
                next_city = city

    return next_city, shortest_distance


def calculate_shortest_path_and_distance_from_starting_city(
    starting_city, cities_list, distance_between_cities
):
    cities_visited = [starting_city]

    total_distance = 0

    current_city = starting_city

    for city in cities_list:
        if city not in cities_visited:
            (
                next_city,
                shortest_distance,
            ) = get_next_possible_city_with_shortest_distance(
                current_city, cities_list, distance_between_cities, cities_visited
            )
            total_distance += shortest_distance

            cities_visited.append(next_city)

            current_city = next_city

    return total_distance, cities_visited


def tsp(cities_list, distance_between_cities):
    shortest_distance_overall = 1e10
    shortest_route_overall = []

    # I want to see what is the best city to start with and what is the shortest distance
    for starting_city in cities_list:
        (
            shortest_distance,
            shortest_route,
        ) = calculate_shortest_path_and_distance_from_starting_city(
            starting_city, cities_list, distance_between_cities
        )

        if shortest_distance < shortest_distance_overall:
            shortest_distance_overall = shortest_distance
            shortest_route_overall = shortest_route

    return shortest_distance_overall, shortest_route_overall


shortest_distance, shortest_route = tsp(cities_list, distance_between_cities)


print("Shortest distance: ", shortest_distance)
print("Cities visited: ", shortest_route)

assert len(shortest_route) == len(cities_list)
