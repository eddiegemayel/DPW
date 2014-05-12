class HTMLFormPage(object):
    def __init__(self):
        self.page_open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Big League Futbol</title>
        <link href="css/main.css" rel="stylesheet" type="text/css"/>
        <link href='http://fonts.googleapis.com/css?family=Francois+One' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Arimo' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
    </head>
    <body>
        '''
        self.page_content = '''
        <h1>Sign Up For The Futbol Team</h1>
        <form method="GET" action="">
            <div class="wrapper">
            <h2>Basic Info</h2>
            <div class="section">
            <label for="firstname">First Name:</label>
            <input type="text" name="firstname" placeholder="Enter Your First Name"/>
            <br/>
            <label for="lastname">Last Name:</label>
            <input type="text" name="lastname" placeholder="Enter Your Last Name"/>
            <br/>
            <label for="phone">Phone Number:</label>
            <input type="text" name="phone" placeholder="Enter Your Contact Phone Number"/>
            </div>


            <br/>
            <h2>What Day Would You Prefer To Play On?</h2>
            <div class="section" id="checkboxes">
            <label for="friday">Friday:</label>
            <input type="checkbox" name="days" value="Friday" checked="checked"/>
            <label for="saturday">Saturday:</label>
            <input type="checkbox" name="days" value="Saturday"/>
            <label for="sunday">Sunday:</label>
            <input type="checkbox" name="days" value="Sunday"/>
            </div>

            <br/>
            <h2>What Position Do You Play?</h2>
            <div class="section" id="selection">
            <select name="position">
                <option value="Striker">Forward/Striker</option>
                <option value="Midfielder">Midfielder</option>
                <option value="Defender">Defender</option>
                <option value="Keeper">Keeper</option>
            </select>
            </div>
            <div class="btn">
            <button name="submit" class="css3button">Enter</button>
            </div>
            </div>
        </form>
        '''
        self.page_close = '''
    </body>
</html>
'''

    def print_out(self, content):

        return self.page_open + self.page_content + content + self.page_close