#Invite people for dinner
Guests_list = ['abby', 'bonnie', 'cathy', 'david', 'ethan', 'fred', 'giga']
print(f"Welcome to the dinner, {Guests_list[0].title()}")
print(f"Welcome to the dinner, {Guests_list[1].title()}")
print(f"Welcome to the dinner, {Guests_list[2].title()}")
print(f"Welcome to the dinner, {Guests_list[3].title()}")
print(f"Welcome to the dinner, {Guests_list[4].title()}")
print(f"Welcome to the dinner, {Guests_list[5].title()}")
print(f"Welcome to the dinner, {Guests_list[6].title()}")

#some guests are not able to make it so removing the guest from the list, welcome the rest
Guests_cant_come = Guests_list.pop()
print(f"{Guests_cant_come.title()} was not able to come.")
print(f"The rest, {[guest.title() for guest in Guests_list]} are welcome.")

#find a new table for new guests, a new invitation for all of the guests and find out the length
Guests_list.insert(0, 'iris')
Guests_list.insert(3, 'Kwiyomi')
Guests_list.append('Taylor')
print(f"Welcome to the dinner,\n\t{[guest.title() for guest in Guests_list]}")
len(Guests_list)
print(len(Guests_list))

#List the place i want to visit and sort the list without changing it
places_visit = ['paris', 'london', 'alaska', 'germany', 'italy']
print([place.title() for place in places_visit])
print(sorted([place.title() for place in places_visit]))
print(f"this is the in order list, {sorted([place.title() for place in places_visit])}")
print(f"this is the original order, {[place.title() for place in places_visit]}")

#use sorted() to print my list in reverse-alphabetical order without changing the order of the original list
print(f"the reverse version of the list is: {sorted([place.title() for place in places_visit], reverse=True)}")
print(f"the original version of the list is {places_visit}")

#use reverse() to change the order of your list print the list to show that its order has changed
print(places_visit)
places_visit.reverse()
print(places_visit)
places_visit.reverse()
print(places_visit)

#use sort() to change list and reverse
print(f"\n{places_visit}")
places_visit.sort()
print(places_visit)
places_visit.sort(reverse=True)
print(places_visit)
