#Eddie Gemayel
#May 12 2014
#Lab 3
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_page = Page()

        self.ronaldo = Player()
        self.ronaldo.name = "Christiano Ronaldo"
        self.ronaldo.position = "Forward"
        self.ronaldo.team = "Real Madrid"
        self.ronaldo.games = 165.0
        self.ronaldo.goals = 177.0
        self.ronaldo.calc_goals_per_game()
        print self.ronaldo.goals_per_game

        self.zlatan = Player()
        self.zlatan.name = "Zlatan Ibrahimovic"
        self.zlatan.position = "Forward"
        self.zlatan.team = "PSG"
        self.zlatan.games = 66.0
        self.zlatan.goals = 55.0
        self.zlatan.calc_goals_per_game()
        print self.zlatan.goals_per_game


        self.pogba = Player()
        self.pogba.name = "Paul Pogba"
        self.pogba.position = "Midfielder"
        self.pogba.team = "Juventus"
        self.pogba.games = 56.0
        self.pogba.goals = 11.0
        self.pogba.calc_goals_per_game()
        print self.pogba.goals_per_game

        self.yaya = Player()
        self.yaya.name = "Yaya Toure"
        self.yaya.position = "Midfielder"
        self.yaya.team = "Manchester City"
        self.yaya.games = 131.0
        self.yaya.goals = 38.0
        self.yaya.calc_goals_per_game()
        print self.yaya.goals_per_game

        self.rues = Player()
        self.rues.name = "Marco Rues"
        self.rues.position = "Winger"
        self.rues.team = "Dortmund"
        self.rues.games = 61.0
        self.rues.goals = 30.0
        self.rues.calc_goals_per_game()
        print self.rues.goals_per_game

        players = [self.ronaldo, self.zlatan, self.pogba, self.yaya, self.rues]
        print players


        home_page.title = "Home Page"
        home_page.update()

        ronaldo_page = Page()
        ronaldo_page.title = "Ronaldo"
        ronaldo_page.update()

        # if Player == ronaldo:
        #     self.response.write(ronaldo_page.print_out())
        # else:
        #     self.response.write(home_page.print_out())


#############################################---------------player class
class Player(object):
    def __init__(self):
        self.name = ""
        self.position = ""
        self.team = ""
        self.games = 0.0
        self.goals = 0.0
        self.__goals_per_game = 0.0



    @property
    def goals_per_game(self):
        return self.__goals_per_game

    @goals_per_game.setter
    def goals_per_game(self, value):
        self.__goals_per_game = value

    def calc_goals_per_game(self):
        total = self.goals / self.games
        self.__goals_per_game = total


#############################################---------------page class

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
        self.__content = """
        <h1>Greatest Footballers In The World</h1>
        <h2>Click on a great footballer to learn more about their stats</h2>
        <ul>
            <li><a href="?Player=ronaldo">Ronaldo</a></li>
            <li><a href="?player=zlatan">Zlatan Ibrahimovic</a></li>
            <li><a href="?player=pogba">Paul Pogba</a></li>
            <li><a href="?player=yaya">Yaya Toure</a></li>
            <li><a href="?player=rues">Marco Rues</a></li>
        </ul>
        """
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