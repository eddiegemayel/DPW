#Eddie Gemayel
#May 12 2014
#Lab 3
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_page = Page()
        home_page.title = "Home Page"
        home_page.update()
        ronaldo = Player()

        ronaldo.name = "Christiano Ronaldo"
        ronaldo.position = "Forward"
        ronaldo.team = "Real Madrid"
        ro_ga = ronaldo.games = 165.0
        ro_go = ronaldo.goals = 177.0
        ronaldo.goals_per_game = ro_go / ro_ga
        print ronaldo.goals_per_game

        zlatan = Player()
        zlatan.name = "Zlatan Ibrahimovic"
        zlatan.position = "Forward"
        zlatan.team = "PSG"
        z_ga = zlatan.games = 66.0
        z_go = zlatan.goals = 55.0
        zlatan.goals_per_game = z_go / z_ga
        print zlatan.goals_per_game


        pogba = Player()
        pogba.name = "Paul Pogba"
        pogba.position = "Midfielder"
        pogba.team = "Juventus"
        p_ga = pogba.games = 56.0
        p_go = pogba.goals = 11.0
        pogba.goals_per_game = p_go / p_ga
        print pogba.goals_per_game

        yaya = Player()
        yaya.name = "Yaya Toure"
        yaya.position = "Midfielder"
        yaya.team = "Manchester City"
        y_ga = yaya.games = 131.0
        y_go = yaya.goals = 38.0
        yaya.goals_per_game = y_go / y_ga
        print yaya.goals_per_game

        rues = Player()
        rues.name = "Marco Rues"
        rues.position = "Winger"
        rues.team = "Dortmund"
        re_ga = rues.games = 61.0
        re_go = rues.goals = 30.0
        rues.goals_per_game = re_go / re_ga
        print rues.goals_per_game


        self.response.write(home_page.print_out())


#############################################player class
class Player(object):
    def __init__(self):
        self.name = ""
        self.position = ""
        self.team = ""
        self.__games = 0
        self.goals = 0
        #self.goals_per_game = 0


    def print_info(self):
        pass

    # @property
    # def games(self):
    #     return self.__games
    #
    # @games.setter
    # def games(self, value):
    #     pass
    #
    #
    #
    # @property
    # def goals_per_game(self):
    #     return self.__goals_per_game
    #
    # @goals_per_game.setter
    # def goals_per_game(self, goals, games):
    #     new_value = goals / games
    #     return new_value

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
        self.__content = "Content "
        self.__close = """
    </body>
</html> """

        self.__all = self.__open + self.__content + self.__close


    def print_out(self):
        return self.__all

    def update(self):
        self.__all = self.__all.format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)