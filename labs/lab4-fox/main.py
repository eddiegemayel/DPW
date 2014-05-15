import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()
        p.title = "Animal Home Page"

        eagle = Eagle()
        pig = Pig()
        horse = Horse()

        eagle.sound = "Caaaaw!"
        pig.sound = "Oink Oink!"
        horse.sound = "Neigh!"

        animals = [eagle, pig, horse]

        print animals[0]

        



class Page(object):
    def __init__(self):
        self._open = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title><!--calling the function-->
        <link rel ="stylesheet" type="text/css" href="{self.css_url}"/>
    </head>
    <body>
        """
        self._content = "This is my home DEFAULT content"
        self._close = """
    </body>
</html>"""
        self._css_url = ""
        self._title = ""
        self.all = ""

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def css_url(self):
        return self._css_url

    @css_url.setter
    def css_url(self, c):
        self._css_url = c

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())

class Animal(object):
    def __init__(self):
        self.phylum = ""
        self.classs = ""
        self.order = ""
        self.family = ""
        self.genus = ""
        self.lifespan = ""
        self.habitat = ""
        self.location = ""
        self.__sound = "Default"

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new):
        self.__sound = new

class Eagle(Animal):
    def __init__(self):
        Animal.__init__(self)

        self.phylum = "Chordata"
        self.classs = "Aves"
        self.order = "Accipitriformes"
        self.family = "Accipitridae"
        self.genus = "Haliaeetus"
        self.lifespan = "Around 20 years"
        self.habitat = "Wetlands"
        self.location = "North America"

    @property
    def sound(self):
        return self.__sound
    @sound.setter
    def sound(self, new):
        self.__sound = new

class Pig(Animal):
    def __init__(self):
        Animal.__init__(self)

        self.phylum = "Chordata"
        self.classs = "Mammalia"
        self.order = "Artiodactyla"
        self.family = "Suidae"
        self.genus = "Sus"
        self.lifespan = "Around 8 years"
        self.habitat = "Anywhere with enough water"
        self.location = "Americas, Eurasia, Africa"

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new):
        self.__sound = new

class Horse(Animal):
    def __init__(self):
        Animal.__init__(self)

        self.phylum = "Chordata"
        self.classs = "Mammalia"
        self.order = "Perissodactyla"
        self.family = "Equidae"
        self.genus = "Equus"
        self.lifespan = "Between 25-30 years"
        self.habitat = "Open Grass Plains"
        self.location = "Americas, Europe"

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new):
        self.__sound = new


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)