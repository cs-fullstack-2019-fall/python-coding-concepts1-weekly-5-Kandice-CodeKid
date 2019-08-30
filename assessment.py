### Problem 1:
# Ask a user for the year they were born by calculating their age. Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”

# ## Create a variable to save the user birth year
# bornYear = int(input("Enter the year that you were born: "))
# ## create a variable to save current year (-) the birth year
# currentAge = (2019 - bornYear)
# ## print the current age of person
# print(f'You are {currentAge} years old')

############################################################################
### Problem 2:
# Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”

## create an input that asks the user to enter some data that will return a string.
# userData = input("Enter a word")
# currentNames = ['Kenn', 'Kevin', 'Erin','Autumn']
# if userData == currentNames:
#     print(f'Hello Teacher')
# else:
#     print(f'Hello student')
############################################################################################


### Problem 3:
# Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.


# ## create a variable to hold the user negative number input
# negUser = int(input("Enter a negative number"))
# # I used a for loop and range to count to the user's number. Given was start from 7 and count down to the user's number at intervals of 1. User number -1, to include the user number
# for x in range(7, negUser-1,-1):
#     ## Print the count 7 down to negUser's number
#     print(x)

### Problem 4:
# Ask the user to enter a number between -10 to -5. If their input is not between the two numbers ask them to do it again until they get it right. Afterward they print the correct number, print "Good job"

# userNum = int(input("enter a number between -10 and -5:  "))
# while userNum >= -10 and userNum <= -5:
#     userNum = ''
#     print(f'Good job')
# else:
#     print('Try again')
#     userNum = int(input("enter a number between -10 and -5:  "))


### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.

# squad = ["One", "Two", "Three", "Four", "Five"]
# print(squad[::-1])


### Problem 6:
# Create a function that will have the string firstName as a parameter. In the function ask the user for their last name. Print "Hello [FIRST & LAST NAME]" in the function. Call that function

# def stringFunc(Kandice):
#     lastName = input('Enter your last name')
#     print(f'Hello  {lastName}')
#
# stringFunc('Kandice')


### Problem 7:
# Create the class Books with name, rating, genre, and author properties/attributes. Create a class method that will change the rating of the book. Outside of the class, create three objects of the class Book and put them in an array. Lastly, USING THE ARRAY print only the names of the books using any method we’ve learned in class.

# class Books:
#     def __init__(self,name, rating, genre, author):
#         self.name = name
#         self.rating = rating
#         self. genre = genre
#         self . author = author
#     def __str__(self,book_rating):
#         self.book_rating = book_rating
#
#
#
# def prob7():
#     book1 = Books('Bridge to Terrabithia', 5, 'Fiction', 'Jane Doe')
#     book2 = Books('Asata', 8, 'Nonfiction', 'Asata Shakur')
#     book3 = Books('Ask Again, Yes', 6, 'Fiction', 'John Doe')
#     book_collection = [book1, book2, book3]
#     print(book_collection.book1[0])
# prob7()


### Problem 8:
# Create a function that asks the user to enter a number. If the number is between and include -50 and 5, return "Funds too low". If the number is between 5 and 50, return “You should add more funds.” If the number is more than 50, return “Just enough.”
# def prob8():
#     userInput = int(input("Enter a number  "))
#
#     if userInput >= -50 and userInput <= 5:
#         return ('funds too low')
#     elif userInput >= 5 and userInput <= 50:
#         return ('You should add more money')
#     elif userInput > 50:
#         return (f'Just enough')


# prob8()

### Problem 9:
# Ask the user for a positive number. Create an empty array and starting from zero, add each number by 1 into the array. Print EACH ELEMENT of the array.

# userNum = int(input('Enter a positive number'))
# posArray = []
# posArray.append(userNum)
# print(posArray)



### Problem 10:
# Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property. Include a method that will print each attribute/property. Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.

pet_list = ['ball','food', 'bell']

class Pet:
    def __init__(self,type,breed):
        self.type = type
        self.breed = breed
    def __str__(self):
        return (f'type: {self.type}  breed: {self.breed}')


def prob10():
    newPet1= Pet('cat','siamese')
    newPet2 = Pet('dog,','bulldog')
    print(newPet1, newPet2)
prob10()