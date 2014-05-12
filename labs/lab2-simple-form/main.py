import webapp2

#import HTML pages to be loaded later
from page import HTMLFormPage
from page2 import HTMLDisplayPage

#main handler class
class MainHandler(webapp2.RequestHandler):

    def get(self):
        #calling constructor function
        #store pages in simple variables
        p = HTMLFormPage()
        d = HTMLDisplayPage()

        #if information is delievered, load 'd' variable which is HTML display page
        if self.request.GET:
            #store the information gathered into variables
            fn = self.request.GET["firstname"]
            ln = self.request.GET["lastname"]
            pn = self.request.GET["phone"]
            day = self.request.GET["days"]
            pos = self.request.GET["position"]
            #call out print_out function which displays the information
            self.response.write(d.print_out("<div class='wrapper'><p><strong>First Name:</strong> " + fn + "</p><p><strong>Last Name:</strong> " + ln + "</p><p><strong>Phone Number:</strong> " + pn + "</p><p><strong>Preferred Day To Play:</strong> " +day+"</p><p><strong>Position:</strong> "+pos+"</p></div>"))
        #if no info is collected, just display the form, variable 'p'
        else:
            self.response.write(p.print_out(" "))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)