# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
options = input("hey what do you want to do Show/Add/Delete or Quit?")
if options == "Show".lower():
    print("ill show you!!!!!")
elif options == "Add".lower():
    print()



#Remove all duplicates from the following list
nums_list = [1, 1, 1, 2, 2, 3, 5, 6, 4, 12, 11, 12, 12, 14, 16, 16, 16, 1, 1, 1, 2, 2]
new_list = []
for x in nums_list:
    if x < 2:
        nums_list.append(x(new_list))

#Out put the intersection of the following the following sets.
set1 = {20, 24, 26, 27}
set2 = {26, 35, 63, 27}
print(set1.intersection(set2))

#Output the difference between the following sets
set3 = {100, 65, 89, 200}
set4 = {65, 103, 54, 200}


new_set = {}
def sets():
    for x in set3:
        if set3 not in set4:
            x.append((new_set))
            return
print(new_set)