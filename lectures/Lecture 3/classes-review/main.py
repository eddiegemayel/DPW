import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write('Hello world!')

        yoda = Character()
        yoda.name = "Master Yoda"
        yoda.age = 900
        yoda.occupation = "Jedi Master"
        yoda.gender = "Dude"
        yoda.print_info()

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.age = 30
        luke.occupation = "Jedi"
        luke.gender = "Dude"
        luke.print_info()

        leia = Character()
        leia.name = "Leia Organa"
        leia.occupation = "Princess"
        leia.gender = "Chick"
        leia.age = luke.age
        leia.squad_no = "pink 5"
        print leia.squad_no


class Character(object):
    def __init__(self): #contrustor function
        self.name = ""
        self.__age = 0
        self.occupation = ""
        self.gender = ""
        self.__rogue_squadron_no = "DEFAULT"


    def print_info(self):
        print self.name + " is a(n) "+ self.occupation

    @property
    def age(self):
        return age

    age.setter
    def age(self, value):
        if age < 0:
            print "You can't be less than 0 ya shit"
        self.__age = value

    #read access
    @property
    def squad_no(self):
        return self.__rogue_squadron_no

    #write access
    @squad_no.setter
    def squad_no(self, value):
        if value == "pink 5":
            value = "red 6"
        print value
        self.__rogue_squadron_no = value

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
