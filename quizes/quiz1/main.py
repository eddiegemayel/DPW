#collect user inputs
height = raw_input("Enter a height: ")
width = raw_input("Enter a width: ")

#calculates area
def calc_area(w, h):
    if w == h:
        area = w * h
        string =  "The area of your square is {area}"
        string = string.format(**locals())
        return string
    else:
        area = w * h
        string =  "The area of your rectangle is {area}"
        string = string.format(**locals())
        return string


#call out area function
new_area = calc_area(int(width), int(height))

#print the results
print new_area


beer = raw_input("Enter your beer number : ")

def count_down():
    for i in range(int(beer), 0, -1):
        n = int(i)-1
        string =  "{i} bottles of beer on the wall, {i} bottles of beer...take one down and pass it around. Now you have {n} beers on the wall."
        string = string.format(**locals())
        print string

the_countdown = count_down()

print the_countdown