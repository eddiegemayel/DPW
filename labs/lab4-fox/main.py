import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
        pass


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

class Animal(object):
    def __init__(self):
        self.phylum = ""
        self.classs = ""
        self.order = ""
        self.family = ""
        self.genus = ""
        self.lifespan = ""
        self.habitat = ""
        self.location = ""
        self.sound = ""

    def sound(self):
        return self.sound


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)