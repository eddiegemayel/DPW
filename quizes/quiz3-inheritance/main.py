#Eddie Gemayel
#Quiz 3
#May 19 2014
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        bmw = Car()

        bmw.sound = "Vroom"

        self.response.write(bmw.sound)



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



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
