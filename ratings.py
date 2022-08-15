"""Restaurant rating lister."""


def restaurant_ratings(text_file):

    restaurant_ratings_dict = {}

    restaurant_ratings_file = open(text_file)

    for line in restaurant_ratings_file:
        line = line.rstrip()
        restaurant_rating = line.split(':')
        name = restaurant_rating[0]
        rating = restaurant_rating[1]
        restaurant_ratings_dict[name] = rating
        sorted_list = sorted(restaurant_ratings_dict)
        # for item in sorted_list:

    for item in sorted_list:
        for rest_name, rest_rating in restaurant_ratings_dict.items():
            if rest_name == item:
                print(f'{rest_name} is rated at {rest_rating}.')


restaurant_ratings('scores.txt')
