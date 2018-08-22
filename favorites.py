def pretty_print_unordered(to_print):
    for item in to_print:
        print('* ' + str(item))

def pretty_print_ordered(to_print):
    for i, value in enumerate(to_print, 1):
        print(str(i) + ". " + str(value))

favorites = []
more_items = True
while more_items:
    user_input = input("Enter something you like: ")
    if user_input == '':
        more_items = False
    else:
        favorites.append(user_input)

print()
print("Here are all the things you like!")
pretty_print_ordered(favorites)
