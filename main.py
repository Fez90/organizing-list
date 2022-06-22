# sort() method sorting list permanently alphabetic order can't be reverted to original order

cars = ['audi', 'bmw', 'ford', 'tesla', 'chevrolet']
cars.sort()
print(cars)

# reverse = True in sort() method change permanently

cars.sort(reverse=True)
print(cars)

# reversed the list
# sorted() function temporarily sorting list and maintains original list

print(sorted(cars))
print(cars)

# reverse() function reversing list permanently can be reversed by using reverse() function second time

cars = ['bmw', 'audi', 'ford','tesla']
print(cars)
cars.reverse()
print(cars)

# finding the lenght of the list using functon len()

len(cars)

#  useful to determine numnber of aliens, the amount of data need to be determined, number of registered users etc
