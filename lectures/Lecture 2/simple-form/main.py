import webapp2
#from 'file' import 'classname'
from page import HTMLPage

#blueprint for creating our web app
class MainHandler(webapp2.RequestHandler):
    #catalyst - starts our web app
    #when this app loads ... this function gets called automagically
    def get(self):
        #calling constructor function
        p = HTMLPage()

        if self.request.GET:
            fn = self.request.GET["firstname"]
            ln = self.request.GET["lastname"]
            self.response.write(p.print_out(fn+ " "+ ln))
        else:
            self.response.write(p.print_out(" "))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)