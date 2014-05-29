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
        #make the view from the form page
        view = FormPage()
        view.title = "Lyrics Wiki API"

        if self.request.GET:
            #creates instance of the model
            l_model = LyricModel()

            #replace any spaces in the entry with underscores so the API understands it
            l_model.code1 = self.request.GET["code1"].replace(" ", "_")
            l_model.code2 = self.request.GET["code2"].replace(" ", "_")

            #send the data and parse it with send_req method
            l_model.send_req()

            #create instance of lyric view
            l_view = LyricView()

            # transfers wdo from model to the view
            l_view.ldo = l_model.ldo

            #update view and format the locals
            l_view.update()

            #make the empty page_content string into the content from lyric view
            view.page_content = l_view.content

        #print it all oout
        #its important that this print out is here and NOT inside the if statement
        self.response.write(view.print_out())


class LyricModel(object):
    #this class handles data requests

    def __init__(self):
        self.url = "http://lyrics.wikia.com/api.php?artist="
        self.__code1 = ""
        self.__code2 = ""

    def send_req(self):
        #collects and parses the xml data
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
        self.__ldo.lyric_url = xmldoc.getElementsByTagName("url")[0].firstChild.nodeValue

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
    #this holds info sent in by the api
    def __init__(self):
        #empty variables that will be filled later
        self.artist = ""
        self.song = ""
        self.lyrics = ""


class LyricView(object):
    #just showing weather info from the api
    def __init__(self):

        self.ldo = LyricDataObject()
        self.content = ""

    def update(self):
        #update the content with variables than format the locals

        self.content = '''
        <div class="content">
            <h3 class="song">{self.ldo.song}</h3>
                <p><strong>By - </strong><em>{self.ldo.artist}</em></p>
                <p><strong>Lyric preview : </strong> <em>{self.ldo.lyrics}</em></p>
                <p><strong><a href="{self.ldo.lyric_url}">Link to full lyrics</a></strong></p>
        </div>

        '''
        self.content = self.content.format(**locals())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)