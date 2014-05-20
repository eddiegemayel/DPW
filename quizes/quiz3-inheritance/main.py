#Eddie Gemayel
#Quiz 3
#May 19 2014
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        bmw = Car()
        boeng = Airplane()

        bmw.sound = "Vroom"
        boeng.sound = "Swooosh"

        self.response.write(boeng.sound)



class Vehicle(object):
    def __init__(self):
        self.__sound = "Default"
        self.weight = 0
        self.top_speed = 0
        self.passengers = 0

    def movement(self):
        print "I am moving somewhere"

    def refuel(self):
        print "Gotta fuel up again!"


    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new):
        self.__sound = new

class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.weight = 1000
        self.top_speed = 150
        self.passengers = 4
        self.wheels = 4
        self.miles_per_gallon = 30
        self.power_steering = "Yes"

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new):
        self.__sound = new

class Airplane(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.weight = 100000
        self.top_speed = 600
        self.passengers = 200
        self.bathrooms = 2
        self.in_flight_movie = "Yes"
        self.snacks = "Yes"

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new):
        self.__sound = new



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
