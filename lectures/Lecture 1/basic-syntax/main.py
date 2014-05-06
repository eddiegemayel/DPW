#Single Line Comments
'''
This is a multiple line comment yo
Eddie Gemayel
May 5th 2014
DPW
'''

#print "Hello World!"

first_name = "Kermit "
last_name = "Da Frog"
year_born = 1994

print first_name + last_name

age = 2014 - year_born

#Assignment Operators
#-= *= += /=

#print age

'''
if(year_born < 1990){
    print "you are part of generation y"
}
'''

# if year_born < 1990:
#     pass
# elif year_born > 1978:
#     print "you are gen X"
# else:
#     print "yeah"

#arrays
students = ["Nicole", "Eli", "Gabriel", "Jordan", "Eddie"]
students.append("Arturo")
# students.reverse()
# students = students[0].lower()
#print students


#dictionaries - associative arrays
# Just like an array, without indexes
#name_of_dictionary = {"key":value}
class_info = {"students": students, "roster count":9, "room": "FS4A 107"}

print class_info["roster count"]


#loops yo
for s in students:
    print s + ", you are awesome."

    if s == "Jordan":
        break


#for i in range (start, end, incement/decrement)
# start at 0 stop at 5


import random


for i in range(0,5):
    print students[i]







for i in range(0,1):
    print random.randrange(20)


#functions
#defintions
def calc_area(h, w):
    area = h * w
    return area

a = calc_area(6, 8)

print a


#format string method

username = "ZugZug"
join_date = 2001

message = '''
Welcome to our site {username}!
its horrible that you are here
why are you here, you've been here since {join_date}!
'''

message = message.format(**locals())

print message



#getting info from the user
first = raw_input("Type yo first name ya fucking fool: ")
print first + " , wow, nice to fucking meet you"


#type yo age
number = raw_input("Type yo fucking age fool")
print str(int(number)) +"You younginhi"