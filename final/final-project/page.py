class Page(object):
    def __init__(self):
        self._open = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title><!--calling the function-->
        <link rel ="stylesheet" type="text/css" href="css/main.css"/>
        <link href='http://fonts.googleapis.com/css?family=Montserrat|Raleway' rel='stylesheet' type='text/css'>
    </head>
    <body>
        """
        self._content = "This is my DEFAULT content that shouldn't show up"
        self._close = """
    </body>
</html>"""
        self._title = ""
        self.all = ""

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())

class FormPage(Page):
    def __init__(self):
        #call that constructor
        Page.__init__(self)
        #super(FormPage, self).__init__()

        self.__form_open = """
        <h2>Enter an artist and song title</h2>
        <form method="GET" action="">"""
        self.__inputs = """

        <input id="artistInput" type="text" name = "code1" placeholder="Artist name"  />
        <input id="songInput" type="text" name = "code2" placeholder="Song name"  />
        <button class="btn">Search</button>

        """
        self.__form_close = """</form>"""
        self.form_header = """
            <div class="header">
                <h1>Search Song Lyrics</h1>
            </div>
        """
        self.page_content = ""
        #self._content = self.form_header + self.__form_open + self.__inputs + self.__form_close


    def update(self):
        self.all = self._open + self.form_header + self.__form_open + self.__inputs + self.__form_close + self.page_content + self._close
        self.all = self.all.format(**locals())

    def update2(self):
        self.all = self._open + self.page_content + self._close
        self.all = self.all.format(**locals())