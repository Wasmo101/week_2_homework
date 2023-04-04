#1Using the given list, print out a filtered version of the list with only the numbers that are less than ten
alist = [1,11,14,5,8,9]
new_numbers = []
for numbers in alist:
    if numbers < 10:
        new_numbers.append(numbers)
    else:
        pass
print(new_numbers)        



# #2Merge and sort the two lists below Hint: You can use the .sort() method
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
def merge_sort(l_1, l_2):
    new_list = l_1 [:] #makes a copy of a list
    for item in l_2:
        if item not in l_1:   #this gets rid of dups.
            new_list.append(item)
    new_list.sort()
    return new_list
print(merge_sort(l_1, l_2))




# #quare every number from 1 to 15
# x = 1 ** 2
# while x< 16:
#     print(x ** 2)
def sqared_list():
    while 1 <= 16:
        sqared_list(1 ** 2)
        break    
print(sqared_list)




# #4Using List Comprehension and the given list, print out a filtered list with 
# #only the names that start with the letter 'a'. 
# #The names in the outputted list should be title cased and have no whitespace.

# names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
# new_list = ()
# for x in names_list:
#     if 'a' in x:
#         names_list.append(new_list)

# #expected output = ['Amy', 'Alex']

names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
new_list = ()
for x in names_list:
    if 'a' in x:
         names_list.append(new_list.tittle().strip())


# #5Print all Prime numbers from 1 to 100
