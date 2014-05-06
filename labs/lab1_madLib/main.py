'''
Eddie Gemayel
May 5th 2014
DPW
Lab1 MadLib
'''
names_array = []
#this array will be accessed by the if statement
car_array = ["BMW", "Lambo", "Honda", "Ford"]
villain_array = ["Darth Vader", "Green Goblin", "The Joker", "Lex Luthor"]

import random



#collecting inputs from the user
name1 = raw_input("Type a Name! ")
name2 = raw_input("Type a second Name! ")


verb1 = raw_input("Type a past tense Verb! ")
verb2 = raw_input("Type another past tense Verb! ")

number1 = raw_input("Type a number between (and/or including) 0 and 3! ")
number2 = raw_input("Type another number between (and/or including) 0 and 3! ")
number3 = raw_input("Type your age! ")


class_verbs = {"verb1": verb1, "verb2": verb2}


names_array.append(name1)
names_array.append(name2)

def car_select(num):
    if num == 0:
        return car_array[0]
    elif num == 1:
        return car_array[1]
    elif num == 2:
        return car_array[2]
    elif num == 3:
        return car_array[3]
    elif num > 3 or num < 0:
        return "Chevy"

def villain_select(num):
    if num == 0:
        return villain_array[0]
    elif num == 1:
        return villain_array[1]
    elif num == 2:
        return villain_array[2]
    elif num == 3:
        return villain_array[3]
    elif num > 3 or num < 0:
        return "Dr. Evil"

def random_people():
    for i in range(0,1):
        return random.randrange(10000)


car = car_select(int(number1))
villain = villain_select(int(number2))
v_num = int(number3) * 2

r_number = random_people()

print r_number


#print names_array
#print class_verbs

story = '''
This is the story about {names_array[0]}. He/She was driving around in his/her {car}, when a villain named {villain} appeared
out of nowhere! {villain} was {v_num} years old...which was 2X older than {names_array[0]}, who was a young {number3} years of age!
{names_array[0]} called {villain} 'old'...this angered {villain} and was a cause to fight...until their good friend {names_array[1]}
came to save the day! {names_array[1]} came in and {class_verbs[verb1]} {villain} right in the face! Ouch! {villain} {class_verbs[verb2]} to the floor and died.
{names_array[1]} had saved the day, and their friend {names_array[0]}. Hoorah! The {r_number} people of the city were elated
that the villain had been destroyed!

'''

story = story.format(**locals())



print story

