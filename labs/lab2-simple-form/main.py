import webapp2

from page import HTMLFormPage

class MainHandler(webapp2.RequestHandler):

    def get(self):
        #calling constructor function
        p = HTMLFormPage()

        if self.request.GET:
            fn = self.request.GET["firstname"]
            ln = self.request.GET["lastname"]
            pn = self.request.GET["phone"]
            self.response.write(p.print_out(fn+ " "+ ln + "" + pn))
        else:
            self.response.write(p.print_out(" "))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)