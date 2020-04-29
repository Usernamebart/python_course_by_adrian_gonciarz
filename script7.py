# #point1 jest zmienialny, point2 nie jest zmianialny (inmutable)
#
# point1 = [3, 10] # lista
# point2 = (3, 10) # tuple
#
# point1[0] = 13
# # point2[0] = 13 - to nie pójdzie, error będzie
#
# names = ['Jan', 'Kasia', 'Jarek']
# #tablica z niezmienialną zawartością
# users = [
#     (459, 'a1@example.com', 'password1',),
#     (460, 'a1@example.com', 'password1',),
#     (461, 'a1@example.com', 'password1',),
#
# ]
#
# t = (2, )
# print(type(t))
#
# def user(email, password='haslo123'):
#     print(f'This is user with {email} and password {password}')
#
# user('a@example.com', 'nowehaslo456')
#
# def user(email, password='haslo123', user_type='client'):
#     print(f'This is user type {user_type} with {email} and password {password}')
#
# user('a@example.com', user_type='admin')
#
# def describe_dog(name, race, owner='me'):
#     #owner default 'me'
#     print(f'This is dog {name} of race {race} and the owner is {owner}')
#
# describe_dog('Morgan', 'German Sheppard')
# describe_dog('Alex', 'German Sheppard')
# describe_dog('Zet', 'German Sheppard', owner='Ja')
#
# print(1, 23, 4, 5, 6, 7, 7, 7)
#
# def game(game_name, *players):
#     print(f'Game name: {game_name}')
#     #print(f'Game players: {players}')
#     for idx, player in enumerate(players):
#         print(f'Player number {idx+1}: {player}')
#
#         #alternatywnie
#         #print(*[f"player number {str(i)}: {p}\n" for i, p in enumerate(players)])
#
# game('Poker', 'Janek', 'Basia', 'Lucy', 'Zenek', 'Ann', 'Andrew')
#
# a = {"foo": 1, "bar": 2}
# print(a['foo'])
# print(a.get('bar'))
# #print(a['foo1'])
# print(a.get('bar1'))
# print(a.get('bar1', 123))
#
# def car(colour, manufacturer, **kwargs): #kwargs -> pseudosłownik
#     print(f'The car is {colour} and is produced by {manufacturer}')
#     if kwargs.get('max_speed'):
#         print(f"Car max speed is {kwargs.get('max_speed')}")
#     gearbox = kwargs.get('gearbox', 'manual') #przyjmuje defaultowo gearbox jako manual, chyba że w car() /line66/ podamy gearbox
#     print(f'Gearbox type is {gearbox}')
#
# car('red', 'Honda', max_speed=300, gearbox='automatic')
# car('red', 'Honda', max_speed=300,)

