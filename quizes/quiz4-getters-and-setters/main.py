#Eddie Gemayel
#Quiz 4
#Getters and
#Setters
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):


        self.response.write('Hello world!')


class Page(object):
    def __init__(self):

        self.__count = 0
        self.open = """
<!DOCTYPE html>
<html>
    <head>
        <title>Quiz 4: Count</title>
    </head>
    <body>
        """
        self.count_area = """
        {self.count}
        """
        self.__button = """
        <a href=?count=button>Count Up</a>
        """
        self.close = """
    </body>
</html>
        """


    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, c):
        self.__count = c


    @property
    def button(self):
        return self.__button

    @button.setter
    def button(self, b):
        self.__button = b


    def update(self):
        self.count_area.format(**locals())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)