
# Given a dictionary of airline routes, find and return an array of airlines the represents the
# route from one airline to another


def find_airline_route(airlines, starting_point, ending_point):

    route = [starting_point]

    for i in range(len(airlines)):
        if route[-1] == ending_point:
            break
        route.append(airlines[route[-1]])

    return route


if __name__ == '__main__':
    airlines = {
        'SEA': 'PDX',
        'RAP': 'MSP',
        'PDX': 'BOI',
        'BOI': 'BIL',
        'MSP': 'MKE',
        'BIL': 'RAP',
        'MKE': 'CMH'
    }
    starting_point = 'SEA'
    ending_point = 'BIL'
    print(find_airline_route(airlines, starting_point, ending_point))
