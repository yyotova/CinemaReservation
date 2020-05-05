def menu():
    menu = f'''
    [1] show movies
    [2] show movie projections <movie_id> [<date>]
    [3] make reservation
    [4] cancel reservation <name>
    [5] exit
    [6] help
    '''
    print(menu)
    return input("Choise")
