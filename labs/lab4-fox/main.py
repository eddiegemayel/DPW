import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()

        eagle = Eagle()
        pig = Pig()
        horse = Horse()

        eagle.sound = "Caaaaw!"
        pig.sound = "Oink Oink!"
        horse.sound = "Neigh!"

        animals = [eagle, pig, horse]

        print animals[0]

        self.response.write(p._open + p._links)

        if self.request.GET:
            animal = int(self.request.GET['animal'])

            name = animals[animal].name
            phylum = animals[animal].phylum
            classs = animals[animal].classs
            order = animals[animal].order
            family = animals[animal].family
            genus = animals[animal].genus
            lifespan = animals[animal].lifespan
            habitat = animals[animal].habitat
            location = animals[animal].location
            sound = animals[animal].sound

            #p.title = name

            content='''
            <div class="animalContent">
            <h2>The {name}</h2>

                <div class="labelContainer">
                    <p class="label"><strong>Animal Name:</strong></p>
                    <p class="label"><strong>Phylum:</strong></p>
                    <p class="label"><strong>Class:</strong></p>
                    <p class="label"><strong>Order:</strong></p>
                    <p class="label"><strong>Family:</strong></p>
                    <p class="label"><strong>Genus:</strong></p>
                    <p class="label"><strong>Average Lifespan:</strong></p>
                    <p class="label"><strong>Habitat:</strong></p>
                    <p class="label"><strong>Geo-Location:</strong></p>
                    <p class="label"><strong>Sound It Makes:</strong></p>
                </div>

                <div class="infoContainer">
                    <p class="info">{name}</p>
                    <p class="info">{phylum}</p>
                    <p class="info">{classs}</p>
                    <p class="info">{order}</p>
                    <p class="info">{family}</p>
                    <p class="info">{genus}</p>
                    <p class="info">{lifespan}</p>
                    <p class="info">{habitat}</p>
                    <p class="info">{location}</p>
                    <p class="info"><strong>{sound}</strong></p>
                </div>

                <div class="pic">
                    <img src="css/images/{name}.jpg"/>
                </div>

                </div>'''


            #format local variables
            content = content.format(**locals())

            #write out the content and page close
            self.response.write(content)

        self.response.write(p._close)



class Page(object):
    def __init__(self):
        self._open = """
<!DOCTYPE html>
<html>
    <head>
        <title>Much Animals</title>
        <link rel ="stylesheet" type="text/css" href="css/main.css"/>
        <link href='http://fonts.googleapis.com/css?family=Alegreya+Sans+SC|Exo+2|Alef' rel='stylesheet' type='text/css'>
    </head>
    <body>
        """
        self._links = """
        <div class="links">
            <a href="?animal=0">Eagle</a>
            <a href="?animal=1">Pig</a>
            <a href="?animal=2">Horse</a>
        </div>
        """
        self._close = """
    </body>
</html>"""
        self._title = ""
        self.all = ""

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t


    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._links + self._close
        self.all = self.all.format(**locals())

class Animal(object):
    def __init__(self):
        self.name= ""
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
        self.name= "Eagle"
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
        self.name = "Pig"
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
        self.name= "Horse"
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