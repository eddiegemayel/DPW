#Eddie Gemayel
#Final Practical
#May 30 2014
import webapp2
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = Page()
        #Testing to see if i could get a name to show up. it worked.
        # req = urllib2.Request("http://rebeccacarroll.com/api/got/got.xml")
        # opener = urllib2.build_opener()
        # data = opener.open(req)
        # xmldoc = minidom.parse(data)
        #
        #
        #
        #
        # print(xmldoc.getElementsByTagName("name")[0].firstChild.nodeValue)

        if self.request.GET:
            got_model = GOTModel()

            got_model.send_req()

            got_view = GOTView()

            got_view.GOTdo = got_model.GOTdo

            got_view.populate()

            view.page_content = got_view.content


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

        self.GOTdo.name = xmldoc.getElementsByTagName("name")[0].firstChild.nodeVaule


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
        <link rel="stylesheet" href="css/main.css"/>
    </head>
    <body>
        <a href="">Click here for Lannister</a>
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
