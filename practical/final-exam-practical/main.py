#Eddie Gemayel
#Final Practical
#May 30 2014
import webapp2
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #default static page view is created
        view = Page()

        #Testing to see if i could get a name to show up. it worked.
        # req = urllib2.Request("http://rebeccacarroll.com/api/got/got.xml")
        # opener = urllib2.build_opener()
        # data = opener.open(req)
        # xmldoc = minidom.parse(data)


        # src = xmldoc.getElementsByTagName("image")[counter].firstChild.nodeValue
        # self.response.write("<img src="+src+"/>")


        #a link has been clicked
        if self.request.GET:
            #model is created
            got_model = GOTModel()

            #trying to set counter to the value of counter clicked...its not listening
            got_model.newcounter = view.counter

            #send the request with which link user picked
            got_model.send_req()

            #create the dynamic view
            got_view = GOTView()

            #tell it which data object we are using
            got_view.GOTdo = got_model.GOTdo

            #populate the page with new info
            got_view.populate()

            #set the populated info to the page content
            view.page_content = got_view.content

        #write out the page content
        self.response.write(view.update())



class GOTModel(object):
    def __init__(self):
        #store url here along with counter that defaults to 0
        self.url = "http://rebeccacarroll.com/api/got/got.xml"

        self.newcounter = 0

    def send_req(self):
        #parse the xml data recieved from api
        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        xmldoc = minidom.parse(data)

        #instantiate data object
        self.__GOTdo = GOTDataObject()

        #collect info in the xml based on what the counter number is
        self.__GOTdo.name = xmldoc.getElementsByTagName("name")[self.newcounter].firstChild.nodeValue
        self.__GOTdo.sigil = xmldoc.getElementsByTagName("sigil")[self.newcounter].firstChild.nodeValue
        self.__GOTdo.motto = xmldoc.getElementsByTagName("motto")[self.newcounter].firstChild.nodeValue
        self.__GOTdo.head = xmldoc.getElementsByTagName("head")[self.newcounter].firstChild.nodeValue
        self.__GOTdo.image = xmldoc.getElementsByTagName("image")[self.newcounter].firstChild.nodeValue

    @property
    def GOTdo(self):
        return self.__GOTdo

    # @property
    # def counter(self):
    #     return self.__counter
    #
    # @set
    # def counter(self, n):
    #     n = self.counter
    #     return n



class GOTDataObject(object):
    def __init__(self):
        #this is where the empty strings are held to be populated later
        self.name = ""
        self.sigil = ""
        self.motto = ""
        self.head = ""
        self.image = ""

class GOTView(object):
    def __init__(self):
        #the content is empty at first until something is clicked
        self.content = ""
        #create a data object
        self.GOTdo = GOTDataObject()

    def populate(self):
        #this populates with local variables that will be formatted
        self.content = """
        <div class="content">
            <h2><strong>{self.GOTdo.name}</strong></h2>
                <p>Sigil : {self.GOTdo.sigil}</p>
                <p>Motto : {self.GOTdo.motto}</p>
                <p>Head : {self.GOTdo.head}</p>
                <img src="{self.GOTdo.image}"/>
        </div>
        """
        #format the locals
        self.content = self.content.format(**locals())


class Page(object):
    def __init__(self):
        #create data object
        self.GOTdo = GOTDataObject()

        #counter starts at 0...but for whatever reason refuses to change
        self.counter = 0

        #opening of html document
        self.open = """
<!DOCTYPE html>
<html>
    <head>
        <title>Game of Thrones</title>
        <link rel="stylesheet" href="css/main.css"/>
    </head>
    <body>
        <a href="?counter=0">Lannister</a>
        <a href="?counter=1">Stark</a>
        <a href="?counter=2">Baratheon</a>
        <a href="?counter=3">Greyjoy</a>
        <a href="?counter=4">Targaryen</a>
        <a href="?counter=5">Tully</a>
        """
        #page content to be populated by model
        self.page_content = """

        """
        #closing tags
        self.close = """
    </body>
</html>
"""

    def update(self):
        #format locals and return page
        self.open.format(**locals())

        return self.open + self.page_content + self.close



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)