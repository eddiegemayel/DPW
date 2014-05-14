import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()


class Page(object):
    def __init__(self):
        self._open = """
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>
    <body>
        """
        self._content = ""
        self._close = """
    </body>
</html>"""
        self._css_url = ""
        self._title = ""

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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)