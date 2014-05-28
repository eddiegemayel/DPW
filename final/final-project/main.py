#Eddie
#final project
#may 19 2014
import webapp2
from page import *
#import json , for json file
from xml.dom import minidom #library for working with xml in python
import urllib2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view.title = "Lyrics Wiki API"

        if self.request.GET:
            # artist = self.request.GET["code1"]
            # song = self.request.GET["code2"]

            l_model = LyricModel() #creates instance of the model
            l_model.code1 = self.request.GET["code1"]
            l_model.code2 = self.request.GET["code2"]
            l_model.send_req()

            l_view = LyricView()

            l_view.ldo = l_model.ldo # transfers wdo from model to the view

            l_view.update()

            view.page_content = l_view.content


        self.response.write(view.print_out())


class LyricModel(object):
    """ this class handles data requests
    """
    def __init__(self):
        self.url = "http://lyrics.wikia.com/api.php?artist="
        self.__code1 = ""
        self.__code2 = ""

    def send_req(self):

        req = urllib2.Request(self.url +self.code1+"&song="+self.code2+"&fmt=xml")
        opener = urllib2.build_opener()
        data = opener.open(req)
        #parse it
        xmldoc = minidom.parse(data)

        #find tags we want..and put it into instance of weather data object
        self.__ldo = LyricDataObject() #create instance of data object class

        self.__ldo.artist = xmldoc.getElementsByTagName("artist")[0].firstChild.nodeValue
        self.__ldo.song = xmldoc.getElementsByTagName("song")[0].firstChild.nodeValue
        self.__ldo.lyrics = xmldoc.getElementsByTagName("lyrics")[0].firstChild.nodeValue

    #dont want anyone overwriting data object im making it a property
    #with just the getter


    @property
    def ldo(self):
        return self.__ldo


    @property
    def code1(self):
        return self.__code1

    @code1.setter
    def code1(self, c):
        self.__code1 = c


    @property
    def code2(self):
        return self.__code2

    @code2.setter
    def code2(self, c):
        self.__code2 = c



class LyricDataObject(object):
    """
    this holds info sent in by the api
    """

    def __init__(self):
        self.artist = ""
        self.song = ""
        self.lyrics = ""


class LyricView(object):
    #just showing weather info from the api
    def __init__(self):
        self.wdo = LyricDataObject()
        self.content = ""

    def update(self):
        self.content = '''
        <div>
            <h3>Song : {self.ldo.song}</h3>
                <p><strong>By : </strong> {self.ldo.artist}</p>
                <p><strong>Lyric Preview : </strong> {self.ldo.lyrics}</p>
        </div>

        '''
        self.content = self.content.format(**locals())


            #old code
            # artist.replace(" ", "_")
            # song.replace(" ", "_")

            #url = "http://lyrics.wikia.com/api.php?artist="+artist+"&song="+song+"&fmt=xml"
            #go get the api info
            # req = urllib2.Request(url)
            # opener = urllib2.build_opener()
            # data = opener.open(req)

            #parse it
            #xmldoc = minidom.parse(data)


            #look at elements within the xml

            # self.response.write(xmldoc.getElementsByTagName("artist")[0].firstChild.nodeValue + "<br/>")
            # self.response.write(xmldoc.getElementsByTagName("song")[0].firstChild.nodeValue + "<br/>")
            # self.response.write(xmldoc.getElementsByTagName("lyrics")[0].firstChild.nodeValue)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)