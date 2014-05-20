#Eddie Gemayel
#Quiz 3
#May 19 2014
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #creating specific vehicles using sub classes
        bmw = Car()
        boeng = Airplane()



        #setting the new sounds to each vehicle
        bmw.sound = "Vroom"
        boeng.sound = "Swooosh"

        #just to test it
        self.response.write(bmw.movement())


#super abstract class never seen by the user
class Vehicle(object):
    def __init__(self):
        #some typical attributes / properties any vehicle would have
        self.__sound = "Default"
        self.weight = 0
        self.top_speed = 0
        self.passengers = 0

    #some typical functions any vehicle would have
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

#sub classes of more specific types of vehicles created from the vehicle super class
class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.weight = 1000
        self.top_speed = 150
        self.passengers = 4
        self.wheels = 4
        self.miles_per_gallon = 30
        self.power_steering = "Yes"

    def movement(self):
        print "I am driving somewhere"

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

    def movement(self):
        print "I am flying somewhere"

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, new):
        self.__sound = new



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)