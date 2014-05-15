import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.title = "Yao"
        p.form_header = "Enter ya name ya twat"
        p.css_url = "css/styles.css"
        self.response.write(p.print_out())

        p2 = FormPage()



class Page(object):
    def __init__(self):
        self._open = """
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title><!--calling the function-->
        <link rel ="stylesheet" type="text/css" href="{self.css_url}"/>
    </head>
    <body>
        """
        self._content = "This is my DEFAULT content"
        self._close = """
    </body>
</html>"""
        self._css_url = ""
        self._title = ""
        self.all = ""

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = t

    @property
    def css_url(self):
        return self._css_url

    @css_url.setter
    def css_url(self, c):
        self._css_url = c

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())

class FormPage(Page):
    def __init__(self):
        #call that constructor hoe
        Page.__init__(self)
        #super(FormPage, self).__init__()

        self.__form_open = """
        <form method="GET" action="">"""
        self.__inputs = """
        <input type="text" name = "f_name" />
        <input type="text" name = "l_name" />
        <input type="submit" name = "submit" />
        """
        self.__form_close = """</form>"""
        self.form_header = ">>Form Header<<"
        self._content = self.form_header + self.__form_open + self.__inputs + self.__form_close


    def update(self):
        self.all = self._open + self.form_header + self.__form_open + self.__inputs + self.__form_close + self._close
        self.all = self.all.format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)