#Eddie Gemayel
#Quiz 3
#May 19 2014
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



class Vehicle(object):
    def __init__(self):
        self.__sound = ""
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



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
