#Eddie Gemayel
#Quiz 4
#Getters and
#Setters
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        page = Page()

        global counter

        if self.request.GET:
            counter += 1

        else:
            counter = 0


        page.count = counter

        #page.update()
        self.response.write(page.print_out())

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

        self.close = """
    </body>
</html>
        """


    def print_out(self):

        return self.open + self.close

class Counter(object):
    def __init__(self):
        self.content = """
        {self.count}
        """
        self.__button = """

        <br/>
        <a href='?count=count'>Count Up</a>
        """

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, c):
        self.__count = c
        self.content.format(**locals())

    @property
    def button(self):
        return self.__button

    @button.setter
    def button(self, b):
        self.__button = b


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)