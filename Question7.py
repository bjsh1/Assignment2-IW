#7. Create a list of tuples of first name, last name, and age for your friends and colleagues. 
# If you don't know the age, put in None. 
# Calculate the average age, skipping over any None values. 
# Print out each name, followed by old or young if they are above or below the average age.

lists=[('Ram','Dashrat',38),('Laxman','Dashrat',37),('Bhim','Niraula',40),('Sita','Ram',30),('Gita','Shyam',None),('Rita','Hari',28)]

#print(lists[0][2])

sum_age=0
count=0

for num in range(len(lists)):
    
    if lists[num][2]!=None:
        sum_age+=lists[num][2]
        count+=1
print("sum is {} and count is {}".format(sum_age,count))

avg_age=sum_age/count

print("The average age is {}".format(avg_age))