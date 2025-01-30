# 1. Given a list of tuples where each tuple contains a name and a score, 
# create a new list that contains the names of students who scored above 80.
# Example input: [('Mike', 75), ('Joe', 90), ('Beck', 85)]
# Expected output: ['Joe', 'Beck']

names = [('Mike', 75), ('Joe', 90), ('Beck', 85)]
age = [
name for name,age  in names if age > 80   ]
print(age)


# 2. Given a tuple with several lists inside it, 
# write a function to return the list with the maximum sum of its elements.
# Example input: ([1, 2], [3, 4], [5, 6, 7])
# Expected output: [5, 6, 7]

numbers = ([1, 2], [3, 4], [5, 6, 7])
maxx = max(numbers, key=sum)
print(maxx)


# 3. Given a list of tuples with names and ages, 
# return a list of names where the age is greater than 30 and less than 50.
# Example input: [('Mike', 25), ('Joe', 31), ('Beck', 40)]
# Expected output: ['Joe', 'Beck']


age = [('Mike', 25), ('Joe', 31), ('Beck', 40)]
newage = [
    name for name, old in age  if old >= 30 and old <=50
]

print(newage)



# 4. Given a list of integers, 
# write a function to return a list of tuples where the first element is the number 
# and the second is 'Even' or 'Odd' depending on whether the number is even or odd.
# Example input: [1, 2, 3, 4]
# Expected output: [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even')]

numbers = [1, 2, 3, 4]
name = list(map(lambda x: ( x ,'Even' if x % 2 == 0 else  'Odd' ), numbers))
print(name)


# 5. Given a list of tuples containing a string and an integer, 
# write a function that returns a tuple of the string with the largest length 
# and its corresponding integer. If two strings have the same length, 
# choose the one with the larger integer.
# Example input: [('apple', 5), ('banana', 4), ('cherry', 6)]
# Expected output: ('apple', 5)



mylist = [('apple', 5), ('banana', 4), ('cherry', 6)]
result = max(mylist ,key=lambda x : x[0] and x[1] )
print(result)




# 6. Given a list of tuples where each tuple contains a date (as a string in 'YYYY-MM-DD' format) and an event, 
# return the list of events in the order of the most recent dates.
# Example input: [('2024-12-01', 'Event A'), ('2025-01-01', 'Event B')]
# Expected output: [('2025-01-01', 'Event B'), ('2024-12-01', 'Event A')]

mylist = [('2024-12-01', 'Event A'), ('2025-01-01', 'Event B')]
result = sorted(mylist, key=lambda x: x[0], reverse=True)
print(result)


# 7. Given a list of tuples where each tuple contains a name and a score, 
# return the highest score and the corresponding name.
# Example input: [('Mike', 75), ('Joe', 90), ('Beck', 85)]
# Expected output: ('Joe', 90)



mylist = [('Mike', 75), ('Joe', 90), ('Beck', 85)]
result = max(mylist, key=lambda x: x[1])
print(result)




# 8. Given a list of tuples where each tuple contains a product name and its price, 
# write a function to return a list of products whose price is between 50 and 100.
# Example input: [('product1', 45), ('product2', 60), ('product3', 120)]
# Expected output: [('product2', 60)]



mylist =  [('product1', 45), ('product2', 60), ('product3', 120)]
result = [ (i,a) for i, a in mylist if 50 <= a <= 100 ]
print(result)



# 9. Given a list of tuples where each tuple contains a person's name and their age, 
# return the name of the oldest person in the list.
# Example input: [('Mike', 25), ('Joe', 31), ('Beck', 40)]
# Expected output: 'Beck'
 


mylist = [('Mike', 25), ('Joe', 31), ('Beck', 40)]
result = max( mylist,key=lambda x: x[1])
print(result[0])



# 10. Given a list of tuples containing a student's name and their grades in multiple subjects, 
# return the names of students who have an average grade greater than 80.
# Example input: [('Mike', [85, 75, 90]), ('Joe', [70, 80, 60])]
# Expected output: ['Mike']

mylist = [('Mike', [85, 75, 90]), ('Joe', [70, 80, 60])]
result = list(filter(lambda x : sum(x[1])/len(x[1])> 80 ,mylist))
print(result[0][0])