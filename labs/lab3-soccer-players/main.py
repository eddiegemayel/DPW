#Eddie Gemayel
#May 12 2014
#Lab 3
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #home page being created from page object
        home_page = Page()

        #creating each player from the Player class object
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

        #making an array for each player that clicking a link will reference too
        players = [self.ronaldo, self.zlatan, self.pogba, self.yaya, self.reus]

        #Setting home page title
        home_page.title = "Home Page"
        home_page.update()

        #write out the page opening and navigation. they should always stay there
        self.response.write(home_page.open + home_page.nav)

        #if info is recieved
        if self.request.GET:
            #get which player was selected
            player = int(self.request.GET['player'])
            print player

            #gather info on the selected player
            name = players[player].name
            position = players[player].position
            team = players[player].team
            games_played = players[player].games_played
            goals = players[player].goals
            goals_per = players[player].goals_per_game


            #self.title(name)


            home_page.title = name
            home_page.update()

            #content area that will dynamically change depending on selected player
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
                <img class="pic" src="css/images/{player}.jpg"/>
                </div>'''


            #format local variables
            content = content.format(**locals())

            #write out the content and page close
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


    #getter and setter for determining average goals per game
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
        self.__title = "Footballers"
        self.open = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Alegreya+Sans+SC' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=PT+Sans|PT+Sans+Narrow' rel='stylesheet' type='text/css'>
    </head>
    <body>"""
        self.nav = """
        <h1>Greatest Footballers In The World</h1>
        <h2>Click on a legend to learn more</h2>
        <div class="linkContainer">
        <ul>
            <li><a href="?player=0">Ronaldo</a></li>
            <li><a href="?player=1">Zlatan</a></li>
            <li><a href="?player=2">Pogba</a></li>
            <li><a href="?player=3">Toure</a></li>
            <li><a href="?player=4">Reus</a></li>
        </ul>
        </div>
        """
        self.close = """
    </body>
</html> """

        self.all = self.open + self.nav + self.close

    #Getter
    @property
    def title(self):
        return self.__title

    #Setter
    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()

    def print_out(self):
        return self.all

    def update(self):
        self.all = self.all.format(**locals())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)