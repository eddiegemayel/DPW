#Eddie Gemayel
#May 12 2014
#Lab 3
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_page = Page()
        home_page.update()
        home_page.title = "Home Page"

        ronaldo = Player()



        zlatan = Player()
        pogba = Player()
        yaya = Player()
        rues = Player()



        self.response.write(home_page.print_out())


#############################################player class
class Player(object):
    def __init__(self):
        self.name = ""
        self.position = ""
        self.team = ""
        self.__games = 0
        self.goals = 0
        self.__goals_per_game = 0


    def print_info(self):
        #prints out any info
        pass

    @property
    def games(self):
        return self.__games

    @games.setter
    def games(self, value):
        pass

#############################################page class

class Page(object):
    def __init__(self):
        self.__title = "Home Page"
        self.__open = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
    </head>
    <body>"""
        self.__content = ""
        self.__close = """
    </body>
</html> """
        self.__all = self.__open + self.__content + self.__close

    


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
