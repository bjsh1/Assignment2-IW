#4. Create a list. Append the names of your colleagues and friends to it. 
# Has the id of the list changed? Sort the list. 
# What is the first item onthe list? What is the second item on the list?

friends=['ram','hari','sita','rawan','hanuman','lakshman']
before=id(friends)

friend2=['kalika','dwarika','kanika'] 
friends.extend(friend2) #adding more friends

after=id(friends)

if before==after:
    print("Theres no change in the id's of list before and after appending")
else:
    print("Theres change") 


friends.sort() #sorting the lists

first_element=friends[0]

print("First item in the list is: '{}' ".format(first_element))

second_element=friends[1]
print("Second item in the list is: '{}' ".format(second_element))
