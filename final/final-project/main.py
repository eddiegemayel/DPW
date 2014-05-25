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
        view.form_header = "<h1>Search Song Lyrics!</h1>"
        view.title = "Lyrics Wiki"
        self.response.write(view.print_out())


        if self.request.GET:
            artist = self.request.GET["code1"]
            song = self.request.GET["code2"]

            artist.replace(" ", "_")
            song.replace(" ", "_")

            url = "http://lyrics.wikia.com/api.php?artist="+artist+"&song="+song+"&fmt=xml"
            #go get the api info
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req)

            #parse it
            xmldoc = minidom.parse(data)


            #look at elements within the xml

            self.response.write(xmldoc.getElementsByTagName("artist")[0].firstChild.nodeValue + "<br/>")
            self.response.write(xmldoc.getElementsByTagName("song")[0].firstChild.nodeValue + "<br/>")
            self.response.write(xmldoc.getElementsByTagName("lyrics")[0].firstChild.nodeValue)






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)