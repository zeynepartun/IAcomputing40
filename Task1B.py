# Task 1B written by Zeynep Artun

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key


def print_distance(item):
    print("Station Name: {}   Distance: {}".format(item[0], item[1]))
    
def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()



    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    result = stations_by_distance(stations, (52.2053, 0.1218))
    sorted_result = sorted_by_key(result, 1)
    first_10 = sorted_result[:10]
    last_10 = sorted_result[-10:]
    print("Closest Stations to Camrbidge City Centre\n")
    for i in first_10:
        print_distance(i)
    print("\nFurthest Stations to Cambridge City Centre\n")
    for i in last_10:
        print_distance(i)


    

    # # Display data from 3 stations:
    # for station in stations:
    #     if station.name in [
    #             'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge'
    #     ]:
            # print(station)



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IB Flood Warning System ***")
    run()




