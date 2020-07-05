# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. 
# Make more tuples with the corresponding information from your friends and append them to the list. 
# Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name, or age.

tuples = ('Jeremy', 'Zucker', 25)
people = []
people.append(tuples)
print(people)



tuple1 = ('Lauv', 'Lauv', 24)
tuple2 = ('ED', 'Sheeran', 28)
tuple3 = ('Rudy', 'Mancuso', 25)
people = [*people, tuple1, tuple2, tuple3]
print(people)


print(sorted(people, key=lambda x:x[0]))

print(sorted(people, key=lambda x:x[1]))

print(sorted(people, key=lambda x:x[-1]))

print(sorted(people, key=lambda x:(x[0], x[1])))
