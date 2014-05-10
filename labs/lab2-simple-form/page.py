class HTMLFormPage(object):
    def __init__(self):
        self.page_open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Big League Futbol</title>
        <link href="css/main.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        '''
        self.page_content = '''
        <h1>Sign Up For The Futbol Team</h1>
        <form method="GET" action="">
            <h2>Basic Info</h2>
            <label for="firstname">First Name:</label>
            <input type="text" name="firstname" placeholder="Enter Your First Name"/>
            <label for="lastname">Last Name:</label>
            <input type="text" name="lastname" placeholder="Enter Your Last Name"/>
            <label for="phone">Phone Number:</label>
            <input type="text" name="phone" placeholder="Enter Your Contact Phone Number"/>

            <br/>
            <h2>What Day Would You Prefer To Play On?</h2>

            <label for="friday">Friday:</label>
            <input type="checkbox" name="days" value="Friday" checked="checked"/>
            <label for="saturday">Saturday:</label>
            <input type="checkbox" name="days" value="Saturday"/>
            <label for="sunday">Sunday:</label>
            <input type="checkbox" name="days" value="Sunday"/>

            <br/>
            <h2>What Position Do You Play?</h2>

            <select name="position">
                <option value="Striker">Forward/Striker</option>
                <option value="Midfielder">Midfielder</option>
                <option value="Defender">Defender</option>
                <option value="Keeper">Keeper</option>
            </select>
            <button name="submit">Enter</button>
        </form>
        '''
        self.page_close = '''
    </body>
</html>
'''

    def print_out(self, content):

        return self.page_open + self.page_content + content + self.page_close