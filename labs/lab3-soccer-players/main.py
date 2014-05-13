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
        self.ronaldo.games_played = 165.0
        self.ronaldo.goals = 177.0
        self.ronaldo.calc_goals_per_game()
        print self.ronaldo.goals_per_game

        self.zlatan = Player()
        self.zlatan.name = "Zlatan Ibrahimovic"
        self.zlatan.position = "Forward"
        self.zlatan.team = "PSG"
        self.zlatan.games_played = 66.0
        self.zlatan.goals = 55.0
        self.zlatan.calc_goals_per_game()
        print self.zlatan.goals_per_game


        self.pogba = Player()
        self.pogba.name = "Paul Pogba"
        self.pogba.position = "Midfielder"
        self.pogba.team = "Juventus"
        self.pogba.games_played = 56.0
        self.pogba.goals = 11.0
        self.pogba.calc_goals_per_game()
        print self.pogba.goals_per_game

        self.yaya = Player()
        self.yaya.name = "Yaya Toure"
        self.yaya.position = "Midfielder"
        self.yaya.team = "Manchester City"
        self.yaya.games_played = 131.0
        self.yaya.goals = 38.0
        self.yaya.calc_goals_per_game()
        print self.yaya.goals_per_game

        self.reus = Player()
        self.reus.name = "Marco Reus"
        self.reus.position = "Winger"
        self.reus.team = "Dortmund"
        self.reus.games_played = 61.0
        self.reus.goals = 30.0
        self.reus.calc_goals_per_game()
        print self.reus.goals_per_game

        players = [self.ronaldo, self.zlatan, self.pogba, self.yaya, self.reus]


        home_page.title = "Home Page"
        home_page.update()




        self.response.write(home_page.open + home_page.nav)

        if self.request.GET:
            player = int(self.request.GET['player'])
            print player

            name = players[player].name
            position = players[player].position
            team = players[player].team
            games_played = players[player].games_played
            goals = players[player].goals
            goals_per = players[player].goals_per_game

            home_page.title = name
            home_page.update()

            content='''<div id="contentArea">
            <h3>{name}</h3>
                <section id="labelArea">
                    <p class="label"><strong>Position:</strong></p>
                    <p class="label"><strong>Team:</strong></p>
                    <p class="label"><strong>Games Played:</strong></p>
                    <p class="label"><strong>Goals Scored:</strong></p>
                    <p class="label"><strong>Average Goals Per Game Scored:</strong></p>
                </section>

                <section id="statArea">
                    <p class="stats">{position}</p>
                    <p class="stats">{team}</p>
                    <p class="stats">{games_played}</p>
                    <p class="stats">{goals}</p>
                    <p class="stats">{goals_per}</p>
                </section>
                <img src="css/images/{player}.jpg"/>
                </div>'''


            content = content.format(**locals())

            self.response.write(content)
        self.response.write(home_page.close)


#############################################---------------player class
class Player(object):
    def __init__(self):
        self.name = ""
        self.position = ""
        self.team = ""
        self.games_played = 0.0
        self.goals = 0.0
        self.__goals_per_game = 0.0



    @property
    def goals_per_game(self):
        return self.__goals_per_game

    @goals_per_game.setter
    def goals_per_game(self, value):
        self.__goals_per_game = value

    def calc_goals_per_game(self):
        total = self.goals / self.games_played
        self.__goals_per_game = total


#############################################---------------page class

class Page(object):
    def __init__(self):
        self.title = ""
        self.open = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
    </head>
    <body>"""
        self.nav = """
        <h1>Greatest Footballers In The World</h1>
        <h2>Click on a great footballer to learn more about their stats</h2>
        <ul>
            <li><a href="?player=0">Ronaldo</a></li>
            <li><a href="?player=1">Zlatan</a></li>
            <li><a href="?player=2">Paul Pogba</a></li>
            <li><a href="?player=3">Yaya Toure</a></li>
            <li><a href="?player=4">Marco Rues</a></li>
        </ul>
        """
        self.close = """
    </body>
</html> """

        self.all = self.open + self.nav + self.close


    def print_out(self):
        return self.all

    def update(self):
        self.all = self.all.format(**locals())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)