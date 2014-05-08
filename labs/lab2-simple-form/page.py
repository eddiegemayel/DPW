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
            <input type="text" name="firstname" placeholder="Enter Your First Name"/>
            <input type="text" name="lastname" placeholder="Enter Your Last Name"/>
            <input type="text" name="phone" placeholder="Enter Your Contact Phone Number"/>
            <button name="submit">Enter</button>
        </form>
        '''
        self.page_close = '''
    </body>
</html>
'''
    def print_out(self, content):

        return self.page_open + self.page_content + content + self.page_close