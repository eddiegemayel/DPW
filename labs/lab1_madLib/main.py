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



#collecting inputs from the user
name1 = raw_input("Type a Name! ")
name2 = raw_input("Type a second Name! ")


verb1 = raw_input("Type a past tense Verb! ")
verb2 = raw_input("Type a second Verb! ")

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
    elif num > 3:
        return "Chevy"
    elif num < 0:
        return "Pontiac"

def villain_select(num):
    if num == 0:
        return villain_array[0]
    elif num == 1:
        return villain_array[1]
    elif num == 2:
        return villain_array[2]
    elif num == 3:
        return villain_array[3]
    elif num > 3:
        return "Dr. Evil"
    elif num < 0:
        return "Two-Face"



car = car_select(int(number1))
villain = villain_select(int(number2))
v_num = int(number3) * 2


#print names_array
#print class_verbs

story = '''
This is the story about {names_array[0]}. He was driving around in his {car}, when a villain named {villain} wanted to fight
him. {villain}'s was {v_num} years old...which was 2X older than {names_array[0]}, who was only {number3}!
This was a cause to fight...until his good friend {names_array[1]} came to save the day! {names_array[1]} came in and {verb1}
{villain} right in the face!

'''

story = story.format(**locals())



print story