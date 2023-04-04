# # Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.
# noun = input("please enter a noun")
# verb = input("please enter a verb")
# adjective = input("please enter a adjective")
# print(f"hey where do you like visiting {noun} what do you like to do {verb} what do you do in those games {adjective}")

# #Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
# age = int(input("hey what is your age?"))
# if age < 18:
#     print("youre a kid still!")
# elif age <= 65:
#     print("youre an adult")
# else:
#     print("your'e a seniour!")   



# #Take in a number from a user input output the number squared.
# number = int(input("hey please input a number?"))
# print(number ** 2)



# #Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False
# #word1 = "panini"
# #word2 = "bulbasaur"
# #word3 = "pie"
# #word4 = "dolphin"
# #word5 = "dog"


word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

# answers = len(word1), len(word2), len(word3), len(word4), len(word5)
# print(answers)
# if answers < 5:
#     print(answers)


def wordeval(word):
    if len(word) >= 5:
        return True
    else:
        return False

print(wordeval("Fabian"))