'''
Eddie Gemayel
May 5th 2014
DPW
Lab1 MadLib
'''
names_array = []



#collecting inputs from the user
name1 = raw_input("Type a Name! ")
name2 = raw_input("Type a second Name! ")


verb1 = raw_input("Type a Verb! ")
verb2 = raw_input("Type a second Verb! ")

number1 = raw_input("Type a number to be added together! ")
number2 = raw_input("Type another number to be added together! ")
number3 = raw_input("Type your age! ")


class_verbs = {"verb1": verb1, "verb2": verb2}


names_array.append(name1)
names_array.append(name2)


print names_array
print class_verbs

story = '''
This is the story about {names_array[0]}!

'''

story = story.format(**locals())

print story