"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'name': 'Liam Thomas Hull',
        'student ID': '10304520',
        'pizza toppings': [
            'Pineapple',
            'Ham',
            'Bacon'
        ],
        'movies': [
            {
                'title': 'Rio',
                'genre': 'Comedy'
            },
            {
                'title': 'Atlantis: The Lost Empire',
                'genre': 'Adventure'
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['soylent green', 'racht'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'the lord of the rings', 'fantasy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    first_name = my_info['name'].split()
    print(f"My name is {my_info['name']}, but you can call me Sir {first_name[0]}")
    # Print sentence containing student ID
    print(f"\nMy Fleming student ID is {my_info['student ID']}.")

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print("\nMy favourite pizza toppings are:")
    # Print bullet list of favourite pizza toppings
    for toppings in my_info['pizza toppings']:
        print(f"- {toppings}")

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['pizza toppings'].extend(toppings)
    # Convert all pizza toppings to lowercase
    for i, toppings in enumerate(my_info['pizza toppings']):
        my_info['pizza toppings'][i] = toppings.lower()
    # Sort toppings list alphabetically
    my_info['pizza toppings'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    new_movie = {
        'title': title,
        'genre': genre
    }
    my_info['movies'].append(new_movie)

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    print('\nI like to watch ', end = '')
    for i, movie in enumerate(my_info['movies']):
        if i < len(my_info['movies']) - 1:
            print(movie['genre'].title(), end = ', ')
        else:
            print('and ' + movie['genre'].title(), end = '.')

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    print('\n\nSome of my favourite movies are ', end = "")
    x = 0
    while x < len(movie_list):
        movie = movie_list[x]
        title = movie['title'].title()
        if x < len(movie_list) - 1:
            print(f"{title}", end = ', ')
        else:
            print(f"and {title}!")
        x = x + 1
    #titles = [title['title'] for title in movie_list['movies']]
    #print(', '.join(titles), end='.')

if __name__ == '__main__':
    main()