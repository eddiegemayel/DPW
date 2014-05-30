#Eddie Gemayel
#Final Practical
#May 30 2014
import webapp2
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = Page()

        self.response.write(view.update())



class GOTModel(object):
    def __init__(self):
        self.url = "http://rebeccacarroll.com/api/got/got.xml"

    def send_req(self):
        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        xmldoc = minidom.parse(data)

        self.GOTdo = GOTDataObject()


class GOTDataObject(object):
    def __init__(self):
        self.name = ""
        self.sigil = ""
        self.motto = ""
        self.head = ""
        self.image = ""

class GOTView(object):
    def __init__(self):
        self.content = ""
        self.GOTdo = GOTDataObject()

    def populate(self):

        self.content = """
        <div class="content">
            <h2><strong>{self.GOTdo.name}</strong></h2>
                <p>Sigil : {self.GOTdo.sigil}</p>
                <p>Motto : {self.GOTdo.motto}</p>
                <p>Head : {self.GOTdo.head}</p>
                <!--<p><img src="{self.GOTdo.image}"/></p>-->
        </div>
        """
        self.content = self.content.format(**locals())


class Page(object):
    def __init__(self):
        self.open = """
<!DOCTYPE html>
<html>
    <head>
        <title>Game of Thrones</title>
    </head>
    <body>
        """
        self.page_content = """
           Default content
        """
        self.close = """
    </body>
</html>
                """

    def update(self):
        return self.open + self.page_content + self.close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
