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

def count_down(b):
    for i in range(b, 0, -1):
        n = b-1
        string =  "{b} bottles of beer on the wall, {b} bottles of beer...take one down and pass it around. Now you have {n} beers on the wall."
        string = string.format(**locals())
        return string

the_countdown = count_down(int(beer))

print the_countdown