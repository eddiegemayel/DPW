#getting info from the user
names_array = []




name1 = raw_input("Type a Name!")
name2 = raw_input("Type a second Name!")
name3 = raw_input("Type a third Name!")

verb1 = raw_input("Type a Verb!")
verb2 = raw_input("Type a second Verb!")
verb3 = raw_input("Type a third Verb!")



class_verbs = {"verb1": verb1, "verb2": verb2, "verb3": verb3}
#class_verbs={"verb1":verb1}

names_array.append(name1)
names_array.append(name2)
names_array.append(name3)

print names_array
print class_verbs