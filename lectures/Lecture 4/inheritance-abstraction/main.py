import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
