import webapp2

from page import HTMLFormPage

from page2 import HTMLDisplayPage

class MainHandler(webapp2.RequestHandler):

    def get(self):
        #calling constructor function
        p = HTMLFormPage()
        d = HTMLDisplayPage()

        if self.request.GET:
            fn = self.request.GET["firstname"]
            ln = self.request.GET["lastname"]
            pn = self.request.GET["phone"]
            day = self.request.GET["days"]
            pos = self.request.GET["position"]
            self.response.write(d.print_out("<div class='wrapper'><p><strong>First Name:</strong> " + fn + "</p><p><strong>Last Name:</strong> " + ln + "</p><p><strong>Phone Number:</strong> " + pn + "</p><p><strong>Preferred Day To Play:</strong> " +day+"</p><p><strong>Position:</strong> "+pos+"</p></div>"))
        else:
            self.response.write(p.print_out(" "))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)