# CinemaReservation
This is a reservation system that will allow you to make reservations for
the newest movies in the cinema. You can register into the system with a
valid email and password. Without registration, you can only see the
movies and projections.

## Requirements
```pip install -r requirements.txt```

## Explanation
You can run the program with: 
* ``` python3 main.py build``` - it will create the data base models
* ```python3 main.py start``` - run the app

There is a welcome menu like this:
```
Welcome to HackCinema!

Choose a command:
  1 - log in
  2 - sign up
  3 - menu
  Input: 
```
So, you can choose to make a registration, to log in or just to look the menu.

But if your session is not over, when you start the app, it will show you:
```
Welcome to HackCinema!

Welcome anni@gmail.com:
        [1] Continue
        [2] Log out

```

This is the menu:
```
	[1] show movies
    [2] show movie projections <movie_id> [<date>]
    [3] make reservation
    [4] cancel reservation
    [5] exit
    [6] help

```
But if you try to make a reservation without log in, it will show you 
```
You have to log in to make reservation!
Choose a command:
  1 - log in
  2 - sign up
  3 - menu
  Input: 
```