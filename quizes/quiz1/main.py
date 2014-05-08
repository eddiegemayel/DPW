height = raw_input("Enter a height: ")
width = raw_input("Enter a width: ")


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


newArea = calc_area(int(width), int(height))

print newArea


beer = raw_input("Enter your beer")

def count_down(b):
    for i in range(b, 1):
        return b

print count_down(beer)