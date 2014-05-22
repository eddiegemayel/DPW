#Eddie Gemayel
#Quiz 4
#Getters and
#Setters
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):


        page_counter = Counter()

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

        global counter

        if self.request.GET:
            counter += 1

        else:
            counter = 0


        page_counter.count = counter

        #page.update()
        self.response.write(self.open+self.close)
        self.response.write(page_counter.content + page_counter.button)

class Page(object):
    def __init__(self):
        pass

class Counter(object):
    def __init__(self):
        self.__count = 0
        self.content = """
        {self.count}
        """
        self.__button = """

        <br/>
        <a href='?count=counter'>Count Up</a>
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

    def print_out(self):
        self.content.format(**locals())
        return self.content + self.__button

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)