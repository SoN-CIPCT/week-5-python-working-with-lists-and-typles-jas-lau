my_list = [1, 2, 3, 4, 5, 6]
print(my_list)
first_two_items = my_list[:2]
print("The first two items in the list are:", first_two_items[0], ",", first_two_items[1])

middle_two_items = my_list[2:4]
print("The middle two items in the list are:", middle_two_items[0], ",", middle_two_items[1])

print("The first and lastitems in the list are:", my_list[0], ",", my_list[5])

menu = ("Sushi", "Onigiri", "Poke", "Sashimi", "Ramen")
print("Original menu:")
for item in menu:
    print(item)

updated_menu = ("Sushi", "Pizza", "Burrito", "Sashimi", "Ramen")
print("\nRevised menu:")
for item in updated_menu:
    print(item)
