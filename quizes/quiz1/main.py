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