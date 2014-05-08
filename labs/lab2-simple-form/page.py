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
        <h1>Sign Up For The Soccer Team</h1>
        <form method="GET" action="">
            <label for="firstname">First Name:</label>
            <input type="text" name="firstname" placeholder="Enter Your First Name"/>
            <label for="lastname">Last Name:</label>
            <input type="text" name="lastname" placeholder="Enter Your Last Name"/>
            <label for="phone">Phone Number:</label>
            <input type="text" name="phone" placeholder="Enter Your Contact Phone Number"/>
            <br/>
            <label for="friday">Friday:</label>
            <input type="checkbox" name="days" value="friday" checked="checked"/>
            <label for="saturday">Saturday:</label>
            <input type="checkbox" name="days" value="saturday"/>
            <label for="sunday">Sunday:</label>
            <input type="checkbox" name="days" value="sunday"/>
            <button name="submit">Enter</button>
        </form>
        '''
        self.page_close = '''
    </body>
</html>
'''

    def print_out(self, content):

        return self.page_open + self.page_content + content + self.page_close