class HTMLDisplayPage(object):
    def __init__(self):
        self.page_open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Confirmation : Big League Futbol</title>
        <link href="css/main.css" rel="stylesheet" type="text/css"/>
        <link href='http://fonts.googleapis.com/css?family=Francois+One' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Arimo' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
    </head>
    <body>
        '''
        self.page_content = '''
        <h1>This Is The Information You Entered</h1>
        <h2 class="indent">Thank You For Your Interest In Your Local Big League Futbol!</h2>
        <h3 class="indent">See You Out On The Pitch!</h3>
        '''
        self.page_close = '''
    </body>
</html>
'''

    def print_out(self, content):

        return self.page_open + self.page_content + content + self.page_close